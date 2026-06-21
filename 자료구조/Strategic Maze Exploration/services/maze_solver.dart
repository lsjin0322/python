import 'dart:async';
import 'dart:collection';
import '../models/cell.dart';

class MazeSolver {
  final int rows;
  final int cols;
  late List<List<Cell>> grid;
  late Cell startCell;
  late Cell endCell;

  MazeSolver({required this.rows, required this.cols}) {
    _initializeMaze();
  }

  void _initializeMaze() {
    grid = List.generate(
      rows,
      (r) => List.generate(cols, (c) => Cell(row: r, col: c)),
    );

    startCell = grid[1][1]..type = CellType.start;
    endCell = grid[rows - 2][cols - 2]..type = CellType.end;

    // 외곽 벽 생성
    for (int i = 0; i < rows; i++) {
      grid[i][0].type = CellType.wall;
      grid[i][cols - 1].type = CellType.wall;
    }
    for (int j = 0; j < cols; j++) {
      grid[0][j].type = CellType.wall;
      grid[rows - 1][j].type = CellType.wall;
    }

    // 내부 장애물 벽 생성
    for (int i = 2; i < rows - 2; i += 2) {
      for (int j = 1; j < cols - 1; j++) {
        if (j != 3 && j != cols - 4) {
          grid[i][j].type = CellType.wall;
        }
      }
    }
  }

  // BFS(너비 우선 탐색) 기반 경로 찾기 알고리즘
  Stream<List<List<Cell>>> solveMaze() async* {
    Queue<Cell> queue = Queue<Cell>();
    Map<Cell, Cell> parentMap = {};
    Set<Cell> visited = {};

    queue.add(startCell);
    visited.add(startCell);

    List<List<int>> directions = [
      [-1, 0], // 상
      [1, 0],  // 하
      [0, -1], // 좌
      [0, 1],  // 우
    ];

    bool found = false;

    while (queue.isNotEmpty) {
      Cell current = queue.removeFirst();

      if (current == endCell) {
        found = true;
        break;
      }

      if (current != startCell && current != endCell) {
        current.type = CellType.searching;
        yield grid;
        await Future.delayed(const Duration(milliseconds: 50));
      }

      for (var dir in directions) {
        int newRow = current.row + dir[0];
        int newCol = current.col + dir[1];

        if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
          Cell neighbor = grid[newRow][newCol];

          if (neighbor.type != CellType.wall && !visited.contains(neighbor)) {
            queue.add(neighbor);
            visited.add(neighbor);
            parentMap[neighbor] = current;
          }
        }
      }

      if (current != startCell && current != endCell) {
        current.type = CellType.visited;
        yield grid;
      }
    }

    // 도착지점 도달 시 최단 경로 역추적
    if (found) {
      Cell? curr = parentMap[endCell];
      while (curr != null && curr != startCell) {
        curr.type = CellType.path;
        yield grid;
        await Future.delayed(const Duration(milliseconds: 30));
        curr = parentMap[curr];
      }
    }
  }

  void reset() {
    _initializeMaze();
  }
}

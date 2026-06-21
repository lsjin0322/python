import 'dart:collection';
import 'point.dart'; // 위에서 만든 point.dart 파일을 불러옴

/// 너비 우선 탐색(BFS) 기반 미로 탐색 함수
List<Point>? solveMazeBFS(List<List<int>> maze, Point start, Point end) {
  int rows = maze.length;
  int cols = maze[0].length;

  // BFS를 위한 선입선출(FIFO) 큐 및 방문 기록용 세트
  Queue<Point> queue = Queue<Point>();
  Map<Point, Point> parentMap = {};
  Set<Point> visited = {};

  // 시작점 설정
  queue.add(start);
  visited.add(start);

  // 상, 하, 좌, 우 4방향 이동 벡터
  List<Point> directions = [
    Point(-1, 0),
    Point(1, 0),
    Point(0, -1),
    Point(0, 1),
  ];

  while (queue.isNotEmpty) {
    Point current = queue.removeFirst();

    // 목적지(출구)에 도달한 경우 경로 복원 후 반환
    if (current == end) {
      List<Point> path = [];
      Point? curr = end;
      while (curr != null) {
        path.add(curr);
        curr = parentMap[curr];
      }
      return path.reversed.toList(); // 역순인 경로를 바르게 뒤집음
    }

    // 인접한 4방향 탐색
    for (var dir in directions) {
      int nx = current.x + dir.x;
      int ny = current.y + dir.y;
      Point next = Point(nx, ny);

      // 미로 맵 경계 내부에 있고, 벽(1)이 아닌 길(0)이며, 방문하지 않은 곳인 경우
      if (nx >= 0 && nx < rows && ny >= 0 && ny < cols) {
        if (maze[nx][ny] == 0 && !visited.contains(next)) {
          visited.add(next);
          parentMap[next] = current; // 이동 경로 역추적을 위해 부모 관계 기록
          queue.add(next);
        }
      }
    }
  }
  return null; // 탈출 경로가 없는 경우
}
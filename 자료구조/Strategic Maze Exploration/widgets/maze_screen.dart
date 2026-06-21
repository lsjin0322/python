import 'package:flutter/material.dart';
import '../models/cell.dart';
import '../services/maze_solver.dart';
import 'maze_painter.dart';

class MazeScreen extends StatefulWidget {
  const MazeScreen({Key? key}) : super(key: key);

  @override
  State<MazeScreen> createState() => _MazeScreenState();
}

class _MazeScreenState extends State<MazeScreen> {
  final int rows = 15;
  final int cols = 15;
  late MazeSolver solver;
  List<List<Cell>>? currentGrid;
  bool isRunning = false;

  @override
  void initState() {
    super.initState();
    solver = MazeSolver(rows: rows, cols: cols);
    currentGrid = solver.grid;
  }

  void _startExploring() {
    if (isRunning) return;
    setState(() {
      isRunning = true;
    });

    solver.solveMaze().listen(
      (updatedGrid) {
        setState(() {
          currentGrid = updatedGrid;
        });
      },
      onDone: () {
        setState(() {
          isRunning = false;
        });
      },
    );
  }

  void _resetMaze() {
    setState(() {
      solver.reset();
      currentGrid = solver.grid;
      isRunning = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Strategic Maze Exploration (BFS)'),
        backgroundColor: Colors.blueAccent,
      ),
      body: Column(
        children: [
          const Padding(
            padding: EdgeInsets.all(16.0),
            child: Text(
              '초록: 출발점 | 빨강: 도착점 | 노랑/파랑: 탐색 과정 | 주황: 최단 경로',
              style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold),
            ),
          ),
          Expanded(
            child: Center(
              child: AspectRatio(
                aspectRatio: 1,
                child: Container(
                  margin: const EdgeInsets.all(16.0),
                  decoration: BoxDecoration(
                    border: Border.all(color: Colors.black, width: 2),
                  ),
                  child: CustomPaint(
                    painter: MazePainter(
                      grid: currentGrid ?? solver.grid,
                      rows: rows,
                      cols: cols,
                    ),
                  ),
                ),
              ),
            ),
          ),
          Padding(
            padding: const EdgeInsets.only(bottom: 32.0),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton(
                  onPressed: isRunning ? null : _startExploring,
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.green),
                  child: const Text('탐색 시작'),
                ),
                ElevatedButton(
                  onPressed: isRunning ? null : _resetMaze,
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.redAccent),
                  child: const Text('초기화'),
                ),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
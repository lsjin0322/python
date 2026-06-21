import 'dart:async';
import 'package:flutter/material.dart';
import 'src/point.dart';           // 분리한 포인트 구조 가져오기
import 'src/maze_solver_bfs.dart'; // 분리한 BFS 알고리즘 가져오기

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'BFS Maze Simulator',
      theme: ThemeData.dark(), // 깔끔한 다크 모드 적용
      home: const MazeSimulator(),
    );
  }
}

class MazeSimulator extends StatefulWidget {
  const MazeSimulator({super.key});

  @override
  State<MazeSimulator> createState() => _MazeSimulatorState();
}

class _MazeSimulatorState extends State<MazeSimulator> {
  // 5x5 미로 데이터 (0: 갈 수 있는 길, 1: 벽)
  final List<List<int>> _maze = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0],
  ];

  final Point _start = Point(0, 0);
  final Point _end = Point(4, 4);

  Set<Point> _visited = {};
  List<Point> _finalPath = [];
  bool _isSearching = false;

  /// 버튼을 누르면 작동하는 화면 애니메이션용 BFS 시뮬레이션 함수
  Future<void> _runBFSSimulation() async {
    setState(() {
      _visited.clear();
      _finalPath.clear();
      _isSearching = true;
    });

    // 1단계와 2단계에서 만든 분리된 알고리즘을 호출하여 경로 계산
    var resultPath = solveMazeBFS(_maze, _start, _end);
    
    if (resultPath != null) {
      // 계산된 최단 경로 노드들을 화면에 하나씩 0.3초 간격으로 그리며 탐색 과정을 연출
      for (var node in resultPath) {
        await Future.delayed(const Duration(milliseconds: 300));
        if (!mounted) return;
        setState(() {
          _visited.add(node);
        });
      }
      setState(() {
        _finalPath = resultPath;
        _isSearching = false;
      });
    } else {
      setState(() {
        _isSearching = false;
      });
    }
  }

  /// 미로 칸의 상태에 따라 색상을 리턴하는 헬퍼 함수
  Color _getTileColor(int x, int y) {
    Point p = Point(x, y);
    if (p == _start) return Colors.green; // 시작점
    if (p == _end) return Colors.red;     // 목적지
    if (_finalPath.contains(p)) return Colors.amber; // 최종 완성된 최단 경로
    if (_visited.contains(p)) return Colors.blue.withOpacity(0.6); // 큐가 탐색한 영역
    if (_maze[x][y] == 1) return Colors.grey[800]!; // 벽
    return Colors.grey[300]!; // 아직 가보지 않은 길
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('BFS 미로 탐색 시뮬레이터'),
        centerTitle: true,
      ),
      body: Center(
        child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
              // 5x5 그리드를 화면에 그려주는 컴포넌트
              AspectRatio(
                aspectRatio: 1,
                child: GridView.builder(
                  gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
                    crossAxisCount: 5,
                    crossAxisSpacing: 4,
                    mainAxisSpacing: 4,
                  ),
                  itemCount: 25,
                  itemBuilder: (context, index) {
                    int x = index ~/ 5;
                    int y = index % 5;
                    return Container(
                      decoration: BoxDecoration(
                        color: _getTileColor(x, y),
                        borderRadius: BorderRadius.circular(4),
                      ),
                      child: Center(
                        child: Text(
                          '($x,$y)',
                          style: const TextStyle(color: Colors.black, fontWeight: FontWeight.bold),
                        ),
                      ),
                    );
                  },
                ),
              ),
              const SizedBox(height: 30),
              ElevatedButton.icon(
                onPressed: _isSearching ? null : _runBFSSimulation,
                icon: const Icon(Icons.play_arrow),
                label: const Text('탐색 시작'),
                style: ElevatedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(horizontal: 32, vertical: 16),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
import 'package:flutter/material.dart';
import '../models/cell.dart';

class MazePainter extends CustomPainter {
  final List<List<Cell>> grid;
  final int rows;
  final int cols;

  MazePainter({required this.grid, required this.rows, required this.cols});

  @override
  void paint(Canvas canvas, Size size) {
    double cellWidth = size.width / cols;
    double cellHeight = size.height / rows;

    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        Paint paint = Paint();
        
        switch (grid[r][c].type) {
          case CellType.empty:
            paint.color = Colors.white;
            break;
          case CellType.wall:
            paint.color = Colors.grey[800]!;
            break;
          case CellType.start:
            paint.color = Colors.green;
            break;
          case CellType.end:
            paint.color = Colors.red;
            break;
          case CellType.searching:
            paint.color = Colors.yellow;
            break;
          case CellType.visited:
            paint.color = Colors.blue[100]!;
            break;
          case CellType.path:
            paint.color = Colors.orange;
            break;
        }

        Rect rect = Rect.fromLTWH(
          c * cellWidth,
          r * cellHeight,
          cellWidth,
          cellHeight,
        );
        
        canvas.drawRect(rect, paint);

        Paint borderPaint = Paint()
          ..color = Colors.grey[300]!
          ..style = PaintingStyle.stroke
          ..strokeWidth = 0.5;
        canvas.drawRect(rect, borderPaint);
      }
    }
  }

  @override
  bool shouldRepaint(covariant CustomPainter oldDelegate) => true;
}
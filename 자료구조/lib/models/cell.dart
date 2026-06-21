enum CellType { empty, wall, start, end, searching, visited, path }

class Cell {
  final int row;
  final int col;
  CellType type;

  Cell({
    required this.row,
    required this.col,
    this.type = CellType.empty,
  });
}
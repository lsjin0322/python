class Point {
  final int x;
  final int y;
  Point(this.x, this.y);

  @override
  bool operator ==(Object other) => other is Point && x == other.x && y == other.y;

  @override
  int get hashCode => Object.hash(x, y);
}
/// 선형 덱 (Linear Deque)
class LinearDeque<T> {
  final List<T?> _storage;
  int _front;
  int _rear;
  final int capacity;

  LinearDeque(this.capacity)
      : _storage = List<T?>.filled(capacity * 2, null),
        _front = capacity,
        _rear = capacity;

  bool get isEmpty => _front == _rear;
  bool get isFull => _front == 0 || _rear == _storage.length - 1;

  // 앞쪽에 데이터 삽입
  void addFirst(T item) {
    if (_front == 0) throw StateError("Linear Deque 앞쪽 공간이 가득 찼습니다.");
    _storage[--_front] = item;
  }

  // 뒤쪽에 데이터 삽입
  void addLast(T item) {
    if (_rear == _storage.length - 1) throw StateError("Linear Deque 뒤쪽 공간이 가득 찼습니다.");
    _storage[_rear++] = item;
  }

  // 앞쪽에서 데이터 제거 후 반환
  T removeFirst() {
    if (isEmpty) throw StateError("Deque가 비어있습니다.");
    return _storage[_front++]!;
  }

  // 뒤쪽에서 데이터 제거 후 반환
  T removeLast() {
    if (isEmpty) throw StateError("Deque가 비어있습니다.");
    return _storage[--_rear]!;
  }
}
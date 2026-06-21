/// 원형 덱 (Circular Deque)
class CircularDeque<T> {
  final List<T?> _storage;
  int _front = 0;
  int _rear = 0;
  final int capacity;

  CircularDeque(this.capacity) : _storage = List<T?>.filled(capacity, null);

  bool get isFull => (_rear + 1) % capacity == _front;
  bool get isEmpty => _front == _rear;

  // 앞쪽에 데이터 삽입 (역방향 회전)
  void addFirst(T item) {
    if (isFull) throw StateError("Circular Deque가 가득 찼습니다.");
    _storage[_front] = item;
    _front = (_front - 1 + capacity) % capacity;
  }

  // 뒤쪽에 데이터 삽입 (정방향 회전)
  void addLast(T item) {
    if (isFull) throw StateError("Circular Deque가 가득 찼습니다.");
    _rear = (_rear + 1) % capacity;
    _storage[_rear] = item;
  }

  // 앞쪽에서 데이터 제거 후 반환
  T removeFirst() {
    if (isEmpty) throw StateError("Deque가 비어있습니다.");
    _front = (_front + 1) % capacity;
    return _storage[_front]!;
  }

  // 뒤쪽에서 데이터 제거 후 반환
  T removeLast() {
    if (isEmpty) throw StateError("Deque가 비어있습니다.");
    T item = _storage[_rear]!;
    _rear = (_rear - 1 + capacity) % capacity;
    return item;
  }
}
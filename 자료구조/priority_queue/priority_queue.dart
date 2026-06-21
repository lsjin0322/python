/// 우선순위 큐에 담길 데이터와 가중치(우선순위)를 정의하는 클래스
class PriorityItem<T> {
  final T data;
  final int priority; // 숫자가 작을수록 우선순위가 높음 (Min-Heap 방식)

  PriorityItem(this.data, this.priority);
}

/// 독립형 우선순위 큐 (Priority Queue) 클래스
class CustomPriorityQueue<T> {
  final List<PriorityItem<T>> _storage = [];

  bool get isEmpty => _storage.isEmpty;
  int get length => _storage.length;

  // 데이터 삽입 (Enqueue)
  void enqueue(T data, int priority) {
    _storage.add(PriorityItem(data, priority));
    // 가중치(priority) 기준 오름차순 정렬
    _storage.sort((a, b) => a.priority.compareTo(b.priority));
  }

  // 데이터 추출 (Dequeue)
  T dequeue() {
    if (isEmpty) {
      throw StateError("우선순위 큐가 비어있습니다.");
    }
    return _storage.removeAt(0).data;
  }

  // 맨 앞 데이터 확인 (Peek)
  T peek() {
    if (isEmpty) {
      throw StateError("우선순위 큐가 비어있습니다.");
    }
    return _storage.first.data;
  }
}
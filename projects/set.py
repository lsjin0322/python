# 집합(set) ADT 클래스 구현

class ArraySet:
    # 초기화 (리스트를 저장 구조로 사용)
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0

    # Contain(e): 집합이 원소 e를 포함하는지 검사한다.
    def contains(self, e):
        for i in range(self.size):
            if self.array[i] == e:
                return True
        return False

    # Insert(e): 새로운 원소 e를 삽입한다. (중복 삽입은 허용안함)
    def insert(self, e):    # 중복 검사 후, 중복이 아니고 가득 차지 않았을 때만 삽입
        if not self.contains(e) and not self.isFull():
            self.array[self.size] = e
            self.size += 1
        else:
            print("상태: 삽입 불가 (중복 원소이거나 포화 상태)")

    # Delete(e): 원소 e를 집합에서 꺼내고(삭제) 반환한다.
    def delete(self, e):
        for i in range(self.size):
            if self.array[i] == e:     # 삭제할 위치의 원소를 마지막 원소로 대체 (순서가 상관없으므로 빠름)
                self.array[i] = self.array[self.size - 1]
                self.size -= 1
                return e
        return None

    # IsFull(): 집합이 가득 차 있는지를 검사한다.
    def isFull(self):
        return self.size == self.capacity

    # isEmpty(): 공집합인지 검사한다.
    def isEmpty(self):
        return self.size == 0

    # Union(setB): setB와 합집합을 만들어 반환한다. (A ∪ B)
    def union(self, setB):
        new_set = ArraySet(self.capacity + setB.capacity)
        # 현재 집합(A)의 모든 원소 추가
        for i in range(self.size):
            new_set.insert(self.array[i])
        # 상대 집합(B)의 원소 중 중복되지 않는 것만 추가
        for i in range(setB.size):
            new_set.insert(setB.array[i])
        return new_set

    # intersect(setB): setB와 교집합을 만들어 반환한다. (A ∩ B)
    def intersect(self, setB):
        new_set = ArraySet(min(self.capacity, setB.capacity))
        for i in range(self.size):
            if setB.contains(self.array[i]):
                new_set.insert(self.array[i])
        return new_set

    # Difference(setB): setB와 차집합을 만들어 반환한다. (A - B)
    def difference(self, setB):
        new_set = ArraySet(self.capacity)
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                new_set.insert(self.array[i])
        return new_set

    # Equals(setB): setB와 같은 집합인지를 검사한다.
    def equals(self, setB):
        if self.size != setB.size:
            return False
        for i in range(self.size):
            if not setB.contains(self.array[i]):
                return False
        return True

    # Size(): 집합의 원소의 개수를 반환한다.
    def Size(self):
        return self.size

    # Display(): 리스트를 화면에 출력한다.
    def display(self, msg='Set: '):
        print(msg, self.array[:self.size])





#=====================
# 집합(set) ADT 테스트 예제

if __name__ == "__main__":
    print("=" * 40)
    print("  집합(Set) ADT 테스트")
    print("=" * 40)

    # 집합 A 생성 및 삽입
    A = ArraySet(10)
    A.insert(1)
    A.insert(2)
    A.insert(3)
    A.insert(4)
    A.insert(5)
    A.display("집합 A: ")

    # 집합 B 생성 및 삽입
    B = ArraySet(10)
    B.insert(3)
    B.insert(4)
    B.insert(5)
    B.insert(6)
    B.insert(7)
    B.display("집합 B: ")

    print("-" * 40)

    # contains() 테스트
    print(f"A.contains(3): {A.contains(3)}")   # True
    print(f"A.contains(9): {A.contains(9)}")   # False

    print("-" * 40)

    # 중복 삽입 테스트
    print("A에 3 중복 삽입 시도:")
    A.insert(3)  # 삽입 불가 메시지 출력

    print("-" * 40)

    # 합집합 A ∪ B
    C = A.union(B)
    C.display("A ∪ B: ")

    # 교집합 A ∩ B
    D = A.intersect(B)
    D.display("A ∩ B: ")

    # 차집합 A - B
    E = A.difference(B)
    E.display("A - B: ")

    print("-" * 40)

    # equals() 테스트
    A2 = ArraySet(10)
    A2.insert(1)
    A2.insert(2)
    A2.insert(3)
    A2.insert(4)
    A2.insert(5)
    print(f"A == A2: {A.equals(A2)}")  # True
    print(f"A == B:  {A.equals(B)}")   # False

    print("-" * 40)

    # delete() 테스트
    A.delete(3)
    A.display("A에서 3 삭제 후: ")
    print(f"A.Size(): {A.Size()}")

    print("-" * 40)

    # isEmpty() / isFull() 테스트
    print(f"A.isEmpty(): {A.isEmpty()}")   # False
    print(f"A.isFull(): {A.isFull()}")     # False

    empty_set = ArraySet(5)
    print(f"빈 집합 isEmpty(): {empty_set.isEmpty()}")  # True

    print("=" * 40)
    print("  테스트 완료")
    print("=" * 40)
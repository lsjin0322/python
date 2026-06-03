#스택구조
stack = []

stack.append(10)
stack.append(20)

print(stack.pop())

# 스택(Stack) ADT 클래스 구현

class ArrayStack:
    # 초기화 (capacity 설정)
    def __init__(self, capacity=10):
        self.capacity = capacity      # 스택의 최대 용량
        self.array = [None] * capacity # 데이터를 저장할 배열
        self.top = -1                 # 가장 위에 있는 데이터의 인덱스 (비어있을 때 -1)

    # Push(e): 요소 e를 스택의 맨 위에 추가한다.
    def push(self, e):
        if not self.isFull():
            self.top += 1
            self.array[self.top] = e
        else:
            print("상태: 스택 포화(Stack Overflow)")

    # Pop(): 스택의 맨 위에 있는 요소를 꺼내 반환한다.
    def pop(self):
        if not self.isEmpty():
            item = self.array[self.top]
            self.top -= 1
            return item
        else:
            print("상태: 스택 공백(Stack Underflow)")
            return None

    # IsFull(): 스택이 가득 차 있는지를 검사한다(True, False).
    def isFull(self):
        return self.top == self.capacity - 1

    # isEmpty(): 스택이 비어있는지 검사한다(True, False).
    def isEmpty(self):
        return self.top == -1

    # Peek(): 스택의 맨 위에 있는 항목을 삭제하지 않고 반환한다.
    def peek(self):
        if not self.isEmpty():
            return self.array[self.top]
        else:
            return None

    # Size(): 스택 내의 모든 항목들의 개수를 반환한다.
    def size(self):
        return self.top + 1

    # Clear(): 스택을 공백 상태로 만든다.
    def clear(self):
        self.top = -1

#=========

# 스택 응용: 괄호 검사 알고리즘

def check_brackets(statement):
    stack = ArrayStack(100) # 검사를 위한 스택 생성

    for char in statement:
        # 여는 괄호 {, [, ( 를 만나면 push
        if char in ('{', '[', '('):
            stack.push(char)

        # 닫는 괄호 }, ], ) 를 만나면
        elif char in ('}', ']', ')'):
            # 스택이 비어있으면 조건 위반 (오류)
            if stack.isEmpty():
                return False

            # 스택에서 하나를 pop하여 짝이 맞는지 확인
            left = stack.pop()
            if (char == '}' and left != '{') or \
               (char == ']' and left != '[') or \
               (char == ')' and left != '('):
                return False 


    return stack.isEmpty()



#==================================
# ── 스택 클래스 사용 예제 ──────────────────────────────

if __name__ == "__main__":

    print("=" * 40)
    print("  ArrayStack 기능 테스트")
    print("=" * 40)

    s = ArrayStack(5)

    # push 테스트
    s.push(10)
    s.push(20)
    s.push(30)
    print(f"push 10, 20, 30 후 size: {s.size()}")   # 3
    print(f"peek (맨 위 확인):       {s.peek()}")    # 30
    print(f"isFull:                  {s.isFull()}")  # False
    print(f"isEmpty:                 {s.isEmpty()}") # False

    print("-" * 40)

    # pop 테스트
    print(f"pop: {s.pop()}")  # 30
    print(f"pop: {s.pop()}")  # 20
    print(f"pop: {s.pop()}")  # 10
    print(f"pop (빈 스택):")
    s.pop()                   # Stack Underflow

    print("-" * 40)

    # overflow 테스트
    print("용량(5) 초과 push 시도:")
    for i in range(6):
        s.push(i * 10)        # 5개 push 후 overflow

    print("-" * 40)

    # clear 테스트
    s.clear()
    print(f"clear 후 isEmpty: {s.isEmpty()}")  # True
    print(f"clear 후 size:    {s.size()}")      # 0

    print("=" * 40)
    print("  괄호 검사 테스트")
    print("=" * 40)

    tests = [
        "{ A [ B + C ] }",
        "( a + b ) * ( c - d )",
        "{ ( a + b }",
        "[ [ [ ] ]",
        "( )",
    ]

    for t in tests:
        result = check_brackets(t)
        print(f"{'올바름 ✓' if result else '오류   ✗'}  |  {t}")

    print("=" * 40)
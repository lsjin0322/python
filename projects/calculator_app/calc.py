from stack import ArrayStack

# 연산자 우선순위
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    return 0

# 중위 표기식 → 후위 표기식 변환
def infix_to_postfix(expr):
    stack = ArrayStack(100)
    output = []

    tokens = expr.split()  # 공백 기준으로 토큰 분리

    for token in tokens:
        if token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.isEmpty() and stack.peek() != '(':
                output.append(stack.pop())
            stack.pop()  # '(' 제거
        elif token in ('+', '-', '*', '/'):
            while (not stack.isEmpty() and
                   stack.peek() != '(' and
                   precedence(stack.peek()) >= precedence(token)):
                output.append(stack.pop())
            stack.push(token)
        else:
            output.append(token)  # 숫자는 바로 출력

    while not stack.isEmpty():
        output.append(stack.pop())

    return ' '.join(output)

# 후위 표기식 계산
def eval_postfix(postfix):
    stack = ArrayStack(100)
    tokens = postfix.split()

    for token in tokens:
        if token in ('+', '-', '*', '/'):
            b = float(stack.pop())
            a = float(stack.pop())
            if token == '+': stack.push(a + b)
            elif token == '-': stack.push(a - b)
            elif token == '*': stack.push(a * b)
            elif token == '/':
                if b == 0:
                    raise ZeroDivisionError("0으로 나눌 수 없습니다")
                stack.push(a / b)
        else:
            stack.push(float(token))

    return stack.pop()

# 수식 계산 메인 함수
def calculate(expr):
    try:
        # 입력값 공백 정리: "3+(2*4)" → "3 + ( 2 * 4 )"
        result_expr = ''
        for ch in expr:
            if ch in '+-*/()':
                result_expr += f' {ch} '
            else:
                result_expr += ch
        result_expr = ' '.join(result_expr.split())

        postfix = infix_to_postfix(result_expr)
        result = eval_postfix(postfix)

        # 정수면 정수로 출력
        if result == int(result):
            return str(int(result))
        return str(round(result, 6))
    except ZeroDivisionError as e:
        return f"오류: {e}"
    except Exception:
        return "오류: 잘못된 수식"
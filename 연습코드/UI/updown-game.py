import flet as ft
import random

def main(page: ft.Page):
    page.title = "업다운 게임"

    answer = random.randint(1, 100)
    attempts = 0

    result_text = ft.Text("1부터 100 사이 숫자를 맞춰보세요!")
    attempt_text = ft.Text("시도 횟수: 0")

    user_input = ft.TextField(label="숫자 입력", width=200)

    def check_number(e):
        nonlocal answer, attempts

        if user_input.value == "":
            result_text.value = "숫자를 입력하세요!"
        else:
            try:
                user_number = int(user_input.value)
                attempts += 1
                attempt_text.value = f"시도 횟수: {attempts}"

                if user_number < answer:
                    result_text.value = "업!"
                elif user_number > answer:
                    result_text.value = "다운!"
                else:
                    result_text.value = "정답입니다! 🎉"
            except:
                result_text.value = "숫자만 입력하세요!"

        page.update()

    def reset_game(e):
        nonlocal answer, attempts
        answer = random.randint(1, 100)
        attempts = 0
        result_text.value = "새 게임 시작!"
        attempt_text.value = "시도 횟수: 0"
        user_input.value = ""
        page.update()

    submit_btn = ft.ElevatedButton("확인", on_click=check_number)
    reset_btn = ft.ElevatedButton("다시 시작", on_click=reset_game)

    page.add(
        result_text,
        attempt_text,
        user_input,
        submit_btn,
        reset_btn
    )

ft.app(target=main)

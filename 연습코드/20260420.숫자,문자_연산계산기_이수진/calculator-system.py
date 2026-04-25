"""
[계산기 클래스]
- 숫자와 문자를 구분하여 각각 리스트에 저장
- 숫자 리스트를 이용해 사칙연산 및 평균, 최댓값, 최솟값 계산

[입력 처리]
- 값을 입력 후 Enter를 누르면 실행
- 숫자는 numbers 리스트, 문자는 strings 리스트에 저장

[화면 출력]
- 저장된 숫자와 문자를 각각 구분하여 화면에 표시

[계산 기능]
- 버튼 클릭 시 선택한 연산 수행
- 결과를 화면에 출력

[UI 구성]
- 입력창, 숫자/문자 표시 영역, 계산 버튼, 결과 출력 영역으로 구성

[사용자 편의 기능]
- 입력 후에도 커서가 유지되어 계속 입력 가능
- Enter 키로 빠르게 데이터 입력 가능

[프로그램 실행]
- Flet을 이용하여 계산기 앱 실행
"""

import flet as ft


class SmartCalculator:
    def __init__(self):
        self.numbers = []
        self.strings = []

    
    def add_value(self, value):
        try:
            num = float(value)
            self.numbers.append(num)
        except:
            self.strings.append(value)

    def add(self):
        return sum(self.numbers)

    def sub(self):
        if not self.numbers:
            return 0
        result = self.numbers[0]
        for n in self.numbers[1:]:
            result -= n
        return result

    def mul(self):
        result = 1
        for n in self.numbers:
            result *= n
        return result

    def div(self):
        if not self.numbers:
            return 0
        result = self.numbers[0]
        for n in self.numbers[1:]:
            if n == 0:
                return "0으로 나눌 수 없음"
            result /= n
        return result

    def avg(self):
        if not self.numbers:
            return 0
        return sum(self.numbers) / len(self.numbers)

    def max(self):
        if not self.numbers:
            return None
        return max(self.numbers)

    def min(self):
        if not self.numbers:
            return None
        return min(self.numbers)


def main(page: ft.Page):
    page.title = "Smart Input Calculator"
    page.bgcolor = "#F4F6F8"
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    calc = SmartCalculator()

 
    input_field = ft.TextField(
        label="값 입력 후 Enter",
        autofocus=True,
        border_radius=12,
        bgcolor="white"
    )

    number_view = ft.Column(spacing=5)
    string_view = ft.Column(spacing=5)
    result_text = ft.Text(size=18, weight="bold", color="#2F6F3E")

   
    def update_view():
        number_view.controls.clear()
        string_view.controls.clear()

        for n in calc.numbers:
            number_view.controls.append(
                ft.Container(
                    content=ft.Text(str(n)),
                    padding=8,
                    bgcolor="#E8F5E9",
                    border_radius=8
                )
            )

        for s in calc.strings:
            string_view.controls.append(
                ft.Container(
                    content=ft.Text(str(s)),
                    padding=8,
                    bgcolor="#FFF3E0",
                    border_radius=8
                )
            )

        page.update()

   
    def on_submit(e):
        value = input_field.value.strip()
        if value == "":
            return

        calc.add_value(value)
        input_field.value = ""
        input_field.focus()   # ⭐ 커서 유지 핵심
        update_view()

    input_field.on_submit = on_submit

    
    def run_calc(func):
        if not calc.numbers:
            result_text.value = "숫자가 없습니다"
        else:
            result = getattr(calc, func)()
            result_text.value = f"{func} 결과: {result}"
        input_field.focus()
        page.update()

    def calc_button(text, func, color):
        return ft.ElevatedButton(
            text,
            on_click=lambda e: run_calc(func),
            style=ft.ButtonStyle(
                bgcolor=color,
                color="white",
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=10
            ),
            expand=True
        )

    page.add(
        ft.Container(
            width=600,
            padding=20,
            bgcolor="white",
            border_radius=20,
            shadow=ft.BoxShadow(blur_radius=20, color="#00000015"),
            content=ft.Column([

                ft.Text("🧮 Smart Calculator", size=26, weight="bold", color="#2F6F3E"),

                input_field,

                ft.Row([
                    ft.Container(
                        expand=1,
                        content=ft.Column([
                            ft.Text("🔢 숫자", weight="bold"),
                            number_view
                        ])
                    ),
                    ft.Container(
                        expand=1,
                        content=ft.Column([
                            ft.Text("🔤 문자", weight="bold"),
                            string_view
                        ])
                    ),
                ]),

                ft.Divider(),

                ft.Row([
                    calc_button("더하기", "add", "#4CAF50"),
                    calc_button("빼기", "sub", "#66BB6A"),
                    calc_button("곱하기", "mul", "#81C784"),
                    calc_button("나누기", "div", "#A5D6A7"),
                ]),

                ft.Row([
                    calc_button("평균", "avg", "#388E3C"),
                    calc_button("최댓값", "max", "#2E7D32"),
                    calc_button("최솟값", "min", "#1B5E20"),
                ]),

                ft.Divider(),

                result_text

            ], spacing=15)
        )
    )


ft.app(target=main)
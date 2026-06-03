# 수식계산기 앱
import flet as ft
from calc import calculate

def main(page: ft.Page):
    page.title = "수식 계산기"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.bgcolor = "#E8E0D5"   
    page.padding = 30
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    display = ft.Text(
        value="0",
        size=38,
        color="#3D3530",        
        text_align=ft.TextAlign.RIGHT,
        expand=True,
        weight=ft.FontWeight.W_300,
    )

    expr_display = ft.Text(
        value="",
        size=13,
        color="#9E8E82",       
        text_align=ft.TextAlign.RIGHT,
        expand=True,
    )

    current_expr = {"value": ""}

    def btn_click(val):
        if val == "C":
            current_expr["value"] = ""
            display.value = "0"
            expr_display.value = ""
        elif val == "⌫":
            current_expr["value"] = current_expr["value"][:-1]
            display.value = current_expr["value"] if current_expr["value"] else "0"
        elif val == "=":
            if current_expr["value"]:
                expr_display.value = current_expr["value"] + " ="
                result = calculate(current_expr["value"])
                display.value = result
                current_expr["value"] = result if "오류" not in result else ""
        else:
            current_expr["value"] += val
            display.value = current_expr["value"]
        page.update()

    def make_btn(label, col="#3D3530", bg="#F0EAE2", expand=1, size=18):
        return ft.Container(
            content=ft.TextButton(
                content=ft.Text(label, size=size, weight=ft.FontWeight.W_500, color=col),
                on_click=lambda e, v=label: btn_click(v),
                style=ft.ButtonStyle(
                    bgcolor=bg,
                    shape=ft.CircleBorder(),
                    overlay_color="#00000011",
                ),
            ),
            expand=expand,
            height=60,
            width=60,
            border_radius=30,
            bgcolor=bg,
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=5,
                color="#22000000",
                offset=ft.Offset(2, 3),
            ),
        )

    buttons = ft.Column(
        controls=[
            ft.Row(controls=[
                # 1 포인트: 테라코타
                make_btn("C",  col="#C0604A", bg="#F2D5CC"),
                # 2 서브: 세이지 그린
                make_btn("(",  col="#5A7A62", bg="#D4E4D6"),
                make_btn(")",  col="#5A7A62", bg="#D4E4D6"),
                make_btn("⌫",  col="#C0604A", bg="#F2D5CC"),
            ], spacing=12, alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[
                make_btn("7"), make_btn("8"), make_btn("9"),
                make_btn("/", col="#5A7A62", bg="#D4E4D6"),
            ], spacing=12, alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[
                make_btn("4"), make_btn("5"), make_btn("6"),
                make_btn("*", col="#5A7A62", bg="#D4E4D6"),
            ], spacing=12, alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[
                make_btn("1"), make_btn("2"), make_btn("3"),
                make_btn("-", col="#5A7A62", bg="#D4E4D6"),
            ], spacing=12, alignment=ft.MainAxisAlignment.CENTER),
            ft.Row(controls=[
                make_btn("0"), make_btn("."),
                make_btn("+", col="#5A7A62", bg="#D4E4D6"),
                make_btn("=", col="#FFFFFF",  bg="#C0604A", size=20),
            ], spacing=12, alignment=ft.MainAxisAlignment.CENTER),
        ],
        spacing=12,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
    )

    # 태양광 패널 장식
    solar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Container(bgcolor="#9E8E8288", width=30, height=10, border_radius=2),
                ft.Container(bgcolor="#9E8E8288", width=30, height=10, border_radius=2),
                ft.Container(bgcolor="#9E8E8288", width=30, height=10, border_radius=2),
                ft.Container(bgcolor="#C0604A88", width=14, height=10, border_radius=6),
            ],
            spacing=4,
        ),
        margin=ft.Margin(bottom=8, top=0, left=0, right=0),
    )

    page.add(
        ft.Container(
            content=ft.Column(
                controls=[
                    solar,
                    ft.Container(
                        content=ft.Column(
                            controls=[expr_display, display],
                            spacing=2,
                            horizontal_alignment=ft.CrossAxisAlignment.END,
                        ),
                        bgcolor="#EDE6DC",
                        border_radius=8,
                        padding=ft.Padding(left=14, top=10, right=14, bottom=10),
                        margin=ft.Margin(bottom=16, top=0, left=0, right=0),
                        border=ft.border.all(1, "#D4C8BC"),
                        shadow=ft.BoxShadow(
                            blur_radius=4,
                            color="#22000000",
                            offset=ft.Offset(1, 2),
                        ),
                    ),
                    buttons,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=6,
            ),
            bgcolor="#F0EAE288",
            border_radius=24,
            padding=20,
            border=ft.border.all(1.5, "#FFFFFF99"),
            shadow=ft.BoxShadow(
                spread_radius=0,
                blur_radius=20,
                color="#22000000",
                offset=ft.Offset(4, 6),
            ),
            width=320,
        ),
    )

if __name__ == "__main__":
    ft.app(main, view=ft.AppView.WEB_BROWSER)
"""
[벚꽃 가위바위보 게임]
- GUI 기반 가위바위보 게임
- 사용자 vs 컴퓨터 대결
- 먼저 3승을 달성하면 게임 종료
- 다시 시작 기능 포함
"""

import flet as ft
import random

def main(page: ft.Page):
    # 기본 창 설정 
    page.title = "🌸 벚꽃 가위바위보 🌸"
    page.theme = ft.Theme(font_family="Malgun Gothic")
    page.bgcolor = "#FFF0F5"  # 배경색 설정
    
    # 창 사이즈 설정 
    page.window.width = 350
    page.window.height = 450
    page.window.resizable = False  # 창 크기 고정

    # 페이지 중앙 정렬
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    # 제목 텍스트
    title = ft.Text(
        "🌸 벚꽃 가위바위보 🌸",
        size=26,
        weight="bold",
        color="#FF69B4"
    )

    # 승리 횟수 저장
    win_count = {'user': 0, 'pc': 0}

    # UI 텍스트 요소
    user_choice_text = ft.Text("당신의 선택: ")
    pc_choice_text = ft.Text("컴퓨터 선택: ")
    result_text = ft.Text("가위, 바위, 보 중 하나를 선택하세요!")
    score_text = ft.Text(
        f"승리 횟수 - 당신: {win_count['user']}, 컴퓨터: {win_count['pc']}",
        weight="bold",
        color="#D02090"
    )

    # 승패 판정 로직 (딕셔너리 기반)
    judge_rsp = {
        '가위': {'가위': None, '바위': 'pc', '보': 'user'},
        '바위': {'가위': 'user', '바위': None, '보': 'pc'},
        '보': {'가위': 'pc', '바위': 'user', '보': None}
    }

    # 선택지 리스트
    choices = ['가위', '바위', '보']

    # --- [게임 실행 함수] ---
    def play_rps(e):
        nonlocal win_count

        # 사용자 / 컴퓨터 선택
        user_rsp = e.control.data
        pc_rsp = random.choice(choices)

        # UI 업데이트
        user_choice_text.value = f"당신의 선택: {user_rsp}"
        pc_choice_text.value = f"컴퓨터 선택: {pc_rsp}"

        # 승부 판정
        winner = judge_rsp[user_rsp][pc_rsp]

        if winner == 'user':
            win_count['user'] += 1
            result_text.value = "당신이 이겼어요! 🎉"
        elif winner == 'pc':
            win_count['pc'] += 1
            result_text.value = "컴퓨터가 이겼어요 😢"
        else:
            result_text.value = "무승부입니다."

        # 점수 표시 업데이트
        score_text.value = f"승리 횟수 - 당신: {win_count['user']}, 컴퓨터: {win_count['pc']}"

        # 게임 종료 조건 (3승)
        if win_count['user'] >= 3:
            result_text.value = "당신이 최종 승리했습니다! 🎊"
            disable_buttons()
        elif win_count['pc'] >= 3:
            result_text.value = "컴퓨터가 최종 승리했습니다.\n다시 도전하시겠습니까?"
            disable_buttons()

        page.update()

    # --- [버튼 비활성화] ---
    def disable_buttons():
        for btn in rps_buttons:
            btn.disabled = True

    # --- [게임 초기화] ---
    def reset_game(e):
        nonlocal win_count
        win_count = {'user': 0, 'pc': 0}

        result_text.value = "가위, 바위, 보 중 하나를 선택하세요!"
        score_text.value = f"승리 횟수 - 당신: {win_count['user']}, 컴퓨터: {win_count['pc']}"
        user_choice_text.value = "당신의 선택: "
        pc_choice_text.value = "컴퓨터 선택: "

        # 버튼 다시 활성화
        for btn in rps_buttons:
            btn.disabled = False

        page.update()

    # 가위바위보 버튼 생성
    rps_buttons = [
        ft.ElevatedButton(choice, on_click=play_rps, data=choice)
        for choice in choices
    ]

    # 다시 시작 버튼
    reset_btn = ft.ElevatedButton("다시 시작🔄", on_click=reset_game)

    # UI 구성
    page.add(
        title,
        user_choice_text,
        pc_choice_text,
        result_text,
        score_text,
        ft.Row(rps_buttons, spacing=10, alignment=ft.MainAxisAlignment.CENTER),
        reset_btn
    )

ft.app(target=main)

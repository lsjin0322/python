import flet as ft
import random

def main(page: ft.Page):
    # 기본 창 설정 
    page.title = "🌸 벚꽃 가위바위보 🌸"
    page.theme = ft.Theme(font_family="Malgun Gothic")
    page.bgcolor = "#FFF0F5"  # 연분홍 배경
    
    # 창 사이즈 설정 
    page.window.width = 350
    page.window.height = 450
    page.window.resizable = False # 창 크기를 고정

    # 페이지 전체 요소를 정중앙으로 배치
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    title = ft.Text(
        "🌸 벚꽃 가위바위보 🌸",
        size=26,
        weight="bold",
        color="#FF69B4"
    )

    # 승리 횟수 초기화
    win_count = {'user': 0, 'pc': 0}

  
    user_choice_text = ft.Text("당신의 선택: ")
    pc_choice_text = ft.Text("컴퓨터 선택: ")
    result_text = ft.Text("가위, 바위, 보 중 하나를 선택하세요!")
    score_text = ft.Text(f"승리 횟수 - 당신: {win_count['user']}, 컴퓨터: {win_count['pc']}", weight="bold", color="#D02090")


    judge_rsp = {
        '가위': {'가위': None, '바위': 'pc', '보': 'user'},
        '바위': {'가위': 'user', '바위': None, '보': 'pc'},
        '보': {'가위': 'pc', '바위': 'user', '보': None}
    }
    #가위바위보 버튼
    choices = ['가위', '바위', '보']

    # 승부 결정 함수
    def play_rps(e):
        nonlocal win_count

        user_rsp = e.control.data  # 버튼에 저장된 사용자 선택
        pc_rsp = random.choice(choices)

        user_choice_text.value = f"당신의 선택: {user_rsp}"
        pc_choice_text.value = f"컴퓨터 선택: {pc_rsp}"

        winner = judge_rsp[user_rsp][pc_rsp]
        if winner == 'user':
            win_count['user'] += 1
            result_text.value = "당신이 이겼어요! 🎉"
        elif winner == 'pc':
            win_count['pc'] += 1
            result_text.value = "컴퓨터가 이겼어요 😢"
        else:
            result_text.value = "무승부입니다."

        score_text.value = f"승리 횟수 - 당신: {win_count['user']}, 컴퓨터: {win_count['pc']}"

      
        if win_count['user'] >= 3:
            result_text.value = "당신이 최종 승리했습니다! 🎊"
            disable_buttons()
        elif win_count['pc'] >= 3:
            result_text.value = "컴퓨터가 최종 승리했습니다. \n다시 도전하시겠습니까?"
            disable_buttons()

        page.update()

    # 버튼 비활성화
    def disable_buttons():
        for btn in rps_buttons:
            btn.disabled = True

    # 게임 초기화
    def reset_game(e):
        nonlocal win_count
        win_count = {'user': 0, 'pc': 0}
        result_text.value = "가위, 바위, 보 중 하나를 선택하세요!"
        score_text.value = f"승리 횟수 - 당신: {win_count['user']}, 컴퓨터: {win_count['pc']}"
        user_choice_text.value = "당신의 선택: "
        pc_choice_text.value = "컴퓨터 선택: "
        for btn in rps_buttons:
            btn.disabled = False
        page.update()

    # 가위바위보 버튼 생성
    rps_buttons = [
        ft.ElevatedButton(choice, on_click=play_rps, data=choice)
        for choice in choices
    ]
#다시시작 버튼
    reset_btn = ft.ElevatedButton("다시 시작🔄", on_click=reset_game)

  
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
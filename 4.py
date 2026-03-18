import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Button 연습")
root.geometry("500x400")
root.configure(bg="white")

#클릭 횟수를 저장할 변수
click_count = 0
status_var = tk.StringVar()
status_var.set("버튼을 클릭해보세요!")

#상태 표시 라벨
status_label = tk.Label(root, textvariable=status_var, font=("맑은 고딕", 14))
status_label.pack(pady=20)

# 기본 버튼
def basic_click():
    global click_count
    click_count += 1
    status_var.set(f"기본 버튼이 {click_count}번 클릭되었습니다!")

basic_button = tk.Button(
    root,
    text="기본 버튼",
    command=basic_click,
    font=("맑은 고딕", 12),
    width=15
)
basic_button.pack(pady=5)

# 스타일이 적용된 버튼들
style_frame = tk.Frame(root, bg="white")
style_frame.pack(pady=10)

tk.Button(style_frame, text="빨간 버튼", bg="red", fg="white", 
          font=("맑은 고딕", 10, "bold"),
          command=lambda: status_var.set("빨간 버튼 클릭!")).pake(side=tk.LEFT, padx=5)

tk.Button(style_frame, text="파란 버튼", bg="blue", fg="white",font=("맑은 고딕", 10, "bold"),
          command=lambda: status_var.set("파란 버튼 클릭!")).pack(side=tk.LEFT, padx=5 )

tk.Button(style_frame, text="초록 버튼", bg="green", fg="white", 
          font=("맑은 고딕", 10, "bold"),
          command=lambda: status_var.set("초록 버튼 클릭!")).pack(side=tk.LEFT, padx=5)

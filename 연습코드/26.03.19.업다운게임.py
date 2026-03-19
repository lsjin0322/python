import tkinter as tk

root = tk.Tk()

root.title("랜덤 숫자를 맞춰보세요!")
root.geometry("400x500")

tk.Label(root, text="숫자를 입력하세요:", font=("맑은 고딕", 12)).pack(pady=10)
name_entry = tk.Entry(root, font=("맑은 고딕", 12), width=30)
name_entry.pack(pady=5)

def show_input():
     user_input =name_entry.get() 
     result_label.config(text=f"입력하신 내용: {user_input}")


tk.Button(root, text="확인하기", command=show_input).pack(pady=10)

result_label = tk.Label(root, text="", font=("맑은 고딕", 11), fg="green")
result_label.pack()

'''
def make_number():
    import random
    return random.randint(1,50)

num_a = make_number()'''

import random

num_a = random.randint(1,50)

print(num_a)

while True:
    num = int(input("숫자를 입력하세요.:"))

    if num == num_a:
         print("축하합니다. 정답입니다.")
         break
    elif num < num_a:
         print(" 아쉬워요. 숫자를 올려주세요! ")
    else:
         print(" 아쉬워요. 숫자를 내려주세요! ")



root.mainloop()


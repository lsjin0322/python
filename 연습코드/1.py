from tkinter import *

root = Tk()
root.mainloop()

# tk_windowsettings.py
from tkinter import *

root = Tk()

root.title("siso")
root.geometry("300x200+100+100")
root.resizable(False, False)

root.mainloop()

# tkinter로 hello world 출력하기
# filename : tk_hellowarld.py
# ciding : utf-8

# tkinter 하이브러리 import
from tkinter import *

# tk 객체 인스턴스 생성하기 
root = Tk()

# 레이블 생성 
label = Label(root, text='Hello World')

# 레이블을 화면에 배치 
label.pack()

# 메인 화면 표시 
root.mainloop()

# tkinter 라이브러리 import
from tkinter import*

# tk 객체 인스턴스 생성하기 
root = Tk()
root.title("siso")
root.geometry("300x200+100+100")
root.resizable(False, False)

# 레이블 생성
label = Label(root, text='Hello World')

# 레이블을 화면에 배치
label.pack()

# 메인 화면 표시 
root.mainloop()

# tkinter 라이브러리 import
from tkinter import *

# tk 객체 인스턴스 생성하기 
root = Tk()
root.title("siso")
root.geometry("300x200+100+100")
root.resizable(False,False)

# 레이블 생성 
label = Label(root, text="Hello World", width=10, height=5, fg="red", relief="solid")

# 레이블을 화면에 배치
label.pack()

# 메인 화면 표시 
root.mainloop()

# tkinter 라이브러리 import
from tkinter import *

# tk 객체 인스턴스 생성하기 
root = Tk()
root.title("siso")
root.geometry("300x200+100+100")
root.resizable(False,False)


# 레이블 생성
label = Label(root, text="Hello World", width=100, height=50, fg="red", relief="solid", bitmap="info", compound="top")

# 레이블을 화면에 배치
label.pack()

# 메인 화면 표시 
root.mainloop()

# tkinter 라이브러리 import
from tkinter import *

# tk 객체 인스턴스 생성하기 
root = Tk()
root.title("siso")
root.geometry("300x200+100+100")
root.resizable(False,False)

count = 0

def countplus():
    global count
    count +=1
    label.config(text=str(count))

def countminus():
    global count
    count -=1
    label.config(text=str(count))

# 레이블 생성
label = Label(root, text="0")
label.pack()

# 버튼 생성
button1 = Button(root, width=10, text="plus", overrelief="solid", command=countplus)
button1.pack()

button2 = Button(root, width=10,text="minus",overrelief="solid",command=countminus)
button2.pack()

# 레이블을 화면에 배치
label.pack()

# 메인 화면 표시 
root.mainloop()


# tkinter 라이브러리 import
from tkinter import *

# tk 객체 인스턴스 생성하기 
root = Tk()
root.title("siso")
root.geometry("300x200+100+100")
root.resizable(False,False)

# tkinter 라이브러리 import
from tkinter import*

def calc(event):
    label.config(text="계산결과: " + str(eval(entry.get())))

# tk 객체 인스턴스 생성하기

# tkinter 라이브러리 import
from tkinter import *

# tk 객체 인스턴스 생성하기 
root = Tk()
root.title("siso")
root.geometry("300x200+100+100")
root.resizable(False,False)

# 레이블 생성 
label = Label(root, text="0")
label.pack()

# Entry 생성
entry = Entry(root,width=30)
entry.bind("<Return>", calc)
entry.pack()


# 메인 화면 표시 
root.mainloop()


import tkinter as tk
from tkinter import messagebox
# from pandas import value_counts
#
# 기본 창 구성
# root = tk.Tk() # 창 생성
# root.title("GUI 프로그래밍 실습") # 창 제목(타이틀)
# root .geometry("800x500") # 창 크기 설정(가로x세로)
# root .resizable(True,False) # 창 크기 조절 가능/불가능
#
#
# label = tk.Label(root, text="안녕 하세요", fg="red" ,bg="blue")
# label.pack(side ="top")
#
# def button_click():
#     print("클릭됨")
#     print(chk_var.get())    # 종료
#     print(radio_var.get())
#     root.quit()
#
# button = tk.Button(root, text = "종료", command=button_click)
# button.pack(side = "bottom")
#
# entry = tk.Entry(root)
# entry.pack(side="top")
#
# text = tk.Text(root, wrap="word")
# # none : 줄 내림 하지 않음
# # char : 글자 단위로 줄 내림
# # word : 단어 단위로 줄 내림
# text.pack(side="top")
#
# chk_var = tk.IntVar()
# chk = tk.Checkbutton(root, text="위 내용에 거짓이 없음을 동의 합니다.",variable=chk_var)
# chk.pack(side="bottom")
#
# def value_print():
#     print(radio_var.get())
#
# # radio_var1 = tk.IntVar()
# # radio_var2 = tk.IntVar()
# # radio_var3 = tk.IntVar()
#
# radio_var = tk.StringVar()
# r1 = tk.Radiobutton(root, text = "옵션1", variable=radio_var, value="옵션 1",command=value_print)
# r2 = tk.Radiobutton(root, text = "옵션2", variable=radio_var, value="옵션 2",command=value_print)
# r3 = tk.Radiobutton(root, text = "옵션3", variable=radio_var, value="옵션 3",command=value_print)
# r1.pack(side="top")
# r2.pack(side="top")
# r3.pack(side="top")
#
# root.mainloop() # 창 실행

# 레이아웃

# root = tk.Tk()
# root.title("레이 아웃 실습")
# root.geometry("800x600")
#
# label1 = tk.Label(root, text="안녕하세요")
# label1.place(x=0,y=0)
#
# label2 = tk.Label(root, text="반갑습니다")
# label2.place(x=50,y=50)
#
# label5 = tk.Label(root, text="파이썬입니다.")
# label5.place(x=100,y=100)
#
# label3 = tk.Label(root, text="소통해요")
# label3.place(x=200,y=150)
#
# label4 = tk.Label(root, text="ㅎㅎ")
# label4.place(x=150,y=200)
#
# root.mainloop()

root = tk.Tk()
root.title("회원가입창")
root.geometry("500x200")

id_label = tk.Label(root, text="아이디 : ")
id_label.grid(row=0, column=0, pady=10)

id_entry = tk.Entry(root)
id_entry.grid(row=0, column=1, padx=5)

def dupl_click():
    tk.messagebox.showinfo("중복확인", "중복확인 되었습니다.")

dupl_btn = tk.Button(root, text="중복확인", command=dupl_click)
dupl_btn.grid(row=0, column=2)

password_label = tk.Label(root, text="비밀번호 : ")
password_label.grid(row=1, column=0)

password_entry = tk.Entry(root, show="*")
password_entry.grid(row=1, column=1, padx=5)
chk_var = tk.IntVar()
chk = tk.Checkbutton(root, text="약관 내용에 동의합니다.", variable=chk_var)
chk.grid(row=2,column=1)

def signup_click():


    if chk_var.get() == 0:
        chk_value = "동의 안함"
    else:
        chk_value = "동의함"
    tk.messagebox.showinfo("회원가입 완료",f"{id_entry.get()}\n약관동의 : {chk_value}")

signup_btn = tk.Button(root, text="회원가입", command=signup_click)
signup_btn.grid(row=3, column=2)

root.mainloop()


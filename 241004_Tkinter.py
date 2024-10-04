import tkinter as tk

# 덧셈 연산
result = 2 + 3

# Tkinter 초기화
root = tk.Tk()
root.title("덧셈 결과")

# 레이블 생성
label = tk.Label(root, text=f"덧셈 결과는 {result}입니다.")
label.pack()

# 이벤트 루프 시작
root.mainloop()

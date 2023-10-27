#匯入tkinter模組，取一個簡稱tk 
import tkinter as tk

#宣告視窗
window = tk.Tk()

#設置視窗標題
window.title(" 你的名字 ")

#設置視窗大小
window.geometry("250x400")

#文字 label
#設定文字，(在哪一個視窗顯示 , 顯示的文字) fg=文字顏色 bg=背景顏色
word = tk.Label(window,text = " 我的第一個GUI介面 ",fg = '#5A5AAD',bg = '#FFE153')

#打包word放進視窗
word.pack()

#打字框 Entry
#設定打字框(在哪一個視窗顯示 , 寬度)
entry = tk.Entry(window , width = 20)

#打包entry放進視窗
entry.pack()

#按鈕 Button
#設定按鈕(在哪一個視窗顯示 , 顯示的文字)
button = tk.Button(window , text = "點我 ")

#打包button放進視窗
button.pack()

#讓視窗開始執行
window.mainloop()
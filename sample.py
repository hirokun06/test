#codimg:utf-8
import tkinter as tk#tkinterをインポートする

def Buttonclick():

	num=int(num_box.get())

	result_box.delete(0,tk.END)#bmi_boxの中身を0文字目から削除
	result_box.insert(0,num)#bmi_boxにbmiの値を0文字目から挿入

	flag = 0
	for ii in range(2,num):
		if num % ii == 0:
			flag = 1
			break
	if flag == 0:
		result = "素数です"
	else:
		result = "素数ではありません"

	check_box.delete(0,tk.END)#result_boxの中身を0文字目から削除
	check_box.insert(0,result)#result_boxにresultの値を0文字目から挿入

#ウィンドウを作る
root=tk.Tk()
root.geometry("400x300")#ウィンドウサイズの指定
root.title("素数判定")#ウィンドウに表示するタイトルを指定

#ラベルを作る
height_label=tk.Label(text="整数")
height_label.place(x=60,y=50)

input_label=tk.Label(text="入力値")
input_label.place(x=60,y=200)

result_label=tk.Label(text="判定結果は")
result_label.place(x=50,y=240)

#テキストボックスを作る
num_box=tk.Entry(width=20)
num_box.place(x=140,y=50)

result_box=tk.Entry(width=20)
result_box.place(x=140,y=200)

check_box=tk.Entry(width=20)
check_box.place(x=140,y=240)

#ボタンを作る
buttonl=tk.Button(root,text="判定する",font=("Halvetica",14),command=Buttonclick)
buttonl.place(x=140,y=130)

root.mainloop()
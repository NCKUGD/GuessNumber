# coding:utf-8
import random
import tkinter as tk
import tkinter.messagebox as tmsg

#當按鈕被點時的處理
def buttonClick():
    #取得文字輸入欄位裡的輸入字串
    b = editbox1.get()

    #判斷是否為4位數字
    fourDigitsFlag = False
    if len(b) != 4:
        tmsg.showerror("Error", "Please input four-digit number")
    else:
        pureNumber = True
        for i in range(4):
            if(b[i] < "0") or (b[i] > "9"):
                tmsg.showerror("Error", "Please input number")
                pureNumber = False
                break

        if pureNumber:
            fourDigitsFlag = True
            
    #當輸入為4為數字時
    if fourDigitsFlag:
        #判斷Hit
        hit = 0

        for i in range(4):
            if a[i] == int(b[i]):
                hit = hit + 1

        #判斷blow
        blow = 0
        for j in range(4):
            for i in range(4):
                if(int(b[j]) == a[i]) and (a[i] != int(b[i]))and (a[j] != int(b[j])):
                    blow = blow + 1
                    break
                
        #當hit為4時結束
        if hit == 4:
            tmsg.showinfo("You're right!", "Congrats")
            #結束
            root.destroy()
        else:
            #顯示Hit和Blow數量
            recordBox.insert(tk.END, b + " / Hit:" + str(hit) + " Blow:" + str(blow) + "\n")

#主程式
a = [random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9),
     random.randint(0, 9)]

#製作視窗
root = tk.Tk()
root.geometry("600x400")
root.title("猜數字遊戲")

#製作顯示紀錄的文字方塊
recordBox = tk.Text(root, font = ("Helvetica", 14))
recordBox.place(x = 400, y = 0, width = 200, height = 400)

#製作標籤
label1 = tk.Label(root, text = "Please input number", font = ("Helvetica", 14))
label1.place(x = 20, y = 20)

#製作文字方塊
editbox1 = tk.Entry(width = 4, font = ("Helvetica", 28))
editbox1.place(x = 120, y = 60)
                    
#製作按鈕
button1 = tk.Button(root, text = "confirm", font = ("Helvetica", 14), command = buttonClick)
button1.place(x = 220, y = 60)


#顯示視窗
root.mainloop()

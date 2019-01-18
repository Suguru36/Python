##! /usr/bin/env python
# coding: UTF-8
import tkinter

#メインフレーム
root = tkinter.Tk()
#フレーム
frame = tkinter.Frame(root)
frame.pack()

#Photo Imageオブジェクトを生成
my_image = tkinter.PhotoImage(file="sizuka.png")

#my_imageをラベルとして生成
label = tkinter.Label(frame, image=my_image)
label.pack()

root.mainloop()

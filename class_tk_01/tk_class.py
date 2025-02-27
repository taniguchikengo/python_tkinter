from tkinter import *

class MainScreen(object):
    root = Tk()
    x = root.winfo_screenwidth() // 2  # アプリ表示位置(x座標)
    y = root.winfo_screenheight() // 5  # アプリ表示位置(y座標)

    def __init__(self,title_name,w_size,h_size):
        self.root.title(title_name)
        self.root.geometry(f"{w_size}x{h_size}+{self.x-w_size//2}+{self.y}")

    def bt_set(self,text_name,x_point,y_point,w_size=10):
        bt = Button(self.root,text=text_name,width=w_size)
        bt.place(x=x_point,y=y_point)
        return bt

    def get_scene_size(self):
        return self.x,self.y

    def set_action(self,button_oj,b_action):
        button_oj["command"]=b_action




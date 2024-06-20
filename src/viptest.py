import subprocess
import tkinter as tk

# 一些好用的解析接口
head_urls = ['https://jx.jsonplayer.com/player/?url=',
             'https://www.ckplayer.vip/jiexi/?url=',
             'https://jx.yangtu.top/?url=',
             'https://jx.playerjy.com/?url=',
             'https://jx.yparse.com/index.php?url=',
             'https://www.8090g.cn/?url=',
             'https://www.pouyun.com/?url=',
             'https://jx.xmflv.com/?url=',
             'https://43.240.74.102:4433?url=',
             'https://api.okjx.cc:3389/jx.php?url=',
             'https://okjx.cc/?url=',
             'https://im1907.top/?jx=',
             'https://jx.aidouer.net/?url=',
             'https://jx.iztyy.com/Bei/?url=',
             'https://www.yemu.xyz/?url=',
             'https://www.mtosz.com/m3u8.php?url=',
             'https://jx.m3u8.tv/jiexi/?url=',
             'https://parse.123mingren.com/?url=',
             'https://jx.4kdv.com/?url=',
             'https://ckmov.ccyjjd.com/ckmov/?url=',
             'https://api.qianqi.net/vip/?url=',
             'https://vip.laobandq.com/jiexi.php?url=',
             'https://www.playm3u8.cn/jiexi.php?url=',
             'https://www.administratorw.com/video.php?url=',
             'https://go.yh0523.cn/y.cy?url=',
             'https://jx.blbo.cc:4433/?url=']


# 按键响应的处理函数
def handle_button_click(url, txt):
    full_url = url + txt.get()
    # print(full_url)
    subprocess.run(['start', full_url], shell=True, encoding='utf-8')


# 按键响应
def button_click(line, txt):
    handle_button_click(head_urls[line - 1], txt)


# 输入框的文本重置清空
def ent_cls(ent):
    ent.delete(0, "end")


# 置顶部分实现函数
def toggle_topmost(root):
    current_state = root.attributes("-topmost")  # 获取当前窗口的顶置状态
    root.attributes("-topmost", not current_state)  # 切换顶置状态

    # 清除该位置之前的布局内容
    previous_txt = root.grid_slaves(row=10, column=3)
    for widget in previous_txt:
        widget.grid_forget()

    # 未顶置按钮设置为绿色，顶置按钮设置为红色
    if root.attributes("-topmost") == 0:
        button = tk.Button(root, text="未顶置", command=lambda: toggle_topmost(root), fg='#19c37d')
        button.place(x=320, y=270)
    else:
        button = tk.Button(root, text="已顶置", command=lambda: toggle_topmost(root), fg='#ff1030')
        button.place(x=320, y=270)


def main():
    root = tk.Tk()
    # 窗口标题
    root.title("视频解析（仅供学习）")
    # 窗口大小
    root.geometry("380x310")
    # 不允许改变尺寸
    root.resizable(False, False)
    txt = tk.Label(root, text='请输入视频网址：', font=40, fg='#24abf2')
    txt.place(x=20, y=20)
    # 输入框
    key_word = tk.StringVar()
    ent = tk.Entry(root, textvariable=key_word)
    ent.place(x=170, y=20)

    # 输入框的文本重置按钮
    button_cls = tk.Button(root, text="重置", command=lambda: ent_cls(ent))
    button_cls.place(x=325, y=20)

    # 为了自定义位置修改方便，一个一个按钮整，手麻了(っ °Д °;)っ
    button1 = tk.Button(root, text="线路1", command=lambda: button_click(1, key_word))
    button1.place(x=20, y=70)

    button2 = tk.Button(root, text="线路2", command=lambda: button_click(2, key_word))
    button2.place(x=80, y=70)

    button3 = tk.Button(root, text="线路3", command=lambda: button_click(3, key_word))
    button3.place(x=140, y=70)

    button4 = tk.Button(root, text="线路4", command=lambda: button_click(4, ent))
    button4.place(x=200, y=70)

    button5 = tk.Button(root, text="线路5", command=lambda: button_click(5, ent))
    button5.place(x=260, y=70)

    button6 = tk.Button(root, text="线路6", command=lambda: button_click(6, ent))
    button6.place(x=320, y=70)

    button7 = tk.Button(root, text="线路7", command=lambda: button_click(7, ent))
    button7.place(x=20, y=120)

    button8 = tk.Button(root, text="线路8", command=lambda: button_click(8, ent))
    button8.place(x=80, y=120)

    button9 = tk.Button(root, text="线路9", command=lambda: button_click(9, ent))
    button9.place(x=140, y=120)

    button10 = tk.Button(root, text="线路10", command=lambda: button_click(10, ent))
    button10.place(x=200, y=120)

    button11 = tk.Button(root, text="线路11", command=lambda: button_click(11, ent))
    button11.place(x=260, y=120)

    button12 = tk.Button(root, text="线路12", command=lambda: button_click(12, ent))
    button12.place(x=320, y=120)

    button13 = tk.Button(root, text="线路13", command=lambda: button_click(13, ent))
    button13.place(x=20, y=170)

    button14 = tk.Button(root, text="线路14", command=lambda: button_click(14, ent))
    button14.place(x=80, y=170)

    button15 = tk.Button(root, text="线路15", command=lambda: button_click(15, ent))
    button15.place(x=140, y=170)

    button16 = tk.Button(root, text="线路16", command=lambda: button_click(16, ent))
    button16.place(x=200, y=170)

    button17 = tk.Button(root, text="线路17", command=lambda: button_click(17, ent))
    button17.place(x=260, y=170)

    button18 = tk.Button(root, text="线路18", command=lambda: button_click(18, ent))
    button18.place(x=320, y=170)

    button19 = tk.Button(root, text="线路19", command=lambda: button_click(19, ent))
    button19.place(x=20, y=220)

    button20 = tk.Button(root, text="线路20", command=lambda: button_click(20, ent))
    button20.place(x=80, y=220)

    button21 = tk.Button(root, text="线路21", command=lambda: button_click(21, ent))
    button21.place(x=140, y=220)

    button22 = tk.Button(root, text="线路22", command=lambda: button_click(22, ent))
    button22.place(x=200, y=220)

    button23 = tk.Button(root, text="线路23", command=lambda: button_click(23, ent))
    button23.place(x=260, y=220)

    button24 = tk.Button(root, text="线路24", command=lambda: button_click(24, ent))
    button24.place(x=320, y=220)

    button25 = tk.Button(root, text="线路25", command=lambda: button_click(25, ent))
    button25.place(x=20, y=270)

    button26 = tk.Button(root, text="线路26", command=lambda: button_click(26, ent))
    button26.place(x=80, y=270)
    # 一个顶置设置按钮，方便使用
    button = tk.Button(root, text="未顶置", command=lambda: toggle_topmost(root), fg='#19c37d')
    button.place(x=320, y=270)

    root.mainloop()


if __name__ == "__main__":
    main()
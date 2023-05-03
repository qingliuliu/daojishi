import base64
import tkinter as tk
from datetime import datetime, date
import io
from tkinter import ttk
import webbrowser


# 获取距离指定日期还有多少天
def get_days_left(target_date):
    today = date.today()
    remaining_days = (target_date - today).days
    return remaining_days

# 设置目标日期为6月25日
target_date = date(date.today().year, 6, 25)

# 创建主窗口
root = tk.Tk()
root.title("中考倒计时")
root.resizable(False, False)

# 设置窗口图标
icon_base64 = b'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'
icon_data = base64.b64decode(icon_base64)
icon_image = tk.PhotoImage(data=icon_data)
root.tk.call('wm', 'iconphoto', root._w, icon_image)

# 获取屏幕的宽度和高度
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# 设置窗口位置为屏幕的右下角
root.geometry("+{}+{}".format(screen_width - 430, screen_height - 280))

# 设置窗口背景色为红色
root.configure(bg="red")

# 创建标签，显示倒计时信息
label = tk.Label(root, font=("微软雅黑", 30), fg="white", bg="red")
label.pack(padx=20, pady=20)

# 更新标签内容，显示距离中考还有多少天
def update_label():
    days_left = get_days_left(target_date)
    label.config(text=" 距离中考还有{}天！".format(days_left))
    root.after(1000, update_label)

update_label()

# 创建鼓励标签，显示“鼓励的话”
encourage_label = tk.Label(root, text="向着梦想奋斗的路途虽然漫长，但努力的每一步", font=("微软雅黑", 13), fg="white", bg="red")
encourage_label.pack(padx=10, pady=1)
encourage_label = tk.Label(root, text="都是向着成功不断靠近的坚实台阶。", font=("微软雅黑", 13), fg="white", bg="red")
encourage_label.pack(padx=10, pady=1)


# 创建关闭按钮
close_button = tk.Button(root, text="关闭", command=root.quit)
close_button.pack(side=tk.RIGHT, padx=10, pady=10)

# 创建最小化按钮
minimize_button = tk.Button(root, text="最小化", command=root.iconify)
minimize_button.pack(side=tk.RIGHT, padx=10, pady=10)

# 创建固定/解除固定按钮
def toggle_topmost():
    if root.attributes("-topmost"):
        root.attributes("-topmost", False)
        topmost_button.config(text="固定")
    else:
        root.attributes("-topmost", True)
        topmost_button.config(text="解除固定")

topmost_button = tk.Button(root, text="固定", command=toggle_topmost)
topmost_button.pack(side=tk.RIGHT, padx=10, pady=10)

# 创建底部标签，显示“code by qingliuliu@github”
def open_url(event):
    webbrowser.open_new_tab("http://chanshiyu.icu")

bottom_label = tk.Label(root, text="code by zht,me:http://chanshiyu.icu", font=("微软雅黑", 9), fg="white", bg="red", cursor="hand2")
bottom_label.bind("<Button-1>", open_url)
bottom_label.pack(side=tk.BOTTOM, pady=5)


root.mainloop()


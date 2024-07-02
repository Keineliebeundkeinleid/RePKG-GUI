import subprocess
import tkinter as tk
import tkinter
from tkinter import filedialog
import json

RePKG_path = None
wallpaper_path = None
save_path = None

def choose_RePKG():
    # 设置文件对话框将会打开的文件类型
    filetypes = (
        ('text files', '*.exe'),
        ('All files', '*.*')
    )

    global RePKG_path

    # 打开文件选择对话框，并获取选择的文件路径
    RePKG_path = filedialog.askopenfilename(
        title='打开文件',
        initialdir='/',
        filetypes=filetypes
    )
    entry_RePKG.insert(0, RePKG_path)


def choose_wallpaper():
    # 设置文件对话框将会打开的文件类型
    filetypes = (
        ('text files', '*.pkg'),
        ('All files', '*.*')
    )

    global wallpaper_path

    # 打开文件选择对话框，并获取选择的文件路径
    wallpaper_path = filedialog.askopenfilename(
        title='打开文件',
        initialdir='/',
        filetypes=filetypes
    )
    entry_wallpaper.insert(0, wallpaper_path)


def choose_save():
    global save_path

    # 打开文件选择对话框，并获取选择的文件路径
    save_path = filedialog.askdirectory()
    entry_save.insert(0, save_path)



def extract():

    extract = RePKG_path+ ' extract '+wallpaper_path+' -o '+save_path

    subprocess.run(extract, capture_output=True, text=True)
    label_OK = tk.Label(root, text='提取完成')
    label_OK.place(x=343, y=440)


# 创建主窗口
root = tk.Tk()
root.title('RePKG-GUI')
root.geometry('720x490')


# RePKG
button_RePKG = tk.Button(root, text='选择文件', command=choose_RePKG)   # 按钮
button_RePKG.place(x=600, y=50)

label_RePKG = tk.Label(root, text='RePKG程序位置')   # 字
label_RePKG.place(x=320, y=20)

entry_RePKG = tkinter.StringVar()   # 文本框
entry_RePKG = tkinter.Entry(root, textvariable=entry_RePKG, font=('FangSong', 15), width=40, state='normal')
entry_RePKG.place(x=150, y=55)

# wallpaper
button_wallpaper = tk.Button(root, text="选择文件", command=choose_wallpaper)   # 按钮
button_wallpaper.place(x=600, y=310)

label_wallpaper = tk.Label(root, text='wallpaper壁纸pkg文件位置')   # 字
label_wallpaper.place(x=285, y=260)

entry_wallpaper = tkinter.StringVar()   # 文本框
entry_wallpaper = tkinter.Entry(root, textvariable=entry_wallpaper, font=('FangSong', 15), width=40, state='normal')
entry_wallpaper.place(x=150, y=315)

# 保存
button_save = tk.Button(root, text="选择文件", command=choose_save)
button_save.place(x=600, y=180)

label_save = tk.Label(root, text='保存位置')
label_save.place(x=340, y=140)

entry_save = tkinter.StringVar()   # 文本框
entry_save = tkinter.Entry(root, textvariable=entry_save, font=('FangSong', 15), width=40, state='normal')
entry_save.place(x=150, y=185)

# 提取
button_extract = tk.Button(root, text='提取', command=extract)
button_extract.place(x=315, y=400)
button_extract.config(width=14, height=1)

# 完成提取
label = tk.Label(root, text='提取完成后打开  ->  保存的位置  ->  materials')
label.place(x=450, y=470)
# 运行主循环
root.mainloop()



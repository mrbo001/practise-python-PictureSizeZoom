import os
from tkinter import *
from tkinter import filedialog
from PIL import Image

root = Tk()
root.title("图片批量缩放工具")
root.geometry("360x280")

Label(root, text="缩放比例：").grid(row=0, column=0)

scale_var = StringVar()
scale_var.set("0.5")
Entry(root, width=10, textvariable=scale_var).grid(row=0, column=1)


def resize_image(file_path, scale):
    """按比例缩放图片并保存"""
    try:
        img = Image.open(file_path)
        w, h = img.size
        img = img.resize((int(w * scale), int(h * scale)), Image.ANTIALIAS)
        new_file_name = os.path.splitext(file_path)[0] + "_resized.jpg"
        img.save(new_file_name)
        print(f"{file_path} 缩放成功并保存为 {new_file_name}")
    except Exception as e:
        print(f"{file_path} 缩放失败：{e}")


def select_directory():
    """选择文件夹"""
    directory = filedialog.askdirectory()
    # 遍历文件夹下的所有图片
    for filename in os.listdir(directory):
        if filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            # 缩放并保存图片
            scale = float(scale_var.get())
            file_path = os.path.join(directory, filename)
            resize_image(file_path, scale)


Button(root, text="选择文件夹", command=select_directory).grid(row=1, columnspan=2, pady=20)


root.mainloop()

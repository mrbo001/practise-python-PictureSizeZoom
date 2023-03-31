import tkinter as tk
import os
from PIL import Image
from tkinter import filedialog

def resize_images(input_dir, output_dir, size):
    """
    将指定文件夹下的所有图片文件等比缩放到指定大小，并保存到新的文件夹中
    :param input_dir: 输入文件夹的路径
    :param output_dir: 输出文件夹的路径
    :param size: 输出图片的大小（宽，高）
    """
    if not os.path.exists(output_dir):
        os.mkdir(output_dir)

    for filename in os.listdir(input_dir):
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.jpeg'):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            with Image.open(input_path) as img:
                w, h = img.size
                ratio = min(size[0] / w, size[1] / h)
                new_size = (int(w * ratio), int(h * ratio))
                img = img.resize(new_size, Image.ANTIALIAS)
                img.save(output_path)

def select_input_dir():
    # 弹出选择文件夹对话框
    input_dir = filedialog.askdirectory()
    input_dir_entry.delete(0, tk.END)
    input_dir_entry.insert(0, input_dir)

def select_output_dir():
    # 弹出选择文件夹对话框
    output_dir = filedialog.askdirectory()
    output_dir_entry.delete(0, tk.END)
    output_dir_entry.insert(0, output_dir)

def resize_images_command():
    # 获取输入参数
    input_dir = input_dir_entry.get()
    output_dir = output_dir_entry.get()
    width = int(width_entry.get())
    height = int(height_entry.get())
    size = (width, height)
    # 执行缩放操作
    resize_images(input_dir, output_dir, size)
    # 提示完成
    tk.messagebox.showinfo(title="提示", message="操作完成！")

# 创建主窗口
root = tk.Tk()
root.title("批量缩放图片")

# 设置窗口尺寸
root.minsize(500, 130)
root.maxsize(500, 130)

# 创建输入控件
input_dir_label = tk.Label(root, text="输入目录:")
input_dir_entry = tk.Entry(root, width=50)
input_dir_button = tk.Button(root, text="选择", command=select_input_dir)

# 创建输出控件
output_dir_label = tk.Label(root, text="输出目录:")
output_dir_entry = tk.Entry(root, width=50)
output_dir_button = tk.Button(root, text="选择", command=select_output_dir)

# 创建尺寸控件
size_label = tk.Label(root, text="输出[宽|高]:")
width_entry = tk.Entry(root, width=15)
height_entry = tk.Entry(root, width=15)

# 创建确认按钮
resize_button = tk.Button(root, text="确定",width=15, command=resize_images_command)

# 布局控件
input_dir_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
input_dir_entry.grid(row=0, column=1, padx=5, pady=5, sticky=tk.W)
input_dir_button.grid(row=0, column=2, padx=5, pady=5, sticky=tk.W)

output_dir_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
output_dir_entry.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
output_dir_button.grid(row=1, column=2, padx=5, pady=5, sticky=tk.W)

size_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
width_entry.grid(row=2, column=1, padx=5, pady=5, sticky=tk.W)
height_entry.grid(row=2, column=1, padx=5, pady=5)

resize_button.grid(row=2, column=1, padx=5, pady=5, sticky=tk.E)


# 运行主循环
root.mainloop()

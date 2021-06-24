"""
开发记事本软件练习
"""

from tkinter import *
from tkinter import messagebox
from tkinter.colorchooser import *
from tkinter.filedialog import *


class Application(Frame):
    """一个经典的GUI程序的类的写法"""

    def __init__(self, master):
        super().__init__(master)  # super()代表的是父类的定义，而不是父类对象
        self.master = master
        self.pack()

        self.createWidget()

    def createWidget(self):
        """创建组件"""
        # 创建主菜单栏
        menubar = Menu(root)

        # 创建子菜单
        menuFile = Menu(menubar)
        menuEdit = Menu(menubar)
        menuHelp = Menu(menubar)

        # 将子菜单加入到主菜单栏中
        menubar.add_cascade(label="文件(F)", menu=menuFile)
        menubar.add_cascade(label="编辑(E)", menu=menuEdit)
        menubar.add_cascade(label="帮助(H)", menu=menuHelp)

        # 添加菜单项
        menuFile.add_command(label="新建(N)", accelerator="ctrl+n", command=self.newfile)
        menuFile.add_command(label="打开(O)", accelerator="ctrl+o", command=self.openfile)
        menuFile.add_command(label="保存(S)", accelerator="ctrl+s", command=self.savefile)
        menuFile.add_separator()  # 添加分割线
        menuFile.add_command(label="退出(x)", accelerator="ctrl+q", command=self.exit)

        menuEdit.add_command(label="剪切(T)", accelerator="ctrl+x", command=self.test)
        menuEdit.add_command(label="复制(C)", accelerator="ctrl+c", command=self.test)
        menuEdit.add_command(label="粘贴(P)", accelerator="ctrl+v", command=self.test)
        menuEdit.add_separator()  # 添加分割线
        menuEdit.add_command(label="删除(L)", accelerator="Del", command=self.test)

        menuHelp.add_command(label="帮助(H)", command=self.test)
        menuHelp.add_command(label="反馈(F)", command=self.test)
        menuHelp.add_command(label="关于(A)", command=self.test)

        # 将主菜单栏加到根窗口
        root["menu"] = menubar

        # 增加快捷键处理
        root.bind("<Control-n>", lambda event:self.newfile())
        root.bind("<Control-o>", lambda event:self.openfile())
        root.bind("<Control-s>", lambda event:self.savefile())
        root.bind("<Control-q>", lambda event:self.exit())

        # 文本编辑区
        self.textpad = Text(root, width=90, height=30)
        self.textpad.pack()

        # 创建上下菜单
        self.contextMenu = Menu(root)
        self.contextMenu.add_command(label="背景颜色", command=self.openColor)

        # 为右键绑定事件
        root.bind("<Button-3>", self.createContextMenu)


    def openfile(self):
        """打开文件"""
        self.textpad.delete("1.0", "end")   # 将控件中的所有的内容清空
        with askopenfile(title="打开文本文件") as f:
            self.textpad.insert(INSERT, f.read())   # 在文本显示框显示，插入
            self.filename = f.name


    def savefile(self):
        """保存文件"""
        with open(self.filename, "w") as f:
            c = self.textpad.get(1.0, END)
            f.write(c)


    def exit(self):
        """退出，关闭窗口"""
        root.quit()


    def newfile(self):
        """新建文件"""
        self.filename = asksaveasfilename(title="另存为", initialfile="未命名.txt",
                                          filetypes=[("文本文档", "*.txt")],
                                          defaultextension=".txt")
        self.savefile()


    def openColor(self):
        s1 = askcolor(color="blue", title="选择背景色")
        self.textpad.config(bg=s1[1])

        pass
    def test(self):
        """测试"""
        messagebox.showinfo("测试窗口", "只是测试")


    def createContextMenu(self, event):
        # 菜单在鼠标右键单击的坐标处显示
        self.contextMenu.post(event.x_root, event.y_root)

if __name__ == '__main__':
    root = Tk()
    root.geometry("600x300+500+200")
    root.title("咸鱼记事本")
    app = Application(master=root)

    root.mainloop()
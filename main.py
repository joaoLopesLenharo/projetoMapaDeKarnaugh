import tkinter as tk
import subprocess

class Interface:
    def __init__(self, master):
        self.master = master
        master.title("Interface Principal")

        self.label = tk.Label(master, text="Escolha o número de variáveis:")
        self.label.pack()

        self.button_2 = tk.Button(master, text="2 variáveis", command=self.interface_2v)
        self.button_2.pack()

        self.button_3 = tk.Button(master, text="3 variáveis", command=self.interface_3v)
        self.button_3.pack()

        self.button_4 = tk.Button(master, text="4 variáveis", command=self.interface_4v)
        self.button_4.pack()

    def interface_2v(self):
        self.hide()
        subprocess.run(["python", "Interface2V.py"])
        self.show()

    def interface_3v(self):
        self.hide()
        subprocess.run(["python", "interface3V.py"])
        self.show()

    def interface_4v(self):
        self.hide()
        subprocess.run(["python", "interface4V.py"])
        self.show()

    def hide(self):
        self.master.withdraw()

    def show(self):
        self.master.deiconify()

def main():
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()

if __name__ == "__main__":
    main()

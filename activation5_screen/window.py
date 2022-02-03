from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("944x828")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 828,
    width = 944,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file =f"background.png")
background = canvas.create_image(
    471.5, 421.5,
    image=background_img)

img0 = PhotoImage(file =f"img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 351, y = 376,
    width = 452,
    height = 91)

entry0_img = PhotoImage(file =f"img_textBox0.png")
entry0_bg = canvas.create_image(
    577.0, 571.5,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#c4c4c4",
    highlightthickness = 0)

entry0.place(
    x = 392, y = 556,
    width = 370,
    height = 29)

img1 = PhotoImage(file =f"img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b1.place(
    x = 406, y = 675,
    width = 337,
    height = 100)

window.resizable(False, False)
window.mainloop()


# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\LukeLab\Tkinter-Designer\UI output\t14\build\assets\frame6")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1096x728")
window.configure(bg = "#F1F5F9")


canvas = Canvas(
    window,
    bg = "#F1F5F9",
    height = 728,
    width = 1096,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    548.0,
    364.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    648.0,
    385.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1012.0,
    30.0,
    image=image_image_3
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    971.0,
    30.0,
    image=image_image_4
)

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    328.0,
    30.0,
    image=image_image_5
)

image_image_6 = PhotoImage(
    file=relative_to_assets("image_6.png"))
image_6 = canvas.create_image(
    534.0,
    30.0,
    image=image_image_6
)

image_image_7 = PhotoImage(
    file=relative_to_assets("image_7.png"))
image_7 = canvas.create_image(
    534.0,
    30.0,
    image=image_image_7
)

image_image_8 = PhotoImage(
    file=relative_to_assets("image_8.png"))
image_8 = canvas.create_image(
    328.0,
    30.0,
    image=image_image_8
)

canvas.create_text(
    536.0,
    703.0,
    anchor="nw",
    text="placeholder for dji",
    fill="#64748B",
    font=("ArialMT", 12 * -1)
)

canvas.create_text(
    273.0,
    704.0,
    anchor="nw",
    text="placeholder for spx",
    fill="#64748B",
    font=("ArialMT", 12 * -1)
)

canvas.create_text(
    404.0,
    704.0,
    anchor="nw",
    text="placeholder for ndx",
    fill="#64748B",
    font=("ArialMT", 12 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    640.0,
    376.0,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#EFF4FB",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=269.0,
    y=176.0,
    width=742.0,
    height=398.0
)

canvas.create_text(
    275.0,
    605.0,
    anchor="nw",
    text="Note: placeholder for the app log loaction",
    fill="#64748B",
    font=("ArialMT", 12 * -1)
)
window.resizable(False, False)
window.mainloop()

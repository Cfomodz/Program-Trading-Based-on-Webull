import tkinter as tk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


class SaveExit(tk.Frame):

    def __init__(self, parent):
        # Initialize the frame
        tk.Frame.__init__(self, parent)
        self.name = "SaveExit"
        self.parent = parent
        self.current = False

        # UI elements：
        OUTPUT_PATH = Path(__file__).parent
        ASSETS_PATH = OUTPUT_PATH / Path(r"./frame9")

        def relative_to_assets(path: str) -> Path:
            return ASSETS_PATH / Path(path)

        self.canvas = Canvas(
            self,
            bg="#F1F5F9",
            height=728,
            width=1096,
            bd=0,
            highlightthickness=0,
            relief="ridge"
        )

        self.canvas.place(x=0, y=0)
        self.image_image_1 = PhotoImage(
            file=relative_to_assets("image_1.png"))
        self.image_1 = self.canvas.create_image(
            548.0,
            364.0,
            image=self.image_image_1
        )

        self.image_image_2 = PhotoImage(
            file=relative_to_assets("image_2.png"))
        self.image_2 = self.canvas.create_image(
            648.0,
            385.0,
            image=self.image_image_2
        )

        self.image_image_3 = PhotoImage(
            file=relative_to_assets("image_3.png"))
        self.image_3 = self.canvas.create_image(
            1012.0,
            30.0,
            image=self.image_image_3
        )

        self.image_image_4 = PhotoImage(
            file=relative_to_assets("image_4.png"))
        self.image_4 = self.canvas.create_image(
            971.0,
            30.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file=relative_to_assets("image_5.png"))
        self.image_5 = self.canvas.create_image(
            328.0,
            30.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file=relative_to_assets("image_6.png"))
        self.image_6 = self.canvas.create_image(
            534.0,
            30.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file=relative_to_assets("image_7.png"))
        self.image_7 = self.canvas.create_image(
            534.0,
            30.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file=relative_to_assets("image_8.png"))
        self.image_8 = self.canvas.create_image(
            328.0,
            30.0,
            image=self.image_image_8
        )

        self.canvas.create_text(
            536.0,
            704.0,
            anchor="nw",
            text="placeholder for dji",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.canvas.create_text(
            273.0,
            704.0,
            anchor="nw",
            text="placeholder for spx",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.canvas.create_text(
            404.0,
            704.0,
            anchor="nw",
            text="placeholder for ndx",
            fill="#64748B",
            font=("ArialMT", 12 * -1)
        )

        self.canvas.create_text(
            706.0,
            342.0,
            anchor="nw",
            text="seconds",
            fill="#004434",
            font=("ArialRoundedMTBold", 16 * -1)
        )

        self.canvas.create_text(
            466.0,
            342.0,
            anchor="nw",
            text="APP State Saved, will exit in ",
            fill="#004434",
            font=("ArialRoundedMTBold", 16 * -1)
        )

        self.canvas.create_text(
            680.0,
            342.0,
            anchor="nw",
            text="3",
            fill="#004434",
            font=("ArialRoundedMTBold", 16 * -1)
        )

        self.canvas.pack(fill="both", expand=True)

        self.canvas.bind("<Button-1>", self.frame_clicked)

    def frame_clicked(self, event):
        x = event.x
        y = event.y
        print(f"{self.name} clicked, x: {x} y: {y}")
        if x <= 200:
            # Sidebar area clicked
            print("Sidebar clicked, frame0")
            self.parent.sidebar_clicked(x, y)
        elif 200 <= x <= 1096 and y <= 60:
            # Top bar area clicked
            print("Top_bar clicked, frame0")
            self.parent.top_bar_clicked(x, y)
        else:
            # frame area clicked
            pass

    def msg_clicked(self, event):
        print(f"{self.name}: Message clicked")

    def notify_clicked(self, event):
        print(f"{self.name}: Notify clicked")


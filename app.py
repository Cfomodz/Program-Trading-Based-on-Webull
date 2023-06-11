"""

APP GUI Main interface

LukeLab, 05/2023

"""
from tkinter import *
import tkinter as tk
from tkinter import font as tkfont  # python 3

# import gui frame classes:
from gui.gui_0_DashboardLogin.DashboardLogin import DashboardLogin
from gui.gui_1_DashboardLogged.DashboardLogged import DashboardLogged
from gui.gui_2_StrategyMonitor.StrategyMonitor import StrategyMonitor
from gui.gui_3_TreaderProfile.TreaderProfile import TreaderProfile
from gui.gui_4_TradingList.TradingList import TradingList
from gui.gui_5_Performance.Performance import Performance
from gui.gui_6_APPLog.APPLog import APPLog
from gui.gui_7_Message.Message import Message
from gui.gui_8_DownloadData.DownloadData import DownloadData
from gui.gui_9_SaveExit.SaveExit import SaveExit


class TradingApp(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # set app icon
        icon_photo = PhotoImage(file="gui/icon.png")
        self.iconphoto(False, icon_photo)

        # set app window size
        self.geometry("1096x728")
        self.configure(bg="#FFFFFF")
        self.title("APP GUI")
        self.title_font = tkfont.Font(
            family="Arial Rounded MT Bold", size=18, weight="bold", slant="italic"
        )
        self.resizable(False, False)

        # container for all frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, minsize=728, weight=1)
        container.grid_columnconfigure(0, minsize=1096, weight=1)

        # set dict save all frame obj
        self.frames = {}
        frame_objs = [DashboardLogin, DashboardLogged, StrategyMonitor, TreaderProfile, TradingList, Performance,
                      APPLog, Message, DownloadData, SaveExit]
        frame_names = ["DashboardLogin", "DashboardLogged", "StrategyMonitor", "TreaderProfile", "TradingList",
                       "Performance", "APPLog", "Message", "DownloadData", "SaveExit"]

        # init all frames:
        for Frame, name in zip(frame_objs, frame_names):
            frame = Frame(container, self)
            self.frames[name] = frame
            frame.grid(row=0, column=0, sticky="nsew")


















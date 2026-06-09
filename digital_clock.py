from tkinter import *
from tkinter.ttk import *
from time import strftime
from datetime import datetime

root = Tk()
root.title("Digital Clock")

window_width = 480
window_height = 220
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

root.configure(bg="#111111")
root.resizable(False, False)
root.overrideredirect(True)

BG = "#111111"
TEXT_COLOR = "#00FF66"

DAYS_VI = ["Thứ Hai", "Thứ Ba", "Thứ Tư", "Thứ Năm", "Thứ Sáu", "Thứ Bảy", "Chủ Nhật"]
MONTHS_VI = ["", "tháng 1", "tháng 2", "tháng 3", "tháng 4", "tháng 5",
             "tháng 6", "tháng 7", "tháng 8", "tháng 9", "tháng 10", "tháng 11", "tháng 12"]

is_24h = True
blink_on = False
show_colon = True

def update_time():
    global show_colon
    now = datetime.now()
    h = now.hour
    suffix = ""
    if not is_24h:
        suffix = " AM" if h < 12 else " PM"
        h = h % 12 or 12
    sep = ":" if (not blink_on or show_colon) else " "
    show_colon = not show_colon
    time_label.config(text=f"{h:02}:{now.minute:02}:{now.second:02}{suffix}")
    time_label.config(text=f"{h:02}{sep}{now.minute:02}{sep}{now.second:02}{suffix}")
    day_idx = now.weekday()
    date_label.config(text=f"{DAYS_VI[day_idx]}, {now.day} {MONTHS_VI[now.month]} {now.year}")
    root.after(1000, update_time)

def toggle_format():
    global is_24h
    is_24h = not is_24h
    btn_fmt.config(text="24h" if is_24h else "12h")

def toggle_blink():
    global blink_on
    blink_on = not blink_on
    btn_blink.config(text="Nháy: ON" if blink_on else "Nháy: OFF")

def start_drag(e):
    root._drag = (e.x, e.y)

def do_drag(e):
    root.geometry(f"+{root.winfo_x() + e.x - root._drag[0]}+{root.winfo_y() + e.y - root._drag[1]}")

root.bind("<ButtonPress-1>", start_drag)
root.bind("<B1-Motion>", do_drag)

time_label = Label(root, font=("Consolas", 52, "bold"), background=BG, foreground=TEXT_COLOR)
time_label.pack(pady=(20, 0))

date_label = Label(root, font=("Consolas", 13), background=BG, foreground="#666666")
date_label.pack()

btn_frame = Frame(root, style="TFrame")
btn_frame.pack(pady=8)

style = Style()
style.configure("TFrame", background=BG)
style.configure("Dark.TButton", background="#1a1a1a", foreground="#888888",
                font=("Consolas", 10), relief="flat", padding=(10, 4))

btn_fmt = Button(btn_frame, text="24h", style="Dark.TButton", command=toggle_format)
btn_fmt.pack(side=LEFT, padx=4)

btn_blink = Button(btn_frame, text="Nháy: OFF", style="Dark.TButton", command=toggle_blink)
btn_blink.pack(side=LEFT, padx=4)

btn_close = Button(btn_frame, text="✕", style="Dark.TButton", command=root.destroy)
btn_close.pack(side=LEFT, padx=4)

update_time()
root.mainloop()
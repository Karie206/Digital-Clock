from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Digital Clock")

# Tự động canh giữa cửa sổ trên màn hình máy tính
window_width = 450
window_height = 180
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)
root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")

root.configure(bg="#111111")
root.resizable(False, False) # Không cho phép thay đổi kích thước cửa sổ

def update_time():
    time_string = strftime("%H:%M:%S %p")
    time_label.config(text=time_string)
    
    # Định dạng Thứ, Ngày Tháng Năm (Tiếng Anh hoặc Tiếng Việt tùy bạn chỉnh)
    # %A: Thứ đầy đủ, %d: Ngày, %B: Tháng đầy đủ, %Y: Năm
    date_string = strftime("%A, %d %B %Y")
    date_label.config(text=date_string)
    
    time_label.after(1000, update_time)

main_frame = Frame(root, padding=15)
main_frame.pack(expand=True)

TEXT_COLOR = "#00FF66"  
BG_COLOR = "#111111"

time_label = Label(
    root, 
    font=("Digital-7", 55, "bold"), 
    background=BG_COLOR, 
    foreground=TEXT_COLOR
)

time_label.pack(anchor=CENTER, pady=(15, 0)) 

date_label = Label(
    root, 
    font=("Consolas", 14, "bold"), 
    background=BG_COLOR, 
    foreground="#888888"  
)
date_label.pack(anchor=CENTER, pady=(5, 15))

update_time()

root.mainloop()
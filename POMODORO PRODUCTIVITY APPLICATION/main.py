import math
from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
TIME = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    global TIME,reps
    window.after_cancel(TIME)
    canvas.itemconfig(timer_text,text='00:00')
    reps = 1
    Timer.config(text="TIMER")
    check_mark.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 2 != 0:  # Odd reps (1, 3, 5, ...) -> Work time
        count_down(work_sec)
        Timer.config(text="WORK")
    elif reps % 2 == 0 and reps % 9 != 0:  # Even reps (2, 4, 6, ...) -> Short break
        count_down(short_break_sec)
        Timer.config(text="SHORT BREAK",fg = YELLOW)
    else:  # Every 9th rep -> Long break
        count_down(long_break_sec)
        Timer.config(text= "LONG BREAK",fg = RED)


    reps += 1  # Increment the reps counter


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec<10:
        count_sec = f"{count_sec:02}" # Using f-string

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        global TIME
        TIME = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("pomodoro")
window.config(padx=100,pady=50, bg=PINK)


canvas = Canvas(width=200, height=224, bg=PINK, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100,130,text="00:00",fill="white", font=(FONT_NAME, 35,"bold"))
canvas.pack()
canvas.grid(column=1,row=1)


Timer =Label(text="TIMER",font=(FONT_NAME, 35,"bold"))
Timer.config(fg=GREEN,bg=PINK)
Timer.grid(column=1,row=0)
start = Button(text="Start",highlightthickness=0,command=start_timer)
start.grid(column=0,row=2)
reset = Button(text="Reset",highlightthickness=0,command=reset_time)
reset.grid(column=2,row=2)
check_mark = Label(text="")
check_mark.config(fg=GREEN,bg=PINK)
check_mark.grid(column = 1, row =3)









window.mainloop()
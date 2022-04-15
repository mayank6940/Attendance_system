from tkinter import *
import tkinter.messagebox as msg

def register():
    msg.showinfo("Sucess", "You are Register")

def Take_ads():
    msg.showinfo("Sucess", "Your Attendance is Taken")


app = Tk()
app.title("Attendance System")
app.geometry("900x700")
app.configure(bg = "#230c33")

attendance_img = PhotoImage(file='D:\\Python_DEV\\Advanced_python_harry\\attendance.png')
register_img = PhotoImage(file='D:\\Python_DEV\\Advanced_python_harry\\register.png')
take_btn = PhotoImage(file='D:\\Python_DEV\\Advanced_python_harry\\take_ad.png')

Label(app, image=attendance_img, bd=0,  bg = "#230c33").place(x = 130, y= 20)

main_win = Frame(app,  bg = "#9D75CB")
main_win.place(x=170, y=200, height=390, width=550)

register_btn = Button(main_win, text="Register", image=register_img,bg="#9D75CB", bd=0, command= register)
register_btn.place(x=200, y=100)

attendance_btn = Button(main_win,image=take_btn, bg="#9D75CB", bd = 0 , command= Take_ads)
attendance_btn.place(x=140, y=200)

#bg = "#aaffe5"


app.mainloop()
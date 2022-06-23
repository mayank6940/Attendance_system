from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from PIL import Image, ImageTk
import cv2
import mysql.connector
# from train_img import train 
import os
import numpy as np

# haarcascade_frontalface_default.xml

def test():
    msg.showinfo("sucess", "run it",parent= apk)


def student_page(self):
    global apk
    apk = Toplevel(app)
    apk.title("Face_Recogniser")
    apk.geometry("1366x768")

    reco_img = Image.open(r'D:\Python_DEV\Advanced_python_harry\reco.jpg')
    reco_img = reco_img.resize((1366, 800), Image.ANTIALIAS)
    reco_bg = ImageTk.PhotoImage(reco_img)

    bg_lbl = Label(apk, image=reco_bg,text="hello")
    bg_lbl.place(x = 0 , y = 0, height=800, width=1366)

    detect = Button(bg_lbl,text="Detect", bd= 0, command=test)
    detect.place(x = 600, y = 550)

    apk.mainloop()



def take_a_photo():
    if dep_c.get() == "Select Department" or student_n.get() == "" or student_r == "":

        msg.showerror("Invalid", "All fields are required", parent=root)
    else:
        try:
            conn = mysql.connector.connect(host="localhost", user="root", password="M8757266773p@", database="attendancedb")
            my_cursor = conn.cursor()
            my_cursor.execute("select * from student")
            myresult = my_cursor.fetchall()
            id=0
            for x in myresult:
                id+=1
            my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semster=%s,Name=%s,Roll=%s,Email=%s,Gender=%s where Id=%s",(
                dep_c.get(),
                course_c.get(),
                year_C.get(),
                semster_c.get(),
                student_n.get(),
                student_r.get(),
                student_e.get(),
                student_g.get(),
                student_i.get()==id+1
                # ==id+1
                
        
            ))
            conn.commit()
            conn.close()

            face_classifier = cv2.CascadeClassifier(r"D:\Python_DEV\Advanced_python_harry\haarcascade_frontalface_default.xml")
            
            def face_crop(img):
                gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                faces = face_classifier.detectMultiScale(gray,1.3,5)

                for (x,y,w,h) in faces:
                    face_crop = img[y:y+h,x:x+w]
                    return face_crop
            cap = cv2.VideoCapture(0)
            img_id = 0
            while True:
                ret, my_frame = cap.read()
                if face_crop(my_frame) is not None:
                    img_id+=1
                face = cv2.resize(my_frame,(0,0),None,0.25,0.25)
                # face = cv2.resize(face_crop(my_frame),(0,0),None,0.25,0.25)
                face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                # file_name_path ="D:\\Python_DEV\\Advanced_python_harry\\data\\" +str(student_n)+"."+str(img_id)+".jpg"
                # file_name_path ="D:\\Python_DEV\\Advanced_python_harry\\data\\"+str(student_n.get())+"."+str(id)+str(".") +str(img_id)+".jpg"
                file_name_path =r"D:\Python_DEV\Advanced_python_harry\data\data."+str(id)+str(".") +str(img_id)+".jpg"

                # cv2.imwrite("D:\\Python_DEV\\Advanced_python_harry\\data\\user.jpg",face)
                cv2.imwrite(file_name_path,face)

                # cv2.putText(face,str(img_id),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                cv2.imshow("Crop Faces",my_frame)

                if cv2.waitKey(1)==13 or int(img_id)==20:
                    break
            cap.release()
            cv2.destroyAllWindows()
            msg.showinfo("Success","Data set has been completed")



        except Exception as es:
            msg.showerror("Error", f"Due to: {str(es)}", parent=root)



def Done():
    if dep_c.get() == "Select Department" or student_n.get() == "" or student_r == "":
        msg.showerror("Invalid", "All fields are required", parent=root)
    else:
        try:
            conn = mysql.connector.connect(

                host="localhost", user="root", password="M8757266773p@", database="attendancedb")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                dep_c.get(),
                course_c.get(),
                year_C.get(),
                semster_c.get(),
                student_n.get(),
                student_r.get(),
                student_e.get(),
                student_g.get(),
                student_i.get()
                


            ))
            conn.commit()
            conn.close()
            msg.showinfo("Success", f"Your data has been saved {student_n.get()}", parent=root)
        except Exception as es:
            msg.showerror("Error", f"Due to: {str(es)}", parent=root)


def register():
    global root
    root = Toplevel(app)
    root.geometry("1366x768")
    root.title("Student Register Page")
    root.configure(bg="grey")
    # root.configure(bg = "#1D5C63")
    # root.resizable(False,False)
    

    # =========variables=======================

    global dep_c
    global course_c
    global year_C
    global semster_c
    global student_e
    global student_r
    global student_g
    global student_n
    global student_i

    dep_c = StringVar()
    course_c = StringVar()
    year_C = StringVar()
    semster_c = StringVar()
    student_n = StringVar()
    student_e = StringVar()
    student_g = StringVar()
    student_r = StringVar()
    student_i = StringVar()

    # =================main_frame stART==========

    main_frame = Label(root, image=bg)
    main_frame.place(x=0, y=0)

    screen_lb = LabelFrame(main_frame, text="Student Details", font="Verdana 20 bold", relief=RIDGE, bg="#EEEEEE")
    screen_lb.place(x=270, y=90, width=850, height=500)

    current_course = LabelFrame(screen_lb, text="Current Courser Information", font="Verdana 10 bold", bd=3)
    current_course.place(x=20, y=10, width=800, height=140)

    dep_lb = Label(current_course, text="Department", font="Verdana 10 bold")
    dep_lb.grid(row=0, column=0, padx=10, pady=15)

    dep_combo = ttk.Combobox(current_course, textvariable=dep_c, font="Verdana 8 bold", width=18, state="readonly")
    dep_combo["values"] = ("Select Department", "Computer Science", "IT", "ECE", "Civil", "Mechanical")
    dep_combo.current(0)
    dep_combo.grid(row=0, column=1)

    course_lb = Label(current_course, text="Courses", font="Verdana 10 bold")
    course_lb.grid(row=0, column=2, padx=170, pady=15)

    course_combo = ttk.Combobox(current_course, textvariable=course_c, font="Verdana 8 bold", width=18,
                                state="readonly")
    course_combo["values"] = (
        "Select Course", "Bachelor In Engineering (B.E)", "Master In Engineering (M.E)", "Ph.D Program")
    course_combo.current(0)
    course_combo.place(x=550, y=16)

    year_lb = Label(current_course, text="Year", font="Verdana 10 bold")
    year_lb.grid(row=1, column=0, padx=10, pady=15)

    year_combo = ttk.Combobox(current_course, textvariable=year_C, font="Verdana 8 bold", width=18, state="readonly")
    year_combo["values"] = ("Select Year", "2018", "2019", "2020", "2021", "2022")
    year_combo.current(0)
    year_combo.grid(row=1, column=1)

    semster_lb = Label(current_course, text="Semster", font="Verdana 10 bold")
    semster_lb.place(x=450, y=65)

    semster_combo = ttk.Combobox(current_course, textvariable=semster_c, font="Verdana 8 bold", width=18,
                                 state="readonly")
    semster_combo["values"] = (
        "Select Semster", "Semster - 1", "Semster - 2", "Semster - 3", "Semster - 4", "Semster - 5", "Semster - 6",
        "Semster - 7", "Semster - 8")
    semster_combo.current(0)
    semster_combo.place(x=550, y=65)

    student_info = LabelFrame(screen_lb, text="Student Information", font="Verdana 10 bold", bd=3)
    student_info.place(x=20, y=170, width=800, height=260)

    student_name = Label(student_info, text="Name :", font="Verdana 11 bold")
    student_name.grid(row=0, column=0, padx=13, pady=13)

    student_name_entry = ttk.Entry(student_info, textvariable=student_n, font="Verdana 10 bold")
    student_name_entry.grid(row=0, column=1)

    student_roll = Label(student_info, text="Roll No  - ", font="Verdana 11 bold")
    student_roll.grid(row=0, column=2, padx=180, pady=13)

    student_roll_entry = ttk.Entry(student_info, textvariable=student_r, font="Verdana 10 bold")
    student_roll_entry.place(x=550, y=13)

    student_email = Label(student_info, text="Email :", font="Verdana 11 bold")
    student_email.place(x=14, y=60)

    student_email_entry = ttk.Entry(student_info, textvariable=student_e, font="Verdana 10 bold")
    student_email_entry.place(x=90, y=60)

    student_gender = Label(student_info, text="Gender :", font="Verdana 11 bold")
    student_gender.place(x=459, y=60)

    student_gender_combo = ttk.Combobox(student_info, textvariable=student_g, font="Verdana 10 bold", state="readonly")
    student_gender_combo["values"] = ("Select Gender", "Male", "Female")
    student_gender_combo.current(0)
    student_gender_combo.place(x=550, y=60)

    student_id = Label(student_info,text="StudentID :",font="Verdana 10 bold")
    student_id.place(x = 14, y = 110)

    student_id_entry = ttk.Entry(student_info, textvariable=student_i,font="Verdana 11 bold")
    student_id_entry.place(x = 110, y = 110, height= 22, width= 170)

    done_btn = ttk.Button(student_info, text="Submit", command=Done)
    done_btn.place(x=350, y=110, width=90, height=40)

    # reset_btn = ttk.Button(student_info, text="Reset", command= reset)
    # reset_btn.place(x=490, y=130, width=90, height=40)

    photo_btn = ttk.Button(student_info, text="Take Photo Sample", command=take_a_photo)
    photo_btn.place(x=100, y=190, width=120, height=40)

    update_btn = ttk.Button(student_info, text="Update Photo Sample")
    update_btn.place(x=580, y=190, width=125, height=40)



def train_classifier():
    data_dir = (r"D:\Python_DEV\Advanced_python_harry\data")
    path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

    faces = []
    ids = []

    for image in path:
        img = Image.open(image).convert('L')
        imgNP = np.array(img, 'uint8')
        id = int(os.path.split(image)[1].split('.')[1])

        faces.append(imgNP)
        ids.append(id)
        cv2.imshow("Tranning", imgNP)
        cv2.waitKey(1) == 13
        # ids = np.array(ids)
    ids = np.array(ids)

    trn = cv2.face.LBPHFaceRecognizer_create()
    trn.train(faces, ids)
    trn.write(r"D:\Python_DEV\Advanced_python_harry\classifier.xml")
    cv2.destroyAllWindows()
    msg.showinfo("Sucess", "Your data has been trannied")





def teacher_login():
    maya = Toplevel(app)
    maya.title("Train Data")
    maya.geometry("1366x768")
    # maya.configure(bg= "blue")
    Frame1_img = Image.open(r'D:\Python_DEV\Advanced_python_harry\frame1.jpg')
    Frame1_img = Frame1_img.resize((700, 750), Image.ANTIALIAS)
    Frame1_bg = ImageTk.PhotoImage(Frame1_img)

    Frame2_img = Image.open(r'D:\Temp_Down\frame2.jpg')
    Frame2_img = Frame2_img.resize((700, 750), Image.ANTIALIAS)
    Frame2_bg = ImageTk.PhotoImage(Frame2_img)

    # head_right = Image.open(r'D:\Python_DEV\Advanced_python_harry\right.png')
    # Frame2_img = Frame2_img.resize((700, 750), Image.ANTIALIAS)
    # Frame2_bg = ImageTk.PhotoImage(Frame2_img)


    fram1 = Frame(maya,bd=0)
    fram1.place(x = 0, y= 0, height= 750, width= 670)

    bg_lbl1 = Label(fram1, image=Frame1_bg,bd=0)
    bg_lbl1.place(x = 0,y=0)

    right_head = PhotoImage(file=r'D:\Python_DEV\Advanced_python_harry\right.png')

    right_lbl = Label(bg_lbl1, image=right_head,bd=0,bg="#54ADD7")
    right_lbl.place(x = 50, y = 50)


    fram2 = Frame(maya,bd=0)
    fram2.place(x = 670,y= 0,height= 750, width= 700)

    bg_lbl2 = Label(fram2, image=Frame2_bg,bd=0)
    bg_lbl2.place(x = 0,y=0)

    left_head = PhotoImage(file=r'D:\Python_DEV\Advanced_python_harry\left.png')

    left_lbl = Label(bg_lbl2, image=left_head,bg="#000000")
    left_lbl.place(x = 10, y = 40)

    train_btn_img = PhotoImage(file=r'D:\Python_DEV\Advanced_python_harry\train.png')
    train_img = Image.open(r'D:\Python_DEV\Advanced_python_harry\train1.jpeg')
    train_img = train_img.resize((100, 100), Image.ANTIALIAS)
    train_bg = ImageTk.PhotoImage(train_img)

    train_btn = Button(fram2,image=train_btn_img,bd=0, bg="#000000",command=train_classifier)
    train_btn.place(x = 210, y= 540)
    maya.mainloop()


    


    # def train_classifier():
    #     data_dir = (r"D:\Python_DEV\Advanced_python_harry\data")
    #     path = [os.path.join(data_dir,file) for file in os.listdir(data_dir)]

    #     faces = []
    #     ids = []

    #     for image in path:
    #         img = Image.open(image).convert('L')
    #         imgNP = np.array(img, 'uint8')
    #         id = int(os.path.split(image)[1].split('.')[1])

    #         faces.append(imgNP)
    #         ids.append(id)
    #         cv2.imshow("Tranning", imgNP)
    #         cv2.waitKey(1) == 13
    #     # ids = np.array(ids)
    #     ids = np.array(ids)

    #     trn = cv2.face.LBPHFaceRecognizer_create()
    #     trn.train(faces, ids)
    #     trn.write(r"D:\Python_DEV\Advanced_python_harry\classifier.xml")
    #     cv2.destroyAllWindows()
    #     msg.showinfo("Sucess", "Your data has been trannied")












def first_page():
    global app
    global bg

    app = Tk()
    app.title("Attendance System Software")
    app.geometry("1366x768")
    # app.state('zoomed')
    # app.resizable(False, False)

    # ....................................Images..............................................
    attendance_img = PhotoImage(file=r'D:\Python_DEV\Advanced_python_harry\attendance.png')

    # register_img = PhotoImage(file='D:\\Python_DEV\\Advanced_python_harry\\register.png')
    # take_btn = PhotoImage(file='D:\\Python_DEV\\Advanced_python_harry\\take_ad.png')

    student_img = Image.open(r'D:\Temp_Down\Download_new\student.png')
    student_img = student_img.resize((300, 170), Image.ANTIALIAS)
    student = ImageTk.PhotoImage(student_img)

    teacher_img = Image.open(r'D:\Temp_Down\Download_new\teacherleft2.jpg')
    teacher_img = teacher_img.resize((300, 170), Image.ANTIALIAS)
    teacher = ImageTk.PhotoImage(teacher_img)

    bg_img = Image.open(r'D:\Temp_Down\Download_new\bg.jpg')
    bg_img = bg_img.resize((1366, 768), Image.ANTIALIAS)
    bg = ImageTk.PhotoImage(bg_img)

    register_img = Image.open(r'D:\Temp_Down\Download_new\register2.jpg')
    register_img = register_img.resize((300, 170), Image.ANTIALIAS)
    register_i = ImageTk.PhotoImage(register_img)

    # ......................................image__closed........................................

    bg_screen = Label(app, image=bg,bd=0)
    bg_screen.place(x=0, y=0)

    heading = Label(bg_screen, image=attendance_img, bg="#230c33")
    heading.place(x=350, y=30)

    student_btn = Button(bg_screen, image=student, bd=0, bg="#230c33", cursor="hand2",command=student_page)
    student_btn.place(x=50, y=150)

    student_btn_1 = Button(bg_screen, text="Student Login", font="Impact 23 ", fg="gray", bg="#EEEEEE", cursor="hand2")
    student_btn_1.place(x=50, y=335, width=300, height=50)

    teacher_btn = Button(bg_screen, image=teacher, bd=0, cursor="hand2", bg="#230c33", command=teacher_login)
    teacher_btn.place(x=550, y=150)

    teacher_btn_1 = Button(bg_screen, text="Teacher Login", font="Impact 23 ", fg="gray", bg="#EEEEEE", cursor="hand2",
                           command=teacher_login)
    teacher_btn_1.place(x=550, y=335, width=300, height=50)

    register_btn = Button(bg_screen, image=register_i, bd=0, cursor="hand2", bg="#230c33", command=register)
    register_btn.place(x=1000, y=150)

    register_btn_1 = Button(bg_screen, text="Register Here", font="Impact 23 ", fg="gray", bg="#EEEEEE", cursor="hand2",
                            command=register)
    register_btn_1.place(x=1000, y=335, width=300, height=50)

    app.mainloop()


first_page()

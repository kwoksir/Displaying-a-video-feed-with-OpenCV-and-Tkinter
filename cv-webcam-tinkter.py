# Import required Libraries
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import cv2
from cvzone import *

cap= cv2.VideoCapture()
cap.open(0,cv2.CAP_DSHOW)
cap.set(3,640)
cap.set(4,480)

def leave():
    cap.release()
    win.after_cancel(after_id)
    win.destroy()

def confirm():
    r = messagebox.askyesno("Quit", "Do you want to quit?")
    if r :
        leave()
    else:
        pass

win = Tk()
win.geometry("1280x600+100+100")
win.pack_propagate(False)

menubar = Menu(win, tearoff=0)
win.config(menu = menubar)

file_menu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "File", menu= file_menu)
file_menu.add_command(label = "New")
file_menu.add_separator()

sub_menu = Menu(file_menu, tearoff = 0)
sub_menu.add_command(label="Option 1")
sub_menu.add_command(label="Option 2")

file_menu.add_cascade(label = "More Option ", menu=sub_menu)
file_menu.add_command(label = "Quit" ,command=confirm)

label =Label(win)
label.pack()
btn = Button(win, text="Close", width=20, font=("Cambria",18), command=confirm)
btn.pack()


# Define function to show frame
def show_frames():
   global after_id
   # Get the latest frame and convert into Image
   _, cap_frame = cap.read()
   cv2image= cv2.cvtColor(cap_frame, cv2.COLOR_BGR2RGB)
   cv2gray = cv2.cvtColor(cv2image, cv2.COLOR_RGB2GRAY)
   imgList = [cv2image, cv2gray]
   imgStacked = stackImages(imgList, 2, 1)
   img = Image.fromarray(imgStacked)

   # Convert image to PhotoImage
   imgtk = ImageTk.PhotoImage(image = img)
   label.imgtk = imgtk
   label.configure(image=imgtk)

   # Repeat after an interval to capture continiously
   after_id = win.after(10, show_frames)

show_frames()
win.protocol('WM_DELETE_WINDOW', leave)
win.mainloop()

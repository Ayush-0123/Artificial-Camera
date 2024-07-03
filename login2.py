from tkinter import*
from PIL import Image
from record import record
from color import color
from face import face
from motion import motion
from find_motion import find_motion
from objectd import objectd
from depth import depth
lin=Tk()
lin.config(bg="sky blue")
lin.geometry("570x450")
lin.title("Welcome to the main page")
la=Label(lin,text="ARTIFICAL CAMERA",bg="sky blue",font=100).place(x=210,y=5)
#photo
photo=PhotoImage(file='rec.png')
photoimag = photo.subsample(6,6)
la1=Label(lin,image=photoimag).place(x=200,y=35)
    
Record=Button(lin,text="Record",width=20,bd=10,relief="raised",font=20,command=record).place(x=5,y=210)
Color=Button(lin,text="Color Detect",width=20,bd=10,relief="raised",font=20,command=color).place(x=300,y=210)           
Detect=Button(lin,text="Detect",width=20,bd=10,relief="raised",font=20,command=face).place(x=5,y=270)
Motion=Button(lin,text="Motion sound",width=20,bd=10,relief="raised",font=20,command=motion).place(x=300,y=270)
find=Button(lin,text="Identify",width=20,bd=10,relief="raised",font=20,command=find_motion).place(x=5,y=330)
Measurement=Button(lin,text="Depth",width=20,bd=10,relief="raised",font=20,command=depth).place(x=300,y=330)
Object=Button(lin,text="Object detection",width=20,bd=10,relief="raised",font=20,command=objectd).place(x=5,y=390)
Exit=Button(lin,text="Exit",width=20,bd=10,relief="raised",font=20,command=lin.destroy).place(x=300,y=390)
lin.mainloop()

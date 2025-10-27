from tkinter import *
from tkinter import messagebox
root=Tk()
root.title("Image Uploader")
root.geometry("500x500")
root.configure(background="blue")

lable_uploadimage=Label(root, text="Upload image : ", bg="blue")
lable_uploadimage_name=Label(root,font=("courier",50,"bold"),bg="blue")
lable_uploadimage_image=Label(root,bg="gold",highlightthickness=5,borderwidth=2,relief=SOLID)
lable_uploadimage_=Label(root,font=("courier",10,"bold"),bg="lightblue")

def IGTec():
    messagebox.showinfo("This website will let you upload any image.")
   


lable_uploadimage.place(relx=0.2,rely=0.1, anchor=CENTER)
lable_uploadimage_name.place(relx=0.5,rely=0.25,anchor=CENTER)
lable_uploadimage_image.place(relx=0.5,rely=0.5,anchor=CENTER)
lable_uploadimage_.place(relx=0.5, rely=0.9, anchor=CENTER)
btn=Button( command=IGTec)
btn.place(relx=0.5,rely=0.18, anchor=CENTER)

root.mainloop()

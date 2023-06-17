import pyshorteners
import pyperclip
from tkinter import *
root=Tk()
root.title("URL Shortener")
root.geometry("600x300")
a=StringVar()
Label(root,text="Enter your URL: ").grid(row=1,column=0,sticky=W)
Entry(root,textvariable=a).grid(row=1,column=1,sticky=W)
c=""
def shorturl():
    b=a.get()
    s=pyshorteners.Shortener()
    #print("Your shortened URL: ",s.tinyurl.short(a))
    c=s.tinyurl.short(b)
    Label(root,text=c).grid(row=2,column=1,sticky=W)
    def copy():
        pyperclip.copy(c)
    Button(root,text="Copy URL",command=copy).grid(row=2,column=2)

Button(root,text="Shorten",command=shorturl).grid(row=1,column=2)

root.mainloop()
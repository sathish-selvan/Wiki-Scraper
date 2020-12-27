import wikipedia

from tkinter import *
from tkinter import scrolledtext

root = Tk()
root.title("Wiki APi")
root.geometry("430x600")

def wiki_search(data):
    try:
        my_lable.config(text="Searching results for : {}".format(data))
        
        passage=wikipedia.summary(data)
        print(passage)
        text_area.delete(0.0,END)
        text_area.insert(INSERT,passage)
        text_area.update_idletasks()
    except:
        #print("does not match any pages")
        my_lable.config(text="does not match any pages")

search = StringVar()


Entry(root,textvariable=search,width="60").grid(row = 0, column=0,pady=10,ipady=3)
my_lable=Label(root,width="60",height="2",cursor="dot",font=("Times New Roman",15))
my_lable.grid(row=1,column=0,pady=2)
text_area = scrolledtext.ScrolledText(root,width ="40",height="20",font=("Times New Roman",15),relief =SUNKEN,wrap=WORD)
text_area.place(x=10,y=95)
Button(root,text="Search",width="20",bg="white",fg="red",command=lambda:wiki_search(search.get())).place(x=143,y=550)

root.mainloop()
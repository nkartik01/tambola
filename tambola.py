import tkinter as tk
import random
import tkinter.font as tkFont
def generate_number():
    if len(pending)>0:
        r=random.randint(0,len(pending)-1)
        a=pending.pop(r)
        number_label.config(text=a)
        buttons[(a-1)//10][(a-1)%10].config(bg="red")
        if len(call_list)>=10:
            call_list.pop(0)
        call_list.append(a)
        s=''
        for i in call_list:
            s+=str(i)+'  '
        call_list_label.config(text=s)
def destroy1():
    for slave in root.grid_slaves():
        slave.destroy()

def refresh():
    global root
    global h
    global number_label
    global buttons
    global call_list
    call_list=[]
    global call_list_label
    try:
        destroy1()
    except:
        pass
    
    global pending
    pending=[]
    print(w)
    for i in range(1,91):
        pending.append(i)
    buttons=[]
    for i in range(9):
        q=[]
        for j in range(1,11):
            if i==0 and j!=10:
                q.append(tk.Button(root,text=' '+str((10*i)+j)+' ',bg="blue",font=tkFont.Font(family="Lucida Grande", size=round(w*35/1920)),fg='white'))
            else:
                q.append(tk.Button(root,text=str((10*i)+j),bg="blue",font=tkFont.Font(family="Lucida Grande", size=round(w*35/1920)),fg='white'))
            q[j-1].grid(row=i+1,column=j)
        buttons.append(q)
    next_button=tk.Button(root,text="Get Next Number",command=generate_number,font=tkFont.Font(family="Lucida Grande", size=round(w*35/1920)))
    next_button.grid(rowspan=2,column=11,row=8)
    refresh_button=tk.Button(root,text="Refresh",command=refresh,font=tkFont.Font(family="Lucida Grande", size=round(w*35/1920)))
    refresh_button.grid(rowspan=2,column=11,row=6)
    number_label=tk.Label(root,text="",font=tkFont.Font(family="Lucida Grande", size=round(w*35/1920)),bg="green",fg="white")
    number_label.grid(row=3,rowspan=3,column=11)
    call_list_label=tk.Label(root,text='',font=tkFont.Font(family="Lucida Grande", size=round(w*35/1920)),bg="green",fg="white")
    call_list_label.grid(row=11,column=1,columnspan=20,rowspan=2)
root=tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))    
refresh()
root.mainloop()

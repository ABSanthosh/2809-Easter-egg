import tkinter as tk 
from tkinter import*
import random


top = tk.Tk()
top.title("Guess the password")

password='wholetthecatsout'
lucky_number=9
labellist = []
sp_chars = ['!','@','#','$','%','^','&','*','(',')','_','-','+','=','~','`','/','}']

lab_pos_x=133
lab_pos_y=160

ee_label=Label(top,text='0',bg='black',fg='white',font=('Bahnschrift',18))
ee_label.place(x=925,y=460)

def dare_window():
    dare = tk.Toplevel()
    dare.title("Dare time!")

    quote = Label(dare,text='"Actions have consequences bro"',bg='black',fg='white',font=('Bahnschrift',18))
    quote.place(x=90,y=40)
   

    quote_sub = Label(dare,text='- Ananya Duvvri',bg='black',fg='white',font=('',10,'italic'))
    quote_sub.place(x=350,y=80)

    uhoh = Label(dare,text="Uh-oh. You guessed it wrong, dumbo.",bg='black',fg='#ff6161',font=('Consolas',14,))
    uhoh.place(x=100,y=120)

    uhoh2 = Label(dare,text="You've earned yourself a dare!",bg='black',fg='#ff6161',font=('Consolas',14))
    uhoh2.place(x=125,y=148)

    evil = Label(dare,text="* EVIL LAUGHTER *",bg='black',fg='#ff6161',font=('courier new',24,'italic'))
    evil.place(x=110,y=215)

    def quit_dare():
        dare.destroy()

    die = Button(dare,text='Click to die',command=quit_dare,fg='black',font=('Bahnschrift',8),bd=5)
    die.place(x=225,y=280)
    


    #dare.overrideredirect(1)
    dare.config(background='black')
    dare.geometry('550x350')
    dare.resizable(False, False)
    dare.attributes('-topmost', 'true')
    dare.mainloop()

def qquit():
    top.destroy()

def win_window():
    win = tk.Toplevel()
    win.title("Yay!")

    quote = Label(win,text="Yayayay, you did it! \nNot so dumb you are, after all :p",bg='black',fg='#3366ff',font=('courier new',16,'italic'))
    quote.place(x=60,y=40)

    passwd_disp = Label(win,text='"wholetthecatsout" is the password.',bg='black',fg='#cccccc',font=('courier new',16,'italic'))
    passwd_disp.place(x=60,y=120)

    claim_button = Button(win,text="Close",command=qquit,width=15,font=("impact",18))
    claim_button.place(x=180,y=230)

    win.config(background='black')
    win.geometry('550x350')
    win.resizable(False, False)
    win.attributes('-topmost', 'true')
    win.mainloop()

def ee_browser():
    link='https://github.com/ABSanthosh/2809-Easter-egg'
    import webbrowser
    webbrowser.open(link)


def caps_window():
    caps = tk.Toplevel()
    caps.title("Ouch...")

    quote = Label(caps,text="Caps lock is on!\nTurn it off to continue",bg='black',fg='white',font=('courier new',26))
    quote.place(x=35,y=80)
    
    #caps.overrideredirect(1)
    caps.config(background='black')
    caps.geometry('550x250')
    caps.attributes('-topmost', 'true')
    caps.resizable(False, False)
    caps.mainloop()
    
def Easter_egg():
    ee = tk.Toplevel()
    ee.title("Easter egg time...")

    quote = Label(ee,text="Well, you have entered\nthe Developer's easter egg\n part!",bg='black',fg='white',font=('courier new',20))
    quote.place(x=73,y=50)

    claim_button = Button(ee,text="Wait what?",command=ee_browser,width=15,font=("impact",18))
    claim_button.place(x=180,y=180)

    #ee.overrideredirect(1)
    ee.config(background='black')
    ee.geometry('550x250')
    ee.attributes('-topmost', 'true')
    ee.resizable(False, False)
    ee.mainloop()   

def destroy_all():
    for widget in top.winfo_children():
        if isinstance(widget, tk.Toplevel):
            widget.destroy()

def shift_window():
    shift = tk.Toplevel()
    shift.title("Ouch...")

    quote = Label(shift,text="shift is being pressed!\nStop using shift key to continue",bg='black',fg='white',font=('courier new',20))
    quote.place(x=20,y=80)


    #shift.overrideredirect(1)
    shift.config(background='black')
    shift.geometry('550x250')
    shift.attributes('-topmost', 'true')
    shift.resizable(False, False)
    shift.mainloop()
    

shift_counter=[]



for i in range(len(password)):
    tex =sp_chars[i]
    buttonborder = Frame(top,height=48,width=48,highlightbackground="#ffffff",background="black",highlightcolor="#ffffff",highlightthickness=4,bd=0)
    l = Label(buttonborder,text=tex,bg='black',fg='white',width=2,height=1,font=('',22,'bold'))
    #l = Label(buttonborder,text=tex,bg='black',fg='white',width=2,height=1,font=('',22))
    l.place(x=0,y=0)
    labellist.append(l)
    buttonborder.place(x=lab_pos_x,y=lab_pos_y)
    lab_pos_x+=43

input_char_show_label = Label(top,text='',bg='black',fg='white',width=2,height=1,font=('Colonna MT',122))
input_char_show_label.place(x=375,y=260)

input_char_show_label_sub = Label(top,text="Guess a letter",bg='black',fg='#a3a3a3',height=1,font=('courier new',18, 'bold', 'italic'))
input_char_show_label_sub.place(x=365,y=445)


email_label = Label(top,text='merishonajaanu@gmail.com',bg='black',fg='#a3a3a3',height=1,font=('courier new',23,'italic'))
email_label.place(x=265,y=55)

password_checker=[]

def key_pressed(event):
    global password_checker, shift_counter,lucky_number
    
    destroy_all()
    try:
        top.shift.destroy()
    except:
        pass
    #print(type(event.keysym))
    if event.state ==10:
        caps_window()
    elif event.state==9:
        shift_window()
    else:
        pos_list=[]
        input_char_show_label.config(text=(event.char).capitalize())
        if (event.char in password.lower()) or (event.char in password.upper()):
            input_char_show_label.config(fg='#80ff66')
            for i in range(len(password)):
                if password[i]==event.char:
                    pos_list.append(i)

            for j in pos_list:
                labellist[j].config(text=(event.char).capitalize(),fg='#80ff66')
                if(event.char not in password_checker):
                    password_checker.append(event.char)
                    #print('1',password_checker,len(password_checker))
                    if len(password_checker)==10:
                        win_window()
                else: 
                    #print("2",password_checker,len(password_checker))
                    if len(password_checker)==10:
                        win_window()
                
        else:
            input_char_show_label.config(fg='#ff6161')
            dare_window()
            #win_window()
    if (event.keysym=="Shift_L" or event.keysym =="Shift_R" and (len(password_checker)<10)):    
        shift_counter.append("EE")
        ee_label.config(text=str(len(shift_counter)))
        if (len(shift_counter)==lucky_number) and (len(password_checker)==10):
            ee_label.config(fg="#41e066")
            destroy_all()
            Easter_egg()
            shift_counter=[]

top.bind('<Key>',key_pressed)
top.config(background='black')
top.geometry('960x500')
top.resizable(False, False)
top.mainloop()

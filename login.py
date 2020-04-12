#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 12, 2020 07:43:09 AM IST  platform: Linux

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import login_support
import symptom


def vp_start_login_gui():
    print("[x] Please Give Some Information \n")
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = main_win (root)
    login_support.init(root, top)
    root.mainloop()

w = None
def create_main_win(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_main_win(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = main_win (w)
    login_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_main_win():
    global w
    w.destroy()
    w = None


class main_win:
    def click(self):
        print("Name = ",self.name.get())
        print("Age = ",self.age.get())
        print("Email = ",self.email.get())
        print("Gender = ",self.gender.get())
        symptom.vp_start_symptom_gui()
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("500x300+402+128")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("AM I ILL")
        top.configure(highlightcolor="black")

        self.name_lb = tk.Label(top)
        self.name_lb.place(relx=0.06, rely=0.223, height=18, width=71)
        self.name_lb.configure(activebackground="#f9f9f9")
        self.name_lb.configure(text='''Name''')

        self.name = tk.Entry(top)
        self.name.place(relx=0.2, rely=0.223,height=19, relwidth=0.372)
        self.name.configure(background="white")
        self.name.configure(font="TkFixedFont")
        self.name.configure(selectbackground="#c4c4c4")

        self.age = tk.Entry(top)
        self.age.place(relx=0.7, rely=0.233,height=19, relwidth=0.152)
        self.age.configure(background="white")
        self.age.configure(font="TkFixedFont")
        self.age.configure(selectbackground="#c4c4c4")

        self.email = tk.Entry(top)
        self.email.place(relx=0.2, rely=0.333,height=19, relwidth=0.372)
        self.email.configure(background="white")
        self.email.configure(font="TkFixedFont")
        self.email.configure(selectbackground="#c4c4c4")

        self.age_lb = tk.Label(top)
        self.age_lb.place(relx=0.6, rely=0.233, height=21, width=38)
        self.age_lb.configure(activebackground="#f9f9f9")
        self.age_lb.configure(text='''Age''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.email_lb = tk.Label(top)
        self.email_lb.place(relx=0.08, rely=0.333, height=21, width=58)
        self.email_lb.configure(activebackground="#f9f9f9")
        self.email_lb.configure(text='''email id''')

        self.gender_lb = tk.Label(top)
        self.gender_lb.place(relx=0.6, rely=0.333, height=21, width=48)
        self.gender_lb.configure(activebackground="#f9f9f9")
        self.gender_lb.configure(text='''Gender''')

        
        self.gender = ttk.Combobox(top)
        self.gender.place(relx=0.7, rely=0.333, relheight=0.077
                , relwidth=0.164)
        self.gender['values']= ["Male","Female","Transgender"] 
        self.gender.current() 
        
        self.Button1 = tk.Button(top)
        self.Button1.place(relx=0.32, rely=0.467, height=27, width=121)
        self.Button1.configure(activebackground="#f9f9f9")
        self.Button1.configure(text='''Start''',command= self.click )

#if __name__ == '__main__':
#    vp_start_login_gui()





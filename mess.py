#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# Support module generated by PAGE version 5.0.3
#  in conjunction with Tcl version 8.6
#    Apr 12, 2020 07:43:05 AM IST  platform: Linux

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

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None
















def vp_start_symptom_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    #set_Tk_var()
    top = Toplevel1 (root)
    init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    set_Tk_var()
    top = Toplevel1 (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def submit(self):
        print(1,self.TCombobox1.get())
        print(2,self.TCombobox2.get())
        print(3,self.TCombobox3.get())
        print(4,self.TCombobox4.get())
        print(5,self.TCombobox5.get())
        print(6,self.TCombobox6.get())
        print(7,self.TCombobox7.get())
        print(8,self.TCombobox8.get())
        print(9,self.TCombobox9.get())
        print(10,self.TCombobox10.get())
        derived_values= [ self.TCombobox1.get() , self.TCombobox2.get() , self.TCombobox3.get() , self.TCombobox4.get() , self.TCombobox5.get() , self.TCombobox6.get() , self.TCombobox7.get() , self.TCombobox8.get() , self.TCombobox9.get() , self.TCombobox10.get() ]
        
        #print(derived_values)
        
        query_fun(derived_values)
        
        destroy_window()
        
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        
        lis=["YOUR ANS","YES","MAY BE","NO"]
        
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("602x691+418+0")
        top.minsize(1, 1)
        top.maxsize(1351, 738)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(highlightcolor="black")

        self.CLOSE = tk.Button(top)
        self.CLOSE.place(relx=0.515, rely=0.854, height=29, width=68)
        self.CLOSE.configure(activebackground="#f9f9f9")
        self.CLOSE.configure(text='''CLOSE''',command=destroy_window)

        self.SUBMIT = tk.Button(top)
        self.SUBMIT.place(relx=0.731, rely=0.854, height=29, width=74)
        self.SUBMIT.configure(activebackground="#f9f9f9")
        self.SUBMIT.configure(text='''SUBMIT''',command=self.submit)

        self.INTRO = tk.Label(top)
        self.INTRO.place(relx=0.017, rely=0.014, height=28, width=576)
        self.INTRO.configure(activebackground="#f9f9f9")
        self.INTRO.configure(text='''INTRO''')

        self.Label_1 = tk.Label(top)
        self.Label_1.place(relx=0.017, rely=0.072, height=18, width=586)
        self.Label_1.configure(activebackground="#f9f9f9")
        self.Label_1.configure(text='''Symptom 1        Do you have fever''')

        self.Label_2 = tk.Label(top)
        self.Label_2.place(relx=0.017, rely=0.145, height=19, width=586)
        self.Label_2.configure(activebackground="#f9f9f9")
        self.Label_2.configure(text='''Symptom 2        Do you have Headache''')

        self.Label_3 = tk.Label(top)
        self.Label_3.place(relx=0.017, rely=0.217, height=19, width=586)
        self.Label_3.configure(activebackground="#f9f9f9")
        self.Label_3.configure(text='''Symptom 3        Do you have Diarrhea''')

        self.Label_4 = tk.Label(top)
        self.Label_4.place(relx=0.017, rely=0.289, height=18, width=586)
        self.Label_4.configure(activebackground="#f9f9f9")
        self.Label_4.configure(text='''Symptom 4        Do you have Dry-cough''')

        self.Label_5 = tk.Label(top)
        self.Label_5.place(relx=0.017, rely=0.362, height=18, width=586)
        self.Label_5.configure(activebackground="#f9f9f9")
        self.Label_5.configure(text='''Symptom 5       Do you have Lethargy(exhaustion)''')

        self.Label_6 = tk.Label(top)
        self.Label_6.place(relx=0.017, rely=0.434, height=19, width=586)
        self.Label_6.configure(activebackground="#f9f9f9")
        self.Label_6.configure(text='''Symptom 6       Do you have Body pain''')

        self.Label_7 = tk.Label(top)
        self.Label_7.place(relx=0.017, rely=0.507, height=19, width=586)
        self.Label_7.configure(activebackground="#f9f9f9")
        self.Label_7.configure(text='''Symptom 7       Do you have vomiting''')

        self.Label_8 = tk.Label(top)
        self.Label_8.place(relx=0.017, rely=0.579, height=18, width=586)
        self.Label_8.configure(activebackground="#f9f9f9")
        self.Label_8.configure(text='''Symptom 8       Do you have sweating''')

        self.Label_9 = tk.Label(top)
        self.Label_9.place(relx=0.0, rely=0.651, height=18, width=596)
        self.Label_9.configure(activebackground="#f9f9f9")
        self.Label_9.configure(text='''Symptom 9       Do you have red eyes''')

        self.Label_10 = tk.Label(top)
        self.Label_10.place(relx=0.0, rely=0.724, height=19, width=596)
        self.Label_10.configure(activebackground="#f9f9f9")
        self.Label_10.configure(text='''Symptom 10       Do you have naueseaa''')

        self.TCombobox1 = ttk.Combobox(top)
        self.TCombobox1.place(relx=0.415, rely=0.101, relheight=0.026
                , relwidth=0.194)
        self.TCombobox1['values']= lis 
        self.TCombobox1.current(0) 

        self.TCombobox2 = ttk.Combobox(top)
        self.TCombobox2.place(relx=0.415, rely=0.174, relheight=0.027
                , relwidth=0.194)
        self.TCombobox2['values']= lis 
        self.TCombobox2.current(0) 

        self.TCombobox3 = ttk.Combobox(top)
        self.TCombobox3.place(relx=0.415, rely=0.246, relheight=0.026
                , relwidth=0.194)
        self.TCombobox3['values']= lis 
        self.TCombobox3.current(0) 

        self.TCombobox4 = ttk.Combobox(top)
        self.TCombobox4.place(relx=0.415, rely=0.318, relheight=0.026
                , relwidth=0.194)
        self.TCombobox4['values']= lis 
        self.TCombobox4.current(0) 

        self.TCombobox5 = ttk.Combobox(top)
        self.TCombobox5.place(relx=0.415, rely=0.391, relheight=0.027
                , relwidth=0.194)
        self.TCombobox5['values']= lis 
        self.TCombobox5.current(0) 

        self.TCombobox6 = ttk.Combobox(top)
        self.TCombobox6.place(relx=0.415, rely=0.463, relheight=0.027
                , relwidth=0.194)
        self.TCombobox6['values']= lis 
        self.TCombobox6.current(0) 

        self.TCombobox7 = ttk.Combobox(top)
        self.TCombobox7.place(relx=0.415, rely=0.535, relheight=0.026
                , relwidth=0.194)
        self.TCombobox7['values']= lis 
        self.TCombobox7.current(0) 

        self.TCombobox8 = ttk.Combobox(top)
        self.TCombobox8.place(relx=0.415, rely=0.608, relheight=0.026
                , relwidth=0.194)
        self.TCombobox8['values']= lis 
        self.TCombobox8.current(0) 

        self.TCombobox9 = ttk.Combobox(top)
        self.TCombobox9.place(relx=0.415, rely=0.68, relheight=0.027
                , relwidth=0.194)
        self.TCombobox9['values']= lis 
        self.TCombobox9.current(0) 

        self.TCombobox10 = ttk.Combobox(top)
        self.TCombobox10.place(relx=0.415, rely=0.753, relheight=0.027
                , relwidth=0.194)
        self.TCombobox10['values']= lis 
        self.TCombobox10.current(0) 


























def query_fun(answer_value):
    
    covid=0
    typhoid=0
    chicken_pox=0
    pneumonia=0
    influenza=0
    sars=0
    mers=0
    ebola=0
    malaria=0
    
    query1 = answer_value[0]
    query2 = answer_value[1]
    query3 = answer_value[2]
    query4 = answer_value[3]
    query5 = answer_value[4]
    query6 = answer_value[5]
    query7 = answer_value[6]
    query8 = answer_value[7]
    query9 = answer_value[8]
    query10 = answer_value[9]
    
    #print(query1,query2,query3,query4,query5,query6,query7,query8,query9,query10)
    
#------------------in case of fever
    if query1=='YES':
        covid += 1
        typhoid += 1
        chicken_pox += 1
        pneumonia += 1
        influenza += 1
        sars += 1
        mers += 1
        ebola += 1
        malaria +=1
    
    elif query1=='NO':
        covid -= 1
        typhoid -= 1
        chicken_pox -= 1
        pneumonia -= 1
        influenza -= 1
        sars -= 1
        mers -= 1
        ebola -= 1
        malaria -= 1

    if query1=='MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4

# ##-----------------------in case of headache

    if query2=='YES':
        covid += 1
        typhoid += 1
        chicken_pox += 1
        pneumonia -= 1
        influenza += 1
        sars += 1
        mers += 1
        ebola += 1
        malaria -=1

    elif query2=='NO':
        covid -= 1
        typhoid -= 1
        chicken_pox -= 1
        pneumonia += 1
        influenza -= 1
        sars -= 1
        mers -= 1
        ebola -= 1
        malaria += 1

    elif query2=='MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4


#----------------------- for Diarrhea

    if query3=='YES':
        covid += 1
        typhoid += 1
        chicken_pox += 1
        pneumonia += 1
        influenza -= 1
        sars -= 1
        mers += 1
        ebola -= 1
        malaria -=1

    elif query3=='NO':
        covid -= 1
        typhoid -= 1
        chicken_pox -= 1
        pneumonia -= 1
        influenza += 1
        sars += 1
        mers -= 1
        ebola += 1
        malaria += 1

    elif query3=='MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4

#---------------------------------------- for Dry-cough

    if query4=='YES':
        covid += 1
        typhoid += 1
        chicken_pox -= 1
        pneumonia += 1
        influenza += 1
        sars += 1
        mers += 1
        ebola += 1
        malaria -=1

    elif query4=='NO':
        covid -= 1
        typhoid -= 1
        chicken_pox += 1
        pneumonia -= 1
        influenza -= 1
        sars -= 1
        mers -= 1
        ebola -= 1
        malaria += 1

    elif query4=='MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4

# ------------------------------------------------for Lethargy(exhaustion)

    if query5=='YES':
        covid += 1
        typhoid -= 1
        chicken_pox += 1
        pneumonia -= 1
        influenza += 1
        sars -= 1
        mers -= 1
        ebola -= 1
        malaria -=1

    elif query5=='NO':
        covid -= 1
        typhoid += 1
        chicken_pox -= 1
        pneumonia += 1
        influenza -= 1
        sars += 1
        mers += 1
        ebola += 1
        malaria += 1

    elif query5=='MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4


#-------------------------------------------------------------------- for Body pain

    if query6=='YES':
        covid += 1
        typhoid += 1
        chicken_pox -= 1
        pneumonia -= 1
        influenza += 1
        sars -= 1
        mers -= 1
        ebola += 1
        malaria -=1

    elif query6=='NO':
        covid -= 1
        typhoid -= 1
        chicken_pox += 1
        pneumonia += 1
        influenza -= 1
        sars += 1
        mers += 1
        ebola -= 1
        malaria += 1

    elif query6=='MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4


# --------------------------for vomiting

    if query7=='YES':
        covid -= 1
        typhoid -= 1
        chicken_pox -= 1
        pneumonia += 1
        influenza += 1
        sars -= 1
        mers += 1
        ebola += 1
        malaria +=1

    elif query7=='NO':
        covid += 1
        typhoid += 1
        chicken_pox += 1
        pneumonia -= 1
        influenza -= 1
        sars += 1
        mers -= 1
        ebola -= 1
        malaria -= 1

    elif query7=='MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4

# ---------------------------for sweating

    if query8=='YES':
        covid -= 1
        typhoid += 1
        chicken_pox -= 1
        pneumonia -= 1
        influenza -= 1
        sars -= 1
        mers -= 1
        ebola -= 1
        malaria += 1

    elif query8=='NO':
        covid += 1
        typhoid -= 1
        chicken_pox += 1
        pneumonia += 1
        influenza += 1
        sars += 1
        mers += 1
        ebola += 1
        malaria -= 1

    elif query8=='MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4

#  ------------------------------------------for muscle aches
    #if query == 'YES':
        covid -= 1
        typhoid -= 1
        chicken_pox -= 1
        pneumonia -= 1
        influenza -= 1
        sars += 1
        mers -= 1
        ebola -= 1
        malaria -= 1

    #elif query == 'NO':
        covid += 1
        typhoid += 1
        chicken_pox += 1
        pneumonia += 1
        influenza += 1
        sars -= 1
        mers += 1
        ebola += 1
        malaria += 1

    #if query == 'MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4

# ------------------------------------------for difficulty

    #if query == 'YES':
        covid += 1
        typhoid -= 1
        chicken_pox -= 1
        pneumonia -= 1
        influenza -= 1
        sars += 1
        mers += 1
        ebola -= 1
        malaria -= 1

    #elif query == 'NO':
        covid -= 1
        typhoid += 1
        chicken_pox += 1
        pneumonia += 1
        influenza += 1
        sars -= 1
        mers -= 1
        ebola += 1
        malaria += 1

    #elif query == 'MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4

# ------------------------------for naueseaa

    if query10 == 'YES':
        covid -= 1
        typhoid -= 1
        chicken_pox -= 1
        pneumonia -= 1
        influenza -= 1
        sars -= 1
        mers += 1
        ebola -= 1
        malaria += 1

    elif query10 == 'NO':
        covid += 1
        typhoid += 1
        chicken_pox += 1
        pneumonia += 1
        influenza += 1
        sars += 1
        mers -= 1
        ebola += 1
        malaria -= 1

    elif query10 == 'MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4

# ------------------------------------in case of muscle pain

    #if query == 'YES':
        covid -= 1
        typhoid -= 1
        chicken_pox -= 1
        pneumonia -= 1
        influenza -= 1
        sars -= 1
        mers -= 1
        ebola += 1
        malaria += 1

    #elif query == 'NO':
        covid += 1
        typhoid += 1
        chicken_pox += 1
        pneumonia += 1
        influenza += 1
        sars += 1
        mers += 1
        ebola -= 1
        malaria -= 1

    #elif query == 'MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4


# -----------------------------in case of chills chills

    #if query == 'YES':
        covid -= 1
        typhoid -= 1
        chicken_pox -= 1
        pneumonia -= 1
        influenza -= 1
        sars -= 1
        mers -= 1
        ebola += 1
        malaria += 1

    #elif query == 'NO':
        covid += 1
        typhoid += 1
        chicken_pox += 1
        pneumonia += 1
        influenza += 1
        sars += 1
        mers += 1
        ebola -= 1
        malaria -= 1

    #elif query == 'MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4


#--------------------------- in case of red eYES

    if query9 == 'YES':
        covid -= 1
        typhoid -= 1
        chicken_pox -= 1
        pneumonia -= 1
        influenza -= 1
        sars -= 1
        mers -= 1
        ebola += 1
        malaria -= 1

    elif query9 == 'NO':
        covid += 1
        typhoid += 1
        chicken_pox += 1
        pneumonia += 1
        influenza += 1
        sars += 1
        mers += 1
        ebola -= 1
        malaria += 1

    elif query9 == 'MAY BE':
        covid += 0.4
        typhoid += 0.4
        chicken_pox += 0.4
        pneumonia += 0.4
        influenza += 0.4
        sars += 0.4
        mers += 0.4
        ebola += 0.4
        malaria += 0.4
         
            
            
            
    #--------------------------- Calculating the three highest possible diseases ----------------------#
    # The Highest Values will give the output as the disease name for example if covid-19 is max "Covid" can be printed 
    # which will be stored in the "Which_highest" variable which will intialized first as an empty string
    
    
    
    
    # ------------------------------------- NOTE ----------------------------------->
    # The values of the resulting string are stored in the string named as follows-->
    
    # Top Possible disease --> Which_highest
    
    # Second Possible disease --> Which_second_highest
    
    # Third Possible disease --> Which_third_highest
    
    Highest_valuesof_diseases = [7,6,4,4,4,5,7,8,7]
    
    # ----- values are assigned to the respective name(with first letter capital)
    
    Names = ["Covid", "Typhoid", "Chicken Pox", "Pneumonia", "Influenza", "Sars", "Mers", "Ebola", "Malaria"]
    Calculated_Values = [covid, typhoid, chicken_pox, pneumonia, influenza, sars, mers, ebola, malaria]
    
    Sizeof_List = len( Calculated_Values)
    
    Average_Values = []  # List of average values
    
    for i in range(0, Sizeof_List, +1):
        average = round((Calculated_Values[i] / Highest_valuesof_diseases[i] )* 100, 3)
        Average_Values.append(average)
    for i in Average_Values:
        print(i, end= " ")
    print()
    highest_possibility = 0
    temp = 0
    for i in range(0, len(Average_Values), +1):
        if(temp < Average_Values[i]):
            temp = Average_Values[i]
    highest_possibility = temp
    second_highest_possiblity = 0
    third_highest_possiblity = 0
    Which_highest = ""
    Which_second_highest = ""
    Which_third_highest = ""
    i = 0
    
    # ----------- Finding the Most Possible disease and store it's name in "Which_highest"
    for i in range(0, len(Average_Values), +1):   
        if(Average_Values[i] == highest_possibility):
            if(len(Which_highest) == 0): 
                Which_highest = Names[i]
            else:
                if(len(Which_second_highest) == 0):
                    Which_second_highest = Names[i]
                else:
                    if(len(Which_third_highest) == 0):
                        Which_third_highest = Names[i]
                        
                        
                        
    # ----------- Finding the Second most possible disease and store it's name in "Which_second_highest"
    Find_second_highest = []
    Find_second_names = []
    Temporary_second_highest = 0
    if(len(Which_second_highest) == 0):
        Find_second_names = Names.copy()
        Find_second_names.remove(Which_highest)
        for i in range(0, len(Average_Values), +1):
            if(Average_Values[i] == highest_possibility):
                continue
            Find_second_highest.append(Average_Values[i])
        another = 0
        Temporary_second_highest = max(Find_second_highest)
        for i in range(0,len(Find_second_names), +1):
            if(Find_second_highest[i] == Temporary_second_highest):
                if(len(Which_second_highest) == 0):
                    Which_second_highest = Find_second_names[i]
                else:
                    if(len(Which_third_highest) == 0):
                        Which_third_highest = Find_second_names[i]
                        

    # ----------- Finding third Possible disease and store it's name in "Which_third_highest"
    Find_third_names = []
    Find_third_highest = []
    if(len(Which_third_highest) == 0):
        for i in range(0, len(Find_second_names), +1):
            if(Find_second_names[i] == Which_second_highest):
                continue
            Find_third_names.append(Find_second_names[i])
        for i in range(0, len(Find_second_highest), +1):
            if(Find_second_highest[i] == Temporary_second_highest):
                continue
            Find_third_highest.append(Find_second_highest[i])
        Temporary_third_highest = max(Find_third_highest)
        for i in range(0,len(Find_third_names), +1):
            if (Find_third_highest[i] == Temporary_third_highest):
                Which_third_highest = Find_third_names[i]
                break















def vp_start_login_gui():
    print("[x] Please Give Some Information \n")
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = main_win (root)
    init(root, top)
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
    init(w, top, *args, **kwargs)
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
        vp_start_symptom_gui()
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































print("\n[x] Starting Self Diagnosis Software \n")
vp_start_login_gui()

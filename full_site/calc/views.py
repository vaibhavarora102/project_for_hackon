from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.POST
def home(request):
    return render(request, 'home.html')
def login(request):
    return render(request, 'login.html')

def privacy_policy(request):
    return render(request, 'privacy_policy.html')

def disclamer(request):
    return render(request, 'disclamer.html')
def login_sub(request):
    global name , email ,age
    name = ' ' + request.POST['name']
    email = ' ' + request.POST['email']
    age =' ' + request.POST['age']
    #gen =' ' + request.POST['gender']
    return render(request,'form.html',{'name':name,'age':age,'email':email})

def spl_submit(request):
    md = 0
    if 'YES' == request.POST['history'] :
        md += 1
    if 'YES' == request.POST['infected'] :
        md += 1
    if 'YES' == request.POST['chronic'] :
        md += 1
    if 'YES' == request.POST['breathing'] :
        md += 1
    if md <= 1 :
        return render(request,'result.html',{'name':name,'age':age,'email':email,'first':fir,'sec':sec,'third':thi})
    else :
        return render(request,'result_2.html')
    


def form_sub(request):
    sy_1 = request.POST['fever']
    sy_2 = request.POST['headache']
    sy_3 = request.POST['diarrhea']
    sy_4 = request.POST['dry_cough']
    sy_5 = request.POST['lethargy']
    sy_6 = request.POST['body_pain']
    sy_7 = request.POST['vomiting']
    sy_8 = request.POST['sweatingh']
    sy_9 = request.POST['red_eyes']
    sy_10 = request.POST['naueseaa']
    answer_value= [sy_1,sy_2,sy_3,sy_4,sy_5,sy_6,sy_7,sy_8,sy_9,sy_10]



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
    #second_highest_possiblity = 0
    #third_highest_possiblity = 0
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
        #another = 0
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
    global fir ,sec ,thi
    fir = Which_highest
    sec = Which_second_highest
    thi  = Which_third_highest




    if "Covid" in [Which_highest , Which_second_highest , Which_third_highest] :
        return render(request,'spl_covid.html',{'name':name,'age':age,'email':email})
    else:
        return render(request,'result.html',{'name':name,'age':age,'email':email,'first':fir,'sec':sec,'third':thi})
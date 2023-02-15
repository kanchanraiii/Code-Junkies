import tkinter as tk
import smtplib
from tkinter import messagebox
def bp():
    if int(e5.get())<=120 and int(ays.get())<=80:
        msg=tk.Tk()
        msg.geometry("300x200")
        msg.configure(bg="azure")
        msg.title("Patient report")
        msg1=tk.Label(msg,text="Optimal BP\n\n\nTo maintain this range make sure\nto lead a balnced lifestyle",bg="azure")
        msg1.place(x='45',y='5')
    elif (int(e5.get()) <=130 and int(e5.get())>=120) and int(ays.get())<=80:
        msg=tk.Tk()
        msg.geometry("300x200")
        msg.configure(bg="azure")
        msg.title("Patient report")
        msg1=tk.Label(msg,text="Slightly elevated blood pressure\nTime to lopk into your lifestyle\nAnd Probably consult a Doctor",bg='azure')
                      
        msg1.place(x='45',y='5')
        
    elif int(e5.get())>130 and int(ays.get())>80:
        msg=tk.Tk()
        msg.geometry("300x200")
        msg.configure(bg="azure")
        msg.title("Patient report")
        msg1=tk.Label(msg,text="High Blood Pressure\n\n\nAbove might be the symptoms of:\n hypertension,stress,\nchronic liver diseases and low potassium levels",bg='azure')
        msg1.place(x='35',y='10')

def heartrate():
    if int(e6.get())<=100 and int(e6.get())>=60:
        msg=tk.Tk()
        msg.geometry("300x200")
        msg.configure(bg="azure")
        msg.title("Patient report")
        msg1=tk.Label(msg,text="Optimal Heart Rate\n\n\nTo maintain this range make sure\n\n\nto lead a balnced lifestyle",bg="azure")
        msg1.place(x='45',y='5')
        
    else:
        msg=tk.Tk()
        msg.geometry("300x200")
        msg.configure(bg="azure")
        msg.title("Patient report")
        msg1=tk.Label(msg,text="Abnormal Heart Rate\n\nTime to consult your Doctor",bg="azure")
        msg1.place(x='65',y='15')
               
def sugar():
    if int(e7.get())>=120 and int(e7.get())<=140:
        msg=tk.Tk()
        msg.geometry("300x200")
        msg.configure(bg="azure")
        msg.title("Patient report")
        msg1=tk.Label(msg,text="Normal Sugar Level")
        msg1.place(x='45',y='5')
        
    elif int(e7.get())>140 and int(e7.get())<=160:
        msg=tk.Tk()
        msg.geometry("300x200")
        msg.configure(bg="azure")
        msg.title("Patient report")
        msg1=tk.Label(msg,text="Patient has impaired glucose levels\n\nsuch levels can be caused by :\n\n\n being overweight or obese,\n\n\n having a family history of diabetes,\n\n\n doing little physical activity,\n\n\n having high blood pressure or high cholesterol\n\n and gestational diabetes",bg="azure")
        msg1.place(x='45',y='5')
         
    elif int(e7.get())>200:
        msg=tk.Tk()
        msg.geometry("300x200")
        msg.configure(bg="azure")
        msg.title("Patient report")
        msg1=tk.Label(msg,text="The patient is diabetic\n\nDiabetes is caused by insufficient production of\n\n insulin due to underlying causes",bg='azure')
        msg1.place(x='35',y='5')
    elif int(e7.get())<70:
        msg=tk.Tk()
        msg.geometry("300x200")
        msg.configure(bg="azure")
        msg.title("Patient report")
        msg1=tk.Label(msg,text="The blood sugar levels are lower than usual\n\nPatient may have hypoglycemia caused by:\n\n high intake of insulin,\n\nnot eating enough carbs,\n\nalcohol consumption or physical activity",bg='azure')
        msg1.place(x='35',y='5')
        
            

def thyroid():
    if (int(t3_entry.get()<=180 and int(t3_entry.get()))>=60 and (int(t4_entry.get())<=2.3 and int(t4_entry.get()))>=0.9 and (int(tsh_entry.get())<=5 and int(tsh_entry.get()))>=0.5):
        msg=tk.Tk()
        msg.geometry("300x200")
        msg.configure(bg="azure")
        msg.title("Patient report")
        msg1=tk.Label(msg,text="Normal Thyroid Level")
        msg1.place(x='35',y='5')
    
        
        
    elif str(t3_entry.get()>180) or str(t4_entry.get()>2.3) or str(tsh_entry.get()<0.5):
        msg=tk.Tk()
        msg.geometry("300x200")
        msg.configure(bg="azure")
        msg.title("Patient report")
        msg1=tk.Label(msg,text="Thyroid levels differ from usual range\n\nIt may indicate hyperthyroidism which can be caused by\n\n: Toxic nodule,Toxic multinodular goiter,Graves\n\n\' disease,Sub-acute thyroiditis\n\n or Excessive Iodine ingestion",bg='azure')
        msg1.place(x='35',y='5')
        
                                       
                                                                 
                                                                 
        
    else:
        msg=tk.Tk()
        msg.geometry("300x200")
        msg.configure(bg="azure")
        msg.title("Patient report")
        msg1=tk.Label(msg,text="Thyroid levels differ from usual range\n\n\It may indicate hypothyroidism which can be caused by: thyroiditis\n\n\n,surgical or radiation treatment of\n\n\n hyperthyroidism or iodine deficiency")
        msg1.place(x='35',y='5')        
        
        
    
def automatic_email():
    date=date_menu.get()
    month=month_menu.get()
    time_=times.get()
    user = e1.get()
    email =e2.get()
    doc1=endo.get()
    doc2=cardio.get()
    doc3=gen.get()
    message = (f"\nDear {user}  Your appointment has been successfully booked on {date} {month} 2022 at {time_} with{doc1},{doc2},{doc3} \n See you there!\n For any query contact: +91XXXXXXXXX\n\nRegards,\nCode Junkies\n\nPlease Do not reply it is an autogenerated email")
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("codejunkies360@gmail.com", "kmdk xpxm ieoq xrqj")
    s.sendmail("&&&&&&&&&&&",email,message)
    messagebox.showinfo("Conformation Info","Appointment Confirmed!!\nCheck Your Email")
win=tk.Tk()
win.geometry("1000x700")
win.configure(bg="lemon chiffon")
win.title("Code Junkies ")
l=tk.Label(win,text="Welcome To Appointment & Medical Report System",font='calibri',bg='lemon chiffon')
ly=tk.Label(win,text="Book your Appointment",font='calibri',bg='lemon chiffon')
ly.place(x='45',y='45')

l.place(x='250',y='5')
l1=tk.Label(win,text="Enter your Name",bg='lemon chiffon').place(x='45',y='80')
e1=tk.Entry(win)

e1.place(x='145',y='80')
l2=tk.Label(win,text="Enter Email",bg='lemon chiffon').place(x='45',y='105')
e2=tk.Entry(win)
e2.place(x='145',y='105')

month_menu=tk.StringVar()
month_menu.set("Month")
drop1=tk.OptionMenu(win,month_menu,"Jan","Feb","March","April","May","June","July","Aug","Sep","Oct","Nov","Dec")
drop1.place(x=125,y=145)

l3=tk.Label(win,text="Select Date",bg='lemon chiffon')
l3.place(x=45,y=145)
date_menu=tk.StringVar()
date_menu.set("Date")
drop2=tk.OptionMenu(win,date_menu,"1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29")
drop2.place(x=220,y=145)
day_menu=tk.StringVar()
day_menu.set("Day")


times=tk.StringVar()

l4=tk.Label(win,text="Available Slots",bg='lemon chiffon')
l4.place(x=45,y=200)
r1=tk.Radiobutton(win,text="10 AM",value="10 AM",variable=times)
r2=tk.Radiobutton(win,text="12 PM",value="12 PM",variable=times)
r3=tk.Radiobutton(win,text="3 PM",value="3 PM",variable=times)
r4=tk.Radiobutton(win,text="5 PM",value="5 PM",variable=times)

r1.place(x=130,y=200)
r2.place(x=200,y=200)
r3.place(x=270,y=200)
r4.place(x=340,y=200)


button=tk.Button(text="Book",command=automatic_email,width="10")
button.place(x=100,y=500)
button2=tk.Button(text="Exit",command=win.destroy,width="10")
button2.place(x=300,y=500)

doc=tk.Label(win,text="Select Doctor and Specialty",bg='lemon chiffon').place(x='45',y='250')
endo=tk.Label(win,text="Endocrionologist",bg="lemon chiffon").place(x='55',y='300')
gen=tk.Label(win,text="General Physician",bg="lemon chiffon").place(x='55',y='350')
cardio=tk.Label(win,text="Cardiologist",bg="lemon chiffon").place(x='55',y='400')
endo=tk.StringVar()
endo.set("Select Dr")
endo_drop=tk.OptionMenu(win,endo,"Dr S.V Madhu(mailesisecretariat@gmail.com)","Dr. Sujoy Ghosh(mailesisecretariat@gmail.com)")
cardio=tk.StringVar()
cardio.set("Select Dr")
cardio_drop=tk.OptionMenu(win,cardio,"Dr. B P Singh (bpsingh.igis@gmail.com)","Dr. Manoranjan Mandal (drmandal6126@gmail.com)")
gen=tk.StringVar()
gen.set("Select Dr")
gen_drop=tk.OptionMenu(win,gen,"Dr. S Arulrhaj (drarulrhaj@gmail.com)","Dr. Mangesh Tiwaskar (tiwaskar@gmail.com)")
endo_drop.place(x=160,y='300')
cardio_drop.place(x=160,y='350')
gen_drop.place(x=160,y='400')



l4=tk.Label(win,text="Enter your vitals",bg='lemon chiffon',font='Calibri').place(x='550',y='45')
age=tk.Label(win,text="Age",bg='lemon chiffon').place(x='550',y='80')
age_entry=tk.Entry(win,width='7')
age_entry.place(x='580',y='80')
gender=tk.StringVar()
gender.set("Gender")
gender_drop=tk.OptionMenu(win,gender,"Male","Female","Trans","Prefer not say")
gender_drop.place(x='660',y='75')
l5=tk.Label(win,text="Blood Pressure",bg='lemon chiffon').place(x='550',y='120')
l6=tk.Label(win,text="Resting Heart Rate",bg='lemon chiffon').place(x='550',y='220')
l7=tk.Label(win,text="Sugar Levels",bg='lemon chiffon').place(x='550',y='270')
sys=tk.Label(win,text="sys",bg='lemon chiffon').place(x='635',y='120')
dys=tk.Label(win,text="dys",bg='lemon chiffon').place(x='635',y='170')
e5=tk.Entry(win,width='10')
e5.place(x='660',y='120')
ays=tk.Entry(win,width='10')
ays.place(x='660',y='170')
e6=tk.Entry(win,width='10')
e6.place(x='660',y='220')
e7=tk.Entry(win,width='10')
e7.place(x='660',y='270')
e8=tk.Entry(win,width='10')
e8.place(x='660',y='320')
l51=tk.Label(win,text="mm/Hg",bg='lemon chiffon',).place(x='730',y='120')
lays=tk.Label(win,text="mm/Hg",bg='lemon chiffon',).place(x='730',y='170')
l61=tk.Label(win,text="beats/min",bg='lemon chiffon').place(x='730',y='220')
l71=tk.Label(win,text="mg/dl",bg='lemon chiffon').place(x='730',y='270')
b51=tk.Button(win,text="Check",command=bp).place(x='800',y='135')
b61=tk.Button(win,text="Check",command=heartrate).place(x='800',y='220')
b71=tk.Button(win,text="Check",command=sugar).place(x='800',y='270')
b81=tk.Button(win,text="Check",command=thyroid).place(x='800',y='400')

thy=tk.Label(win,text="Thyroid",bg="lemon chiffon").place(x='570',y='370')
t3=tk.Label(win,text="T3",bg="lemon chiffon").place(x='635',y='370')
t4=tk.Label(win,text="T4",bg="lemon chiffon").place(x='700',y='370')
tsh=tk.Label(win,text="TSH",bg="lemon chiffon").place(x='740',y='370')


t3_entry=tk.Entry(win,width='4')
t3_entry.place(x='635',y='420')
t4_entry=tk.Entry(win,width='4')
t4_entry.place(x='700',y='420')
tsh_entry=tk.Entry(win,width='4')
tsh_entry.place(x='740',y='420')
















  
 

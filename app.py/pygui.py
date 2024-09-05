from tkinter import *
from tkinter import messagebox
from helpfunctions import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


root = Tk()

root.title("Heater Tube Simulations") 
root.geometry("900x800") #Width x Height
root.minsize(600,800)
root.configure(background='#ed0fcf')


def CallBack():
    B.config(bg='green')
    p1=float(text_p1.get("1.0","end-1c"))
    v1=float(text_v1.get("1.0","end-1c"))
    t1=float(text_t1.get("1.0","end-1c"))
    rh=float(text_r1.get("1.0","end-1c"))
    p2=float(text_p2.get("1.0","end-1c"))
    t2=float(text_t2.get("1.0","end-1c"))

    
    p=float(text_p.get("1.0","end-1c"))
    v=float(text_v.get("1.0","end-1c"))
    t=float(text_t.get("1.0","end-1c"))
    (y1_wat_vap, y1_dry_air, y2_wat_vap, y2_dry_air, m1, m2, m3, water_flow_rate,\
    water_condensed_per_hour, p1,v1,t1,rh,t2,p2) = flow_calc(p1,v1,t1,rh,t2,p2,p,v,t)

    water_condensed_per_hour=round(water_condensed_per_hour,4)
    water_flow_rate=round(water_flow_rate,4)
    y1_wat_vap=round(y1_wat_vap,4)
    y1_dry_air=round(y1_dry_air,4)
    y2_wat_vap=round(y2_wat_vap,4)
    y2_dry_air=round(y2_dry_air,4)
    m1=round(m1,4)
    m2=round(m2,4)
    m3=round(m3,4)
     
    masslabel.config(text=water_condensed_per_hour)
    watervol.config(text=water_flow_rate)
    watervapour1label.config(text=y1_wat_vap)
    dryairlabel1.config(text=y1_dry_air)
    watervapour2label.config(text=y2_wat_vap)
    dryairlabel2.config(text=y2_dry_air)

    m1label.config(text=m1)
    m2label.config(text=m2)
    m3label.config(text=m3)

def onNightMode():
    
    

    try:
        humidity,temperature =Adafruit_DHT.read_retry(11,4)
        
        text_t1.insert(INSERT,temperature)
        text_r1.insert(INSERT,humidity)

    except:
        messagebox.showwarning("Hardware error","Connect DHT11 Sensor")
    b.config(bg='green')
    
l=Label(root,text="Inlet Conditions")
l.place(x=0,y=10)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Pressure (mmhg)")
l.place(x=0,y=30)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Volume (m3/min)")
l.place(x=0,y=50)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Temperature (celsius)")
l.place(x=0,y=70)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Inlet Relative Humidity")
l.place(x=0,y=90)
l.config(width=20,height=1,font=("Times New Roman",11))

#=============================Text=================================
text_p1 = Text(root)
text_p1.place(x=170,y=30)
text_p1.insert(INSERT,750)
text_p1.config(width=5,height=1,font=("Times New Roman",11))

text_v1 = Text(root)
text_v1.place(x=170,y=50)
text_v1.insert(INSERT,1)
text_v1.config(width=5,height=1,font=("Times New Roman",11))

text_t1 = Text(root)
text_t1.place(x=170,y=70)
text_t1.config(width=5,height=1,font=("Times New Roman",11))
text_t1.insert(INSERT,35)

text_r1 = Text(root)
text_r1.place(x=170,y=90)
text_r1.insert(INSERT,0.9)
text_r1.config(width=5,height=1,font=("Times New Roman",11))

b=Button(root, text="Get from sensor",relief="raised",bg="red",command= onNightMode)
b.place(x=220,y=70)
b.config(width=15,height=1,font=("Times New Roman",11))


#==================================STP conditions=================
l=Label(root,text="STP Conditions")
l.place(x=0,y=120)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Pressure (mmhg)")
l.place(x=0,y=140)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Volume (m3/min)")
l.place(x=0,y=160)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Temperature (celsius)")
l.place(x=0,y=180)
l.config(width=20,height=1,font=("Times New Roman",11))

#=======================Text=====================================
text_p = Text(root)
text_p.place(x=170,y=140)
text_p.insert(INSERT,760)
text_p.config(width=5,height=1,font=("Times New Roman",11))

text_v = Text(root)
text_v.place(x=170,y=160)
text_v.insert(INSERT,22.4)
text_v.config(width=5,height=1,font=("Times New Roman",11))

text_t = Text(root)
text_t.place(x=170,y=180)
text_t.config(width=5,height=1,font=("Times New Roman",11))
text_t.insert(INSERT,0)

#===========================outlet conditions===============
l=Label(root,text="Outlet Conditions")
l.place(x=0,y=220)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Pressure (mmhg)")
l.place(x=0,y=240)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Temperature (C)")
l.place(x=0,y=260)
l.config(width=20,height=1,font=("Times New Roman",11))

#=============================Text==================
text_p2 = Text(root)
text_p2.place(x=170,y=240)
text_p2.insert(INSERT,760)
text_p2.config(width=5,height=1,font=("Times New Roman",11))

text_t2 = Text(root)
text_t2.place(x=170,y=260)
text_t2.insert(INSERT,0)
text_t2.config(width=5,height=1,font=("Times New Roman",11))

#=========================Result Buttons=========================
B = Button(root, text = "Compute Result", command = CallBack, bg="red")
B.place(x=10,y=300)
B.config(width=15,height=1,font=("Times New Roman",11))
 
#===========================Result label======================
l=Label(root,text="Results")
l.place(x=0,y=340)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Mole fractions")
l.place(x=0,y=360)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Water Vapour at inlet (y1)")
l.place(x=0,y=380)
l.config(width=30,height=1,font=("Times New Roman",11))

l=Label(root,text="Dry air at inlet (1 - y1)")
l.place(x=0,y=400)
l.config(width=30,height=1,font=("Times New Roman",11))

l=Label(root,text="Water Vapour at outlet (y2)")
l.place(x=0,y=420)
l.config(width=30,height=1,font=("Times New Roman",11))

l=Label(root,text="Dry air at outlet (1-y2)")
l.place(x=0,y=440)
l.config(width=30,height=1,font=("Times New Roman",11))

l=Label(root,text="Volumentric flow rate")
l.place(x=0,y=460)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="dry air at inlet (m1)")
l.place(x=0,y=480)
l.config(width=30,height=1,font=("Times New Roman",11))

l=Label(root,text="dry air at outlet (m2)")
l.place(x=0,y=500)
l.config(width=30,height=1,font=("Times New Roman",11))

l=Label(root,text="condensed water (m3)")
l.place(x=0,y=520)
l.config(width=30,height=1,font=("Times New Roman",11))

l=Label(root,text="Condensed water flow rate (g/min)")
l.place(x=0,y=540)
l.config(width=30,height=1,font=("Times New Roman",11))

l=Label(root,text="Mass of water condensed per hour (kg)")
l.place(x=0,y=560)
l.config(width=30,height=1,font=("Times New Roman",11))

#=========================================================
watervapour1label=Label(root,text=" ")
watervapour1label.place(x=250,y=380)
watervapour1label.config(width=5,height=1,font=("Times New Roman",11))

dryairlabel1=Label(root,text=" ")
dryairlabel1.place(x=250,y=400)
dryairlabel1.config(width=5,height=1,font=("Times New Roman",11))


watervapour2label=Label(root,text=" ")
watervapour2label.place(x=250,y=420)
watervapour2label.config(width=5,height=1,font=("Times New Roman",11))

dryairlabel2=Label(root,text=" ")
dryairlabel2.place(x=250,y=440)
dryairlabel2.config(width=5,height=1,font=("Times New Roman",11))

m1label=Label(root,text=" ")
m1label.place(x=250,y=480)
m1label.config(width=5,height=1,font=("Times New Roman",11))

m2label=Label(root,text=" ")
m2label.place(x=250,y=500)
m2label.config(width=5,height=1,font=("Times New Roman",11))

m3label=Label(root,text=" ")
m3label.place(x=250,y=520)
m3label.config(width=5,height=1,font=("Times New Roman",11))

watervol=Label(root,text=" ")
watervol.place(x=250,y=540)
watervol.config(width=5,height=1,font=("Times New Roman",11))

masslabel=Label(root,text=" ")
masslabel.place(x=250,y=560)
masslabel.config(width=5,height=1,font=("Times New Roman",11))

#===============================simulation=============================
l=Label(root,text="Simulation")
l.place(x=0,y=590)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Inlet Temperature")
l.place(x=0,y=610)
l.config(width=20,height=1,font=("Times New Roman",11))

l=Label(root,text="Outlet Temperature")
l.place(x=0,y=630)
l.config(width=20,height=1,font=("Times New Roman",11))

#=================================Text===============================
ti = Text(root)
ti.place(x=170,y=610)
ti.insert(INSERT,"100,199")
ti.config(width=10,height=1,font=("Times New Roman",11))

to = Text(root)
to.place(x=170,y=630)
to.insert(INSERT,"5,40,60")
to.config(width=15,height=1,font=("Times New Roman",11))


figure1=plt.Figure(figsize=(5,5),dpi=100)
ax1=figure1.add_subplot(211)
ax2=figure1.add_subplot(212)
bar1=FigureCanvasTkAgg(figure1,root)
bar1.get_tk_widget().pack(side=RIGHT,fill=BOTH)

def CallBack2():
    outlet=to.get("1.0","end-1c")
    inlet=ti.get("1.0","end-1c")
      
    outlet=outlet.split(",")
    inlet=inlet.split(",")
    
    water_quantities = []
    inlet=list(map(int,inlet))
    #inlet_temperatures = np.linspace(1,100,199)
    inlet_temperatures = np.linspace(1,inlet[0],inlet[1])
    #outlet_temperatures = [5, 40, 60]
    outlet_temperatures = list(map(int,outlet))
    
    B2.config(bg='green')
    p1=float(text_p1.get("1.0","end-1c"))
    v1=float(text_v1.get("1.0","end-1c"))
    t1=float(text_t1.get("1.0","end-1c"))
    rh=float(text_r1.get("1.0","end-1c"))
    p2=float(text_p2.get("1.0","end-1c"))
    t2=float(text_t2.get("1.0","end-1c"))

    p=float(text_p.get("1.0","end-1c"))
    v=float(text_v.get("1.0","end-1c"))
    t=float(text_t.get("1.0","end-1c"))

    for outlet_temp in outlet_temperatures:
        quantity = []
        for inlet_temp in inlet_temperatures:
            (_,_,_,_,_,_,_,_,water_condensed_per_hour, _,_,_,_,_,_) = \
            flow_calc(p1,v1,inlet_temp,rh,outlet_temp,p2,p,v,t)

            quantity.append(water_condensed_per_hour)
        water_quantities.append(quantity)

    # iterate for different outlet temperatures and plot each of them
    for idx, outlet_temp in enumerate(outlet_temperatures):
        # this line (below) actually do the plotting. Note: first argument is x, second is y
        ax1.plot(inlet_temperatures, water_quantities[idx], label = str(outlet_temp) + ' °C')
        # code below does formatting (like adding label, title, show legend, grid ,etc)
        #ax1.set_xlabel('Inlet Temperatures (°C)')
        ax1.set_ylabel('Water condensation rate\n(in kg/hr) or (in liter/hr)')
        ax1.set_title('Water Quantities Vs Inlet Temperature\nfor different outlet temperatures')
        ax1.grid()
        ax1.legend()
        
    for idx, outlet_temp in enumerate(outlet_temperatures):
        ax2.plot(inlet_temperatures, 30/np.asarray(water_quantities[idx]), label = str(outlet_temp) + ' °C')
        # code below does formatting (like adding label, title, show legend, grid ,etc)
        ax2.set_yscale('log') # it will change y-axis to logarithmic scale, making it more readable
        ax2.set_xlabel('Inlet Temperatures (°C)')
        ax2.set_ylabel('Time taken to condense 30 kg of water (hr)')
        ax2.set_title('Time takeny to condense 30kg of water with\n different Inlet Temperature and outlet temperatures',fontsize=8)
        ax2.grid()
        ax2.legend()
         
B2 = Button(root, text = "Plot", command = CallBack2, bg="red")
B2.place(x=170,y=650)
B2.config(width=15,height=1,font=("Times New Roman",11))
     
root.mainloop()

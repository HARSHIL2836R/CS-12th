from tkinter import *
import mysql.connector as con




mydb=con.connect(host='localhost',user='root',password='root',database='Periodic', port='2836')
cur=mydb.cursor()
root3=Tk()
root3.attributes('-fullscreen',True)
def show():
    root=Tk()

    root.geometry("1215x593")

    root.title("PERIODIC TABLE")

    root.config(background="white")

    root.resizable(0,0)




    def Legend():
        Legend=Toplevel(root)
        Legend.title("LEGENDS")
        Legend.resizable(0,0)
        Legend1=Label(Legend,text="AKALI \n METAL", font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        Legend1.grid(row=1,column=1)
        Legend2=Label(Legend,text="", font=('Verdana', 12), relief="solid", width="20", height="2", bg="maroon1")
        Legend2.grid(row=1,column=2)
        Legend3=Label(Legend,text="Akaline \n Earth", font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        Legend3.grid(row=2,column=1)
        Legend4=Label(Legend,text="", font=('Verdana', 12), relief="solid", width="20", height="2", bg="darkorchid1")
        Legend4.grid(row=2,column=2)
        Legend5=Label(Legend,text="Transition \n Metals", font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        Legend5.grid(row=3,column=1)
        Legend6=Label(Legend,text="", font=('Verdana', 12), relief="solid", width="20", height="2", bg="steelblue1")
        Legend6.grid(row=3,column=2)
        Legend7=Label(Legend,text="Basic \n Metal", font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        Legend7.grid(row=4,column=1)
        Legend8=Label(Legend,text="", font=('Verdana', 12), relief="solid", width="20", height="2", bg="IndianRed1")
        Legend8.grid(row=4,column=2)
        Legend9=Label(Legend,text="Semi \n metal", font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        Legend9.grid(row=5,column=1)
        Legend10=Label(Legend,text="", font=('Verdana', 12), relief="solid", width="20", height="2", bg="spring green")
        Legend10.grid(row=5,column=2)
        Legend11=Label(Legend,text="Non \n Metal", font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        Legend11.grid(row=6,column=1)
        Legend12=Label(Legend,text="", font=('Verdana', 12), relief="solid", width="20", height="2", bg="dodgerblue2")
        Legend12.grid(row=6,column=2)
        Legend13=Label(Legend,text="Halogens", font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        Legend13.grid(row=7,column=1)
        Legend14=Label(Legend,text="", font=('Verdana', 12), relief="solid", width="20", height="2", bg="gold2")
        Legend14.grid(row=7,column=2)
        Legend15=Label(Legend,text="Nobel \n Gas", font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        Legend15.grid(row=8,column=1)
        Legend16=Label(Legend,text="", font=('Verdana', 12), relief="solid", width="20", height="2", bg="darkgoldenrod2")
        Legend16.grid(row=8,column=2)
        Legend17=Label(Legend,text="Lanthanoide", font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        Legend17.grid(row=9,column=1)
        Legend18=Label(Legend,text="", font=('Verdana', 12), relief="solid", width="20", height="2", bg="yellow")
        Legend18.grid(row=9,column=2)
        Legend17=Label(Legend,text="Actinide", font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        Legend17.grid(row=10,column=1)
        Legend18=Label(Legend,text="", font=('Verdana', 12), relief="solid", width="20", height="2", bg="firebrick1")
        Legend18.grid(row=10,column=2)

    custom=Label(root, bg="white", text = 'groups(across) \n periods(down)', font=('Verdana', 12),fg="red")
    custom.grid(row=1,column=1)
    group1=Button(root, activebackground="white", command=lambda:[H(),Li(),Na(),K(),Rb(),Cs(),Fr()], bg="white", text = '1', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group1.grid(row=1,column=2)
    group2=Button(root, activebackground="white", command=lambda:[Be(),Mg(),Ca(),Sr(),Ba(),Ra(),], bg="white", text = '2', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group2.grid(row=1,column=3)
    group3=Button(root, activebackground="white", command=lambda:[Sc(),Y()], bg="white", text = '3', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group3.grid(row=1,column=4)
    group4=Button(root, activebackground="white", command=lambda:[Ti(),Zr(),Hf(),Rf()], bg="white", text = '4', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group4.grid(row=1,column=5)
    group5=Button(root, activebackground="white", command=lambda:[V(),Nb(),Ta(),Db()], bg="white", text = '5', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group5.grid(row=1,column=6)
    group6=Button(root, activebackground="white", command=lambda:[Cr(),Mo(),W(),Sg()], bg="white", text = '6', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group6.grid(row=1,column=7)
    group7=Button(root, activebackground="white", command=lambda:[Mn(),Tc(),Re(),Bh()], bg="white", text = '7', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group7.grid(row=1,column=8)
    group8=Button(root, activebackground="white", command=lambda:[Fe(),Ru(),Os(),Hs()], bg="white", text = '8', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group8.grid(row=1,column=9)
    group9=Button(root, activebackground="white", command=lambda:[Co(),Rh(),Ir(),Mt()], bg="white", text = '9', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group9.grid(row=1,column=10)
    group10=Button(root, activebackground="white", command=lambda:[Ni(),Pd(),Pt(),Ds()], bg="white", text = '10', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group10.grid(row=1,column=11)
    group11=Button(root, activebackground="white", command=lambda:[Cu(),Ag(),Au(),Rg()], bg="white", text = '11', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group11.grid(row=1,column=12)
    group12=Button(root, activebackground="white", command=lambda:[Zn(),Cd(),Hg(),Cn()], bg="white", text = '12', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group12.grid(row=1,column=13)
    group13=Button(root, activebackground="white", command=lambda:[B(),Al(),Ga(),In(),Tl(),Nh()], bg="white", text = '13', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group13.grid(row=1,column=14)
    group14=Button(root, activebackground="white", command=lambda:[C(),Si(),Ge(),Sn(),Pb(),Fl()], bg="white", text = '14', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")    
    group14.grid(row=1,column=15)
    group15=Button(root, activebackground="white", command=lambda:[N(),P(),As(),Sb(),Bi(),Mc()], bg="white", text = '15', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group15.grid(row=1,column=16)
    group16=Button(root, activebackground="white", command=lambda:[O(),S(),Se(),Te(),Po(),Lv()], bg="white", text = '16', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group16.grid(row=1,column=17)
    group17=Button(root, activebackground="white", command=lambda:[F(),Cl(),Br(),I(),At(),Ts()], bg="white", text = '17', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group17.grid(row=1,column=18)
    group18=Button(root, activebackground="white", command=lambda:[He(),Ne(),Ar(),Kr(),Xe(),Rn(),Og()], bg="white", text = '18', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    group18.grid(row=1,column=19)
    period1=Button(root, activebackground="white", command=lambda:[H(),He()], bg="white", text = '1', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    period1.grid(row=2,column=1)
    period2=Button(root, activebackground="white", command=lambda:[Li(),Be(),B(),C(),N(),O(),F(),Ne()], bg="white", text = '2', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    period2.grid(row=3,column=1)
    period3=Button(root, activebackground="white", command=lambda:[Na(),Mg(),Al(),Si(),P(),S(),Cl(),Ar()], bg="white", text = '3', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    period3.grid(row=4,column=1)
    period4=Button(root, activebackground="white", command=lambda:[K(),Ca(),Sc(),Ti(),V(),Cr(),Mn(),Fe(),Co(),Ni(),Cu(),Zn(),Ga(),Ge(),As(),Se(),Br(),Kr()], bg="white", text = '4', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    period4.grid(row=5,column=1)
    period5=Button(root, activebackground="white", command=lambda:[Rb(),Sr(),Y(),Zr(),Nb(),Mo(),Tc(),Ru(),Rh(),Pd(),Ag(),Cd(),In(),Sn(),Sb(),Te(),I(),Xe()], bg="white", text = '5', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    period5.grid(row=6,column=1)
    period6=Button(root, activebackground="white", command=lambda:[Cs(),Ba(),Hf(),Ta(),W(),Re(),Os(),Ir(),Pt(),Au(),Hg(),Tl(),Pb(),Bi(),Po(),At(),Rn()], bg="white", text = '6', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7")
    period6.grid(row=7,column=1)
    period7=Button(root, activebackground="white", command=lambda:[Fr(),Ra(),Rf(),Db(),Sg(),Bh(),Hs(),Mt(),Ds(),Rg(),Cn(),Nh(),Fl(),Mc(),Lv(),Ts(),Og()], bg="white", text = '7', font=('Verdana', 15),fg="blue", width="3", height="1", bd="7" )
    period7.grid(row=8,column=1)

    hydrogen=Button(root, text = 'H', command=None, bg="dodgerblue2", activebackground="dodgerblue2", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    hydrogen.grid(row=2,column=2)    

    helium=Button(root, text = 'He', command=None, bg="darkgoldenrod2", activebackground="darkgoldenrod2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    helium.grid(row=2,column=19)

    lithium=Button(root, text = 'Li', command=None, bg="maroon1", activebackground="maroon1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    lithium.grid(row=3,column=2)

    berylium=Button(root, text = 'Be', command=None, bg="darkorchid1", activebackground="darkorchid1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    berylium.grid(row=3,column=3)

    boron=Button(root, text = 'B', command=None, bg="spring green", activebackground="spring green", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    boron.grid(row=3,column=14)

    carbon=Button(root, text = 'C', command=None, bg="dodgerblue2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="dodgerblue2")
    carbon.grid(row=3,column=15)

    nitrogen=Button(root, text = 'N', command=None, bg="dodgerblue2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="dodgerblue2")
    nitrogen.grid(row=3,column=16)

    oxygen=Button(root, text = 'O', command=None, bg="dodgerblue2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="dodgerblue2")
    oxygen.grid(row=3,column=17)

    fluorine=Button(root, text = 'F', command=None, bg="gold2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="gold2")
    fluorine.grid(row=3,column=18)

    neon=Button(root, text = 'Ne', command=None, bg="darkgoldenrod2", activebackground="darkgoldenrod2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    neon.grid(row=3,column=19)

    sodium=Button(root, text = 'Na', command=None, bg="maroon1", activebackground="maroon1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    sodium.grid(row=4,column=2)

    magnesium=Button(root, text = 'Mg', command=None, bg="darkorchid1", activebackground="darkorchid1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    magnesium.grid(row=4,column=3)

    aluminium=Button(root, text = 'Al', command=None, bg="IndianRed1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="IndianRed1")
    aluminium.grid(row=4,column=14)

    silicon=Button(root, text = 'Si', command=None, bg="spring green", activebackground="spring green", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    silicon.grid(row=4,column=15)

    phosphorus=Button(root, text = 'P', command=None, bg="dodgerblue2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="dodgerblue2")
    phosphorus.grid(row=4,column=16)

    sulphur=Button(root, text = 'S', command=None, bg="dodgerblue2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="dodgerblue2")
    sulphur.grid(row=4,column=17)

    chlorine=Button(root, text = 'Cl', command=None, bg="gold2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="gold2")
    chlorine.grid(row=4,column=18)

    argon=Button(root, text = 'Ar', command=None, bg="darkgoldenrod2", activebackground="darkgoldenrod2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    argon.grid(row=4,column=19)

    pottassium=Button(root, text = 'K', command=None, bg="maroon1", activebackground="maroon1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    pottassium.grid(row=5,column=2)

    calcium=Button(root, text = 'Ca', command=None, bg="darkorchid1", activebackground="darkorchid1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    calcium.grid(row=5,column=3)

    scandium=Button(root, text = 'Sc', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    scandium.grid(row=5,column=4)

    titanium=Button(root, text = 'Ti', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    titanium.grid(row=5,column=5)

    vanadium=Button(root, text = 'V', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    vanadium.grid(row=5,column=6)

    chromium=Button(root, text = 'Cr', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    chromium.grid(row=5,column=7)

    manganese=Button(root, text = 'Mn', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    manganese.grid(row=5,column=8)

    iron=Button(root, text = 'Fe', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    iron.grid(row=5,column=9)

    cobalt=Button(root, text = 'Co', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    cobalt.grid(row=5,column=10)

    nickel=Button(root, text = 'Ni', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    nickel.grid(row=5,column=11)

    copper=Button(root, text = 'Cu', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    copper.grid(row=5,column=12)

    zinc=Button(root, text = 'Zn', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    zinc.grid(row=5,column=13)

    gallium=Button(root, text = 'Ga', command=None, bg="IndianRed1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="IndianRed1")
    gallium.grid(row=5,column=14)

    germanium=Button(root, text = 'Ge', command=None, bg="spring green", activebackground="spring green", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    germanium.grid(row=5,column=15)

    arsenic=Button(root, text = 'As', command=None, bg="spring green", activebackground="spring green", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    arsenic.grid(row=5,column=16)

    selenium=Button(root, text = 'Se', command=None, bg="dodgerblue2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="dodgerblue2")
    selenium.grid(row=5,column=17)

    bromine=Button(root, text = 'Br', command=None, bg="gold2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="gold2")
    bromine.grid(row=5,column=18)

    krypton=Button(root, text = 'Kr', command=None, bg="darkgoldenrod2", activebackground="darkgoldenrod2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    krypton.grid(row=5,column=19)

    rubidium=Button(root, text = 'Rb', command=None, bg="maroon1", activebackground="maroon1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    rubidium.grid(row=6,column=2)

    strontium=Button(root, text = 'Sr', command=None, bg="darkorchid1", activebackground="darkorchid1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    strontium.grid(row=6,column=3)

    yttrium=Button(root, text = 'Y', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    yttrium.grid(row=6,column=4)

    zirconium=Button(root, text = 'Zr', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    zirconium.grid(row=6,column=5)

    niobium=Button(root, text = 'Nb', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    niobium.grid(row=6,column=6)

    molybdenum=Button(root, text = 'Mo', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    molybdenum.grid(row=6,column=7)

    technetium=Button(root, text = 'Tc', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    technetium.grid(row=6,column=8)

    ruthenium=Button(root, text = 'Ru', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    ruthenium.grid(row=6,column=9)

    rhodium=Button(root, text = 'Rh', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    rhodium.grid(row=6,column=10)

    palladium=Button(root, text = 'Pd', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    palladium.grid(row=6,column=11)

    silver=Button(root, text = 'Ag', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    silver.grid(row=6,column=12)

    cadmium=Button(root, text = 'Cd', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    cadmium.grid(row=6,column=13)

    indium=Button(root, text = 'In', command=None, bg="IndianRed1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="IndianRed1")
    indium.grid(row=6,column=14)

    tin=Button(root, text = 'Sn', command=None, bg="IndianRed1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="IndianRed1")
    tin.grid(row=6,column=15)

    antimony=Button(root, text = 'Sb', command=None, bg="spring green", activebackground="spring green", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    antimony.grid(row=6,column=16)

    tellurium=Button(root, text = 'Te', command=None, bg="spring green", activebackground="spring green", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    tellurium.grid(row=6,column=17)

    iodine=Button(root, text = 'I', command=None, bg="gold2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="gold2")
    iodine.grid(row=6,column=18)

    xenon=Button(root, text = 'Xe', command=None, bg="darkgoldenrod2", activebackground="darkgoldenrod2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    xenon.grid(row=6,column=19)

    caesium=Button(root, text = 'Cs', command=None, bg="maroon1", activebackground="maroon1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    caesium.grid(row=7,column=2)

    barium=Button(root, text = 'Ba', command=None, bg="darkorchid1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="darkorchid1")
    barium.grid(row=7,column=3)

    LS=Button(root, text = 'L.S.', bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    LS.grid(row=7,column=4)

    hafnium=Button(root, text = 'Hf', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    hafnium.grid(row=7,column=5)

    tantalum=Button(root, text = 'Ta', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    tantalum.grid(row=7,column=6)

    tungsten=Button(root, text = 'W', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    tungsten.grid(row=7,column=7)

    rhenium=Button(root, text = 'Re', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    rhenium.grid(row=7,column=8)

    osmium=Button(root, text = 'Os', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    osmium.grid(row=7,column=9)

    iridium=Button(root, text = 'Ir', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    iridium.grid(row=7,column=10)

    platinum=Button(root, text = 'Pt', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    platinum.grid(row=7,column=11)

    gold=Button(root, text = 'Au', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    gold.grid(row=7,column=12)

    mercury=Button(root, text = 'Hg', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    mercury.grid(row=7,column=13)

    thalium=Button(root, text = 'Tl', command=None, bg="IndianRed1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="IndianRed1")
    thalium.grid(row=7,column=14)

    lead=Button(root, text = 'Pb', command=None, bg="IndianRed1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="IndianRed1")
    lead.grid(row=7,column=15)

    bismuth=Button(root, text = 'Bi', command=None, bg="IndianRed1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="IndianRed1")
    bismuth.grid(row=7,column=16)

    polonium=Button(root, text = 'Po', command=None, bg="spring green", activebackground="spring green", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    polonium.grid(row=7,column=17)

    astatine=Button(root, text = 'At', command=None, bg="gold2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="gold2")
    astatine.grid(row=7,column=18)

    radon=Button(root, text = 'Rn', command=None, bg="darkgoldenrod2", activebackground="darkgoldenrod2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    radon.grid(row=7,column=19)

    francium=Button(root, text = 'Fr', command=None, bg="maroon1", activebackground="maroon1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black")
    francium.grid(row=8,column=2)

    radium=Button(root, text = 'Ra', command=None, bg="darkorchid1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="darkorchid1")
    radium.grid(row=8,column=3)

    AS=Button(root, text = 'A.S.', bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    AS.grid(row=8,column=4)

    rutherfordium=Button(root, text = 'Rf', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    rutherfordium.grid(row=8,column=5)

    dubnium=Button(root, text = 'Db', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    dubnium.grid(row=8,column=6)

    seaborgium=Button(root, text = 'Sg', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    seaborgium.grid(row=8,column=7)

    bohrium=Button(root, text = 'Bh', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    bohrium.grid(row=8,column=8)

    hassium=Button(root, text = 'Hs', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    hassium.grid(row=8,column=9)

    meitnerium=Button(root, text = 'Mt', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    meitnerium.grid(row=8,column=10)

    darmstadtium=Button(root, text = 'Ds', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    darmstadtium.grid(row=8,column=11)

    roentgenium=Button(root, text = 'Rg', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    roentgenium.grid(row=8,column=12)

    copernicium=Button(root, text = 'Cn', command=None, bg="steelblue1", activebackground="steelblue1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black")
    copernicium.grid(row=8,column=13)

    nihonium=Button(root, text = 'Nh', command=None, bg="IndianRed1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="IndianRed1")
    nihonium.grid(row=8,column=14)

    flerovium=Button(root, text = 'Fl', command=None, bg="IndianRed1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="IndianRed1")
    flerovium.grid(row=8,column=15)

    moscovium=Button(root, text = 'Mc', command=None, bg="IndianRed1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="IndianRed1")
    moscovium.grid(row=8,column=16)

    livermorium=Button(root, text = 'Lv', command=None, bg="IndianRed1", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="IndianRed1")
    livermorium.grid(row=8,column=17)

    tennessine=Button(root, text = 'Ts', command=None, bg="gold2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="gold2")
    tennessine.grid(row=8,column=18)

    oganesson=Button(root, text = 'Og', command=None, bg="darkgoldenrod2", bd="7", font=('Verdana', 15), width="3", height="1" , fg="black", activebackground="darkgoldenrod2")
    oganesson.grid(row=8,column=19)

    lanthanum=Button(root, text = 'La', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    lanthanum.grid(row=9,column=4)

    cerium=Button(root, text = 'Ce', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    cerium.grid(row=9,column=5)

    praseodymium=Button(root, text = 'Pr', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    praseodymium.grid(row=9,column=6)

    neodymium=Button(root, text = 'Nd', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    neodymium.grid(row=9,column=7)

    promethium=Button(root, text = 'Pm', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    promethium.grid(row=9,column=8)

    samarium=Button(root, text = 'Sm', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    samarium.grid(row=9,column=9)

    europium=Button(root, text = 'Eu', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    europium.grid(row=9,column=10)

    gadolinium=Button(root, text = 'Gd', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    gadolinium.grid(row=9,column=11)

    terbium=Button(root, text = 'Tb', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    terbium.grid(row=9,column=12)

    dysprocium=Button(root, text = 'Dy', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    dysprocium.grid(row=9,column=13)

    holmium=Button(root, text = 'Ho', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    holmium.grid(row=9,column=14)

    erbium=Button(root, text = 'Er', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    erbium.grid(row=9,column=15)

    thulium=Button(root, text = 'Tm', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    thulium.grid(row=9,column=16)

    ytterbium=Button(root, text = 'Yb', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    ytterbium.grid(row=9,column=17)

    lutetium=Button(root, text = 'Lu', command=None, bg="yellow", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="yellow")
    lutetium.grid(row=9,column=18)
       
    actinium=Button(root, text = 'Ac', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    actinium.grid(row=10,column=4)

    thorium=Button(root, text = 'Th', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    thorium.grid(row=10,column=5)

    protactinium=Button(root, text = 'Pa', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    protactinium.grid(row=10,column=6)

    uranium=Button(root, text = 'U', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    uranium.grid(row=10,column=7)

    neptunium=Button(root, text = 'Np', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    neptunium.grid(row=10,column=8)

    plutonium=Button(root, text = 'Pu', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    plutonium.grid(row=10,column=9)

    americium=Button(root, text = 'Am', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    americium.grid(row=10,column=10)

    curium=Button(root, text = 'Cm', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    curium.grid(row=10,column=11)

    berkelium=Button(root, text = 'Bk', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    berkelium.grid(row=10,column=12)

    californium=Button(root, text = 'Cf', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    californium.grid(row=10,column=13)

    einsteinium=Button(root, text = 'Es', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    einsteinium.grid(row=10,column=14)

    fermium=Button(root, text = 'Fm', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    fermium.grid(row=10,column=15)

    mendelevium=Button(root, text = 'Md', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    mendelevium.grid(row=10,column=16)

    nobelium=Button(root, text = 'No', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    nobelium.grid(row=10,column=17)

    lawrencium=Button(root, text = 'Lr', command=None, bg="firebrick1", bd="7", font=('Verdana', 15), width="3", height="1" ,fg="black", activebackground="firebrick1")
    lawrencium.grid(row=10,column=18)


    Legend=Button(root, text='LEGENDS',command=Legend,bg="black",bd="7",font=('Verdana',16),width="92",height="1",fg="darkviolet",activebackground="black")
    Legend.grid(row=11,column=1,columnspan=650)

    root.mainloop()
        
    

def know():
    root=Toplevel()
    def er():
        y=ex.get()
        cur.execute('select * from PeriodicTable where Atomic_No={}'.format(y))
        z=cur.fetchall()
        for i in z:
            sy=i[0]
            na=i[1]
            an=i[2]
            am=i[3]
            vl=i[4]
            dt=i[5]
            bp=i[6]
            mp=i[7]
            en=i[8]

            
            
        root1=Tk()
        a=Label(root1,text='Symbol',font=('Verdana', 12), relief="solid", width="20", height="2", bg="firebrick1")
        a.grid(row=1,column=1)
        b=Label(root1,text=sy,font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        b.grid(row=1,column=2)
        c=Label(root1,text='Name',font=('Verdana', 12), relief="solid", width="20", height="2", bg="firebrick1")
        c.grid(row=2,column=1)
        d=Label(root1,text=na,font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        d.grid(row=2,column=2)
        e=Label(root1,text='Atomic_No',font=('Verdana', 12), relief="solid", width="20", height="2", bg="firebrick1")
        e.grid(row=3,column=1)
        f=Label(root1,text=an,font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        f.grid(row=3,column=2)
        g=Label(root1,text='Atomic_Mass',font=('Verdana', 12), relief="solid", width="20", height="2", bg="firebrick1")
        g.grid(row=4,column=1)
        h=Label(root1,text=am,font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        h.grid(row=4,column=2)  
        i=Label(root1,text='Valency',font=('Verdana', 12), relief="solid", width="20", height="2", bg="firebrick1")
        i.grid(row=5,column=1)
        j=Label(root1,text=vl,font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        j.grid(row=5,column=2)   
        k=Label(root1,text='Density',font=('Verdana', 12), relief="solid", width="20", height="2", bg="firebrick1")
        k.grid(row=6,column=1)
        k=Label(root1,text=dt,font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        k.grid(row=6,column=2)       
        l=Label(root1,text='Boiling_Point',font=('Verdana', 12), relief="solid", width="20", height="2", bg="firebrick1")
        l.grid(row=7,column=1)
        m=Label(root1,text=bp,font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        m.grid(row=7,column=2)      
        n=Label(root1,text='Melting_Point',font=('Verdana', 12), relief="solid", width="20", height="2", bg="firebrick1")
        n.grid(row=8,column=1)
        o=Label(root1,text=mp,font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        o.grid(row=8,column=2)        
        p=Label(root1,text='Electronegativity',font=('Verdana', 12), relief="solid", width="20", height="2", bg="firebrick1")
        p.grid(row=9,column=1)
        q=Label(root1,text=en,font=('Verdana', 12), relief="solid", width="20", height="2", bg="white")
        q.grid(row=9,column=2)
        
        root1.mainloop()
    Label(root,text='Enter Atomic number of the element to be searched: ',bg='orange').pack()
    ex=IntVar()
    e=Entry(root,textvariable=ex).pack()
    sb=Button(root,text='Submit',command=er,bg='orange').pack()
    root.configure(bg='gainsboro')
    root.mainloop()
Button(root3,text='Show periodic table',command=show,bg="orange", activebackground="orange", bd="7", font=('Verdana', 15), width="18", height="3" , fg="black").place(x=500,y=100)
Button(root3,text="Know about Element",command=know,bg="orange", activebackground="orange", bd="7", font=('Verdana', 15), width="18", height="3" , fg="black").place(x=500,y=250)
root3.mainloop()

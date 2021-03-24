from random import *
from tkinter import *

root = Tk()
root.geometry("400x300+100+100")
root.title("CS First Project by Onuralp Avcı")

def toplam():
    a = int(saat1.get())
    b = int(dakika1.get())
    c = int(saniye1.get())

    if a > 12:
        a= int(a) - 12
    if a == 12:
        a = 0
    k = a*3600+b*60+c
    ak = k/720.0
    ye = k/60.0
    sa = c
    if ye > 60:
        ye = ye%60.0
    akye = abs(ak-ye)*6
    aksa = abs(ak-sa)*6
    saye = abs(sa-ye)*6
    if akye > 180:
        akye = 360-akye
    if aksa > 180:
        aksa = 360-aksa
    if saye > 180:
        saye = 360-saye
    akye = float("{:.2f}".format(akye))
    aksa = float("{:.2f}".format(aksa))
    saye = float("{:.2f}".format(saye))
    akyeL.configure(text="Hour-Minute Hand:      "+str(akye))
    aksaL.configure(text="Hour-Second Hand:     "+str(aksa))
    sayeL.configure(text="Second-Minute Hand:      "+str(saye))



saat = Label(text="HOUR: ", font=20)
saat.grid(row=0, column=0, ipadx = 5, ipady = 5)
saat1 = Entry(root,  font=20)
saat1.grid(row=0, column=1, ipady = 5)

dakika = Label(text="MINUTE: ", font=20)
dakika.grid(row=1, column=0, ipadx = 5, ipady = 5)
dakika1 = Entry(root, font=20)
dakika1.grid(row=1, column=1, ipady = 5)

saniye = Label(text="SECOND: ", font=20)
saniye.grid(row=2, column=0, ipadx = 5, ipady = 5)
saniye1 = Entry(root, font=20)
saniye1.grid(row=2, column=1, ipady = 5)

tamam = Button(root,text="OKAY", font=20, command=toplam)
tamam.grid(row=4, column=1, columnspan=2, ipadx = 5, ipady = 5)

akyeL = Label(text="", font=20)
akyeL.grid(row=5, column=1, ipadx = 5, ipady = 5)

aksaL = Label(text="", font=20)
aksaL.grid(row=6, column=1, ipadx = 5, ipady = 5)

sayeL = Label(text="", font=20)
sayeL.grid(row=7, column=1, ipadx = 5, ipady = 5)
mainloop()

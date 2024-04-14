import turtle
import datetime


ekran = turtle.Screen()
ekran.bgcolor("white")
ekran.setup(width=600,height=600)
ekran.title("Analog Saat")

kalem = turtle.Turtle()
kalem.speed(0)
kalem.width(3)

numara_kalemi = turtle.Turtle()
numara_kalemi.speed(0)
numara_kalemi.color("black")

ibre_kalemi= turtle.Turtle()
ibre_kalemi.speed(0)


def saatCiz(radius,default="white"):
    turtle.hideturtle()
    turtle.penup()
    turtle.goto(0,-90-radius)
    if default != "white":
        turtle.fillcolor(default)
    else:
        turtle.fillcolor(default)

    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius+60)
    turtle.end_fill()

    for i in range(12):
        kalem.penup()
        kalem.goto(0,-35)
        kalem.setheading(90)
        kalem.right(i * 30) 
        kalem.forward(radius)
        kalem.pendown()
        kalem.forward(20)
        kalem.penup()
    kalem.hideturtle()

    renkler= ["red","blue","pink","yellow","purple","orange","green","gray","red","blue","pink","yellow"]

    for i in range(12):
        numara_kalemi.penup()
        numara_kalemi.goto(0,-45)
        numara_kalemi.setheading(90)
        numara_kalemi.right(i*-30)
        numara_kalemi.forward(radius+40)
        numara_kalemi.pendown()
        numara_kalemi.pencolor(renkler[i])
        numara_kalemi.write(12-i,font=("Verdana",15))
        numara_kalemi.penup()
    numara_kalemi.hideturtle()


    def guncelle_saat_ibreleri():
        t = datetime.datetime.now()
        saat = t.hour
        dakika = t.minute
        saniye = t.second

        saat_aci = (saat % 12) * 30 + (dakika / 2)
        dakika_aci = dakika * 6 + (saniye / 10) 
        saniye_aci = saniye * 6

        # Saat ibresi
        ibre_kalemi.clear()
        ibre_kalemi.penup()
        ibre_kalemi.width(5)
        ibre_kalemi.pencolor("green")
        ibre_kalemi.goto(0, 0)
        ibre_kalemi.pendown()
        ibre_kalemi.setheading(90)
        ibre_kalemi.right(saat_aci)
        ibre_kalemi.forward(radius*(1/3))
        ibre_kalemi.penup()

        # Dakika ibresi
        ibre_kalemi.penup()
        ibre_kalemi.width(3)
        ibre_kalemi.pencolor("blue")
        ibre_kalemi.goto(0, 0)
        ibre_kalemi.pendown()
        ibre_kalemi.setheading(90)
        ibre_kalemi.right(dakika_aci)
        ibre_kalemi.forward(radius*(1/2))
        ibre_kalemi.penup()

        # Saniye ibresi
        ibre_kalemi.penup()
        ibre_kalemi.width(1)
        ibre_kalemi.pencolor("red")
        ibre_kalemi.goto(0, 0)
        ibre_kalemi.pendown()
        ibre_kalemi.setheading(90)
        ibre_kalemi.right(saniye_aci)
        ibre_kalemi.forward(radius-30)
        ibre_kalemi.penup()
        ibre_kalemi.hideturtle()

        ekran.ontimer(guncelle_saat_ibreleri, 1000)  # Her saniye güncelle

    guncelle_saat_ibreleri()

saatCiz(200,"pink")

turtle.mainloop()

import turtle
from auto import Auto


ablak = turtle.Screen()
ablak.title("Autóverseny")
ablak.bgcolor("black")

a1 = Auto("red", -400, 0, 10)
a2 = Auto("green", -400, 100, 10)

ablak.listen()
ablak.onkey(ablak.bye, "Escape")
ablak.onkey(a1.indit, "d")
ablak.onkey(a2.indit, "k")

turtle.mainloop()

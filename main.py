
"""

    Nunt OS Lubrix v1.0

    Nunt OS - The fastest Operating System.

    Written in Python 3.9.0 on Windows 10 Pro.
    Created under the permssion of NuntCorp
    with help from Github @OxfordBot.

"""

# OS Info

__author__ = "NuntCorp"
__version__ = 1.0
__name__ = "Lubrix"

# Import modules

import turtle
import tkinter as tk
import time
import random
import tkinter.ttk as ttk
import os

# Essential Variables

blank_space =" "
close = False

# Create screen

screen = turtle.Screen()

# Screen essentials

screen.title(2*blank_space+"Nunt OS")
screen.tracer(0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.resizable(False, False)
canvas.pack(fill = tk.BOTH, expand = True, ipady=0)
root.iconphoto(True, tk.PhotoImage(file="logo.gif"))
root.tk.call('tk', 'scaling', 2.0)
root.config(bg="#101010", bd=-4, highlightthickness=-4, highlightcolor="white")
canvas.config(bd=-2, relief='sunken', bg="#101010", highlightthickness=-2, highlightcolor="white")
screen.register_shape("background.gif")
screen.register_shape("logo2.gif")
screen.register_shape("logo3.gif")
screen.register_shape("profile.gif")
screen.update()    
w = 1250
h= 700
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)    
y = (hs/2.15) - (h/2)
x = int(x)
y = int(y)
screen.setup(w, h, x, y)

# Create pen

pen = turtle.Turtle()

# pen essentials

pen.hideturtle()
pen.penup()
pen.goto(0, 0)
pen.speed(0)

# Create writer

writer = turtle.Turtle()

# writer essentials

writer.hideturtle()
writer.penup()
writer.goto(0, 0)
writer.speed(0)

# Core class

class Core:

    def __init__(self, pen, screen):

        self.pen = pen
        self.screen = screen
        self.animation = [
            "#101010",
            "#101010",
            "#111111",
            "#121212",
            "#131313",
            "#141414",
            "#151515",
            "#161616",
            "#171717",
            "#181818",
            "#191919",
            "#191919"
            ]

        self.circle = 36
        self.loading = 0
        self.percent = 0

    def boot(self):
        
        self.screen.tracer(0)
        
        for num in self.animation:
            self.pen.color(num)
            self.pen.pendown()
            self.pen.begin_fill()
            self.pen.circle(10*self.circle)
            self.pen.end_fill()
            self.pen.penup()
            self.pen.sety((10*self.circle)*(-1))
            self.circle -= 2
            
        self.screen.update()
            
        self.pen.goto(0, 10)
        self.pen.shape("logo2.gif")
        self.pen.stamp()
        self.pen.goto(0, -75)
        self.pen.pendown()
        self.pen.color("#161616")
        self.pen.pensize(6)
        self.pen.goto(-80, -75)
        self.pen.goto(80, -75)
        self.pen.penup()
        self.pen.goto(-80, -75)
        self.pen.color("#FFFFFF")
        self.pen.pendown()
        self.screen.update()

        self.screen.update()

        self.pen.penup()
        self.pen.color("#FFFFFF")
        self.pen.goto(450, -325)
        self.pen.write("F12", font=("Consolas", 10, "bold"))
        self.pen.setx(self.pen.xcor()+40)
        self.pen.write("BIOS Setup", font=("Consolas", 9))
        self.pen.pendown()

        self.screen.tracer(1)

        time.sleep(2)

        self.screen.tracer(0)

        self.pen.clear()
        
        self.pen.penup()
        self.pen.goto(0, 0)

        self.circle = 36

        for num in self.animation:
            self.pen.color(num)
            self.pen.pendown()
            self.pen.begin_fill()
            self.pen.circle(10*self.circle)
            self.pen.end_fill()
            self.pen.penup()
            self.pen.sety((10*self.circle)*(-1))
            self.circle -= 2

        self.screen.update()
            
        self.pen.goto(0, 10)
        self.pen.shape("logo2.gif")
        self.pen.stamp()
        self.pen.goto(0, -75)
        self.pen.pendown()
        self.pen.color("#161616")
        self.pen.pensize(6)
        self.pen.goto(-80, -75)
        self.pen.goto(80, -75)
        self.pen.penup()
        self.pen.goto(-80, -75)
        self.pen.color("#FFFFFF")
        self.pen.pendown()
        self.screen.update()
        
        self.screen.tracer(1)

        time.sleep(1)

        self.percent = 0

        paused = False

        while self.pen.xcor() < 80 and self.loading != 160:
            if paused == True:
                self.screen.update()
            else:
                self.screen.tracer(0)
                if self.loading > 160:
                    self.loading = 160
                    self.percent = 100
                    self.text = "Booting ({}%)".format(self.percent)
                elif self.percent == 0:
                    self.percent = 1
                elif random.randint(1, self.percent) == random.randint(1, self.percent):
                    self.load = 1
                    time.sleep(self.load/1000000000)
                    self.pen.fd(self.load)
                    self.percent = int((self.load/160)*100)
                    self.screen.update()
                self.screen.tracer(1)

        time.sleep(2)

        self.login()

    def login(self):

        self.screen.tracer(0)
        self.pen.clear()
        self.pen.penup()
        self.pen.shape("background.gif")
        self.pen.stamp()
        self.pen.goto(20, 0)
        self.pen.pendown()
        self.pen.color("#FFFFFF")
        self.pen.penup()
        self.pen.goto(0, 50)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.fd(150)
        for self.right in range(90):
            self.pen.fd(0.5)
            self.pen.right(1)
        self.pen.fd(97.5)
        for self.right in range(90):
            self.pen.fd(0.5)
            self.pen.right(1)
        self.pen.fd(300)
        for self.right in range(90):
            self.pen.fd(0.5)
            self.pen.right(1)
        self.pen.fd(97.5)
        for self.right in range(90):
            self.pen.fd(0.5)
            self.pen.right(1)
        self.pen.fd(150)
        self.pen.end_fill()
        self.pen.penup()
        self.pen.goto(self.pen.xcor(), self.pen.ycor())
        self.pen.shape("profile.gif")
        self.pen.stamp()
        self.pen.penup()
        self.pen.goto(-135.00000000000034, -17.499999999998906)
        self.pen.pendown()
        self.pen.begin_fill()
        self.pen.color("#f8f8f8", "#f9f9f9")
        self.pen.fd(135*2)
        for self.right in range(90):
            self.pen.fd(0.25)
            self.pen.right(1)
        self.pen.fd(135/4.5)
        for self.right in range(90):
            self.pen.fd(0.25)
            self.pen.right(1)
        self.pen.fd(135*2)
        for self.right in range(90):
            self.pen.fd(0.25)
            self.pen.right(1)
        self.pen.fd(135/4.5)
        for self.right in range(90):
            self.pen.fd(0.25)
            self.pen.right(1)
        self.pen.fd(135)
        self.pen.penup()
        self.pen.end_fill()
        self.screen.update()
        self.screen.tracer(1)

        self.keyboard = Keyboard(password=True,
                                 validation=True)
        self.keyboard.listen()

# Keyboard class

class Keyboard:

    def __init__(self, password=False, validation=False):

        global screen
        global pen
        global writer
        global close

        self.screen = screen
        self.pen = pen
        self.writer = writer
        self.password = password
        self.validation = validation

        self.keyword_nums = 22

        self.close = close
        
        self.keywords = []

    def update(self):

        self.screen.tracer(0)

        with open("keywords.txt", "w") as self.file:
            
            for self.keyword in self.keywords:

                self.file.write(self.keyword)

            self.file.close()

        with open("keywords.txt", "r") as self.file:

            self.content = self.file.read()

            self.file.close()

        os.remove("keywords.txt")

        if self.password == True:

            with open("password.txt", "w") as self.file:

                for self.letter in self.content:

                    self.file.write("•")

                self.file.close()

            with open("password.txt", "r") as self.file:

                self.content = self.file.read()

                self.file.close()

            os.remove("password.txt")

            self.pen.penup()
            self.pen.goto(-135.00000000000034, -17.499999999998906)
            self.pen.pendown()
            self.pen.begin_fill()
            self.pen.color("#f8f8f8", "#f9f9f9")
            self.pen.fd(135*2)
            for self.right in range(90):
                self.pen.fd(0.25)
                self.pen.right(1)
            self.pen.fd(135/4.5)
            for self.right in range(90):
                self.pen.fd(0.25)
                self.pen.right(1)
            self.pen.fd(135*2)
            for self.right in range(90):
                self.pen.fd(0.25)
                self.pen.right(1)
            self.pen.fd(135/4.5)
            for self.right in range(90):
                self.pen.fd(0.25)
                self.pen.right(1)
            self.pen.fd(135)
            self.pen.penup()
            self.pen.end_fill()

            self.writer.color("black")

            self.writer.clear()
            self.writer.penup()
            self.writer.goto(0, -60)
            self.writer.write(self.content, align="center", font=("Calibri", 12))
            self.screen.update()
            
        else:

            self.pen.penup()
            self.pen.goto(-135.00000000000034, -17.499999999998906)
            self.pen.pendown()
            self.pen.begin_fill()
            self.pen.color("#f8f8f8", "#f9f9f9")
            self.pen.fd(135*2)
            for self.right in range(90):
                self.pen.fd(0.25)
                self.pen.right(1)
            self.pen.fd(135/4.5)
            for self.right in range(90):
                self.pen.fd(0.25)
                self.pen.right(1)
            self.pen.fd(135*2)
            for self.right in range(90):
                self.pen.fd(0.25)
                self.pen.right(1)
            self.pen.fd(135/4.5)
            for self.right in range(90):
                self.pen.fd(0.25)
                self.pen.right(1)
            self.pen.fd(135)
            self.pen.penup()
            self.pen.end_fill()

            self.writer.color("black")
            
            self.writer.clear()
            self.writer.penup()
            self.writer.goto(0, -60)
            self.writer.write(self.content, align="center", font=("Calibri", 12))
            self.screen.update()

        self.screen.tracer(1)

    def listen(self):

        self.screen.listen()

        self.screen.onkeypress(self.a, "a")
        self.screen.onkeypress(self.b, "b")
        self.screen.onkeypress(self.c, "c")
        self.screen.onkeypress(self.d, "d")
        self.screen.onkeypress(self.e, "e")
        self.screen.onkeypress(self.f, "f")
        self.screen.onkeypress(self.g, "g")
        self.screen.onkeypress(self.h, "h")
        self.screen.onkeypress(self.i, "i")
        self.screen.onkeypress(self.j, "j")
        self.screen.onkeypress(self.k, "k")
        self.screen.onkeypress(self.l, "l")
        self.screen.onkeypress(self.m, "m")
        self.screen.onkeypress(self.n, "n")
        self.screen.onkeypress(self.o, "o")
        self.screen.onkeypress(self.p, "p")
        self.screen.onkeypress(self.q, "q")
        self.screen.onkeypress(self.r, "r")
        self.screen.onkeypress(self.s, "s")
        self.screen.onkeypress(self.t, "t")
        self.screen.onkeypress(self.u, "u")
        self.screen.onkeypress(self.v, "v")
        self.screen.onkeypress(self.w, "w")
        self.screen.onkeypress(self.x, "x")
        self.screen.onkeypress(self.y, "y")
        self.screen.onkeypress(self.z, "z")
        self.screen.onkeypress(self.enter, "Return")
        self.screen.onkeypress(self.backspace, "BackSpace")

    def backspace(self):

        self.screen.tracer(0)

        if len(self.keywords) == 0:
            pass
         
        else:
            self.keywords.remove(self.keywords[len(self.keywords)-1])

        self.update()

        self.screen.tracer(1)

    def enter(self):

        self.screen.tracer(0)

        if self.validation == True:

            self.update()

            self.passwords = ""

            for self.keyword in self.keywords:

                self.passwords += str(self.keyword)

            self.screen.tracer(1)

            if self.passwords == "nmscasm":

                pass

            else:

                self.screen.tracer(0)

                self.pen.penup()
                self.pen.goto(-135.00000000000034, -17.499999999998906)
                self.pen.pendown()
                self.pen.begin_fill()
                self.pen.color("#FF7F7F")
                self.pen.fd(135*2)
                for self.right in range(90):
                    self.pen.fd(0.25)
                    self.pen.right(1)
                self.pen.fd(135/4.5)
                for self.right in range(90):
                    self.pen.fd(0.25)
                    self.pen.right(1)
                self.pen.fd(135*2)
                for self.right in range(90):
                    self.pen.fd(0.25)
                    self.pen.right(1)
                self.pen.fd(135/4.5)
                for self.right in range(90):
                    self.pen.fd(0.25)
                    self.pen.right(1)
                self.pen.fd(135)
                self.pen.penup()
                self.pen.end_fill()
                self.screen.update()

                self.writer.color("white")
                self.writer.penup()
                self.writer.write(self.content, align="center", font=("Calibri", 12))

                self.screen.tracer(1)

    def a(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("a")
            self.update()

    def b(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("b")
            self.update()

    def c(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("c")
            self.update()

    def d(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("d")
            self.update()

    def e(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("e")
            self.update()

    def f(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("f")
            self.update()

    def g(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("g")
            self.update()

    def h(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("h")
            self.update()

    def i(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("i")
            self.update()

    def j(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("j")
            self.update()

    def k(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("k")
            self.update()

    def l(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("l")
            self.update()

    def m(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("m")
            self.update()

    def n(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("n")
            self.update()

    def o(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("o")
            self.update()

    def p(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("p")
            self.update()

    def q(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("q")
            self.update()

    def r(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("r")
            self.update()

    def s(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("s")
            self.update()

    def t(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("t")
            self.update()

    def u(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("u")
            self.update()

    def v(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("v")
            self.update()

    def w(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("w")
            self.update()

    def x(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("x")
            self.update()

    def y(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("y")
            self.update()

    def z(self):

        if len(self.keywords) < self.keyword_nums:

            self.keywords.append("z")
            self.update()

Core(pen, screen).boot()

screen.mainloop()

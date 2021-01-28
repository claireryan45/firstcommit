from tkinter import *
from time import *
from random import *
import turtle
app = Tk()
labels = []
frame = Frame(app, bg='red', cursor='dot', bd=4)
frame.pack(side='top')
app.title('circle game')
t2 = time()
global label
global high_score
high_score = 0
global counter2
counter2 = 0


class APP(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.createwidget()

    def createovalbutton(self):
        for a in labels:
            if type(a) == Label or type(a) == Button:
                a.destroy()
            else:
                canvas.delete(a)
        global counter2
        counter2 = 0
        xpos = randint(1, 360)
        ypos = randint(1, 360)
        global oval
        oval = canvas.create_oval(xpos, ypos, xpos+20, ypos+20, fill='blue')
        global time1
        time1 = time()
        labels.append(oval)
        canvas.tag_bind(oval, '<ButtonPress-1>', self.button1)

    def createwidget(self):
        app.minsize(108, 72)
        app.maxsize(1080, 720)
        global counter2
        counter2 = 0
        global canvas
        canvas = Canvas(frame, width=1080, height=600)
        global label2
        label2 = Label(frame, text='Start Page')
        label2.pack(side='left')
        labels.append(label2)
        canvas.pack()
        global button
        button = Button(frame, text='Start Button', command=self.createovalbutton)
        labels.append(button)
        button.pack()

    def button1(self, event):
        global counter2
        global time2
        time2 = time()
        for a in labels:
            if type(a) == Label or type(a) == Button:
                a.destroy()
            else:
                canvas.delete(a)
        global time1
        if time2 - time1 < 2:
            if counter2 < 10:
                counter2 += 1
                global label
                label = Label(frame, text=counter2)
                labels.append(label)
                label.pack(side='left')
                xpos = randint(1, 1040)
                ypos = randint(1, 560)
                global oval
                time1 = time()
                oval = canvas.create_oval(xpos, ypos, xpos + 20, ypos + 20, fill='blue')
                canvas.tag_bind(oval, '<ButtonPress-1>', self.button1)
                labels.append(oval)
            elif counter2 >= 10:
                self.medium(event)
        else:
            self.delete()

    def medium(self, event):
        global counter2
        global time2
        time2 = time()
        for a in labels:
            if type(a) == Label or type(a) == Button:
                a.destroy()
            else:
                canvas.delete(a)

        global time1
        if time2 - time1 < 2:
            if counter2 < 20:
                counter2 += 1
                global label
                label = Label(frame, text=counter2)
                labels.append(label)
                label.pack(side='left')
                xpos = randint(1, 1040)
                ypos = randint(1, 560)
                xpos2 = randint(1, 1040)
                ypos2 = randint(1, 560)
                global oval
                time1 = time()
                oval = canvas.create_oval(xpos, ypos, xpos + 20, ypos + 20, fill='blue')
                oval2 = canvas.create_oval(xpos2, ypos2, xpos2 + 20, ypos + 20, fill='green')
                l = [oval, oval2]
                canvas.tag_bind(choice(l), '<ButtonPress-1>', self.medium)
                labels.append(oval)
                labels.append(oval2)
            elif counter2 == 20:
                self.hard(event)
        else:
            self.delete()

    def hard(self, event):
        global counter2
        global time2
        time2 = time()
        for a in labels:
            if type(a) == Label or type(a) == Button:
                a.destroy()
            else:
                canvas.delete(a)
        global time1
        if time2 - time1 < 2:
            if counter2 < 30:
                counter2 += 1
                global label
                label = Label(frame, text=counter2)
                labels.append(label)
                label.pack(side='left')
                xpos = randint(1, 1040)
                ypos = randint(1, 560)
                xpos2 = randint(1, 1040)
                ypos2 = randint(1, 560)
                xpos3 = randint(1, 1040)
                ypos3 = randint(1, 560)
                global oval
                time1 = time()
                oval = canvas.create_oval(xpos, ypos, xpos + 20, ypos + 20, fill='blue')
                oval2 = canvas.create_oval(xpos2, ypos2, xpos2 + 20, ypos + 20, fill='green')
                rect = canvas.create_rectangle(xpos3, ypos3, xpos3 + 40, ypos + 40, fill='red')
                l = [oval, oval2, rect]
                canvas.tag_bind(choice(l), '<ButtonPress-1>', self.hard)
                labels.append(oval)
                labels.append(oval2)
                labels.append(rect)
            elif counter2 == 30:
                self.extra()
        else:
            self.delete()

    def extra(self):
        screen = turtle.Screen()
        screen.colormode(255)
        screen.bgcolor("black")
        t = turtle.Turtle()
        t.speed(1000)

        t.color("white")
        for i in range(20):
            x = randint(-250, 250)
            y = randint(-250, 250)
            t.penup()
            t.goto(x, y)
            t.pendown()
            size = randint(2, 8)
            for i in range(5):
                t.forward(size)
                t.backward(size)
                t.left(72)
    # --------------------------------
        for i in range(10):
            x = randint(-250, 250)
            y = randint(-250, 250)
            t.penup()
            t.goto(x, y)
            t.pendown()
            r = randint(0, 255)
            g = randint(0, 255)
            b = randint(0, 255)
            t.color(r, g, b)

            size = randint(30, 200)
            for i in range(36):
                t.forward(size)
                t.backward(size)
                t.left(10)
        t.clear()
        t.write('You Have successfully beaten the game', align='center')

    def delete(self):
        for a in labels:
            if type(a) == Label or type(a) == Button:
                a.destroy()
            else:
                canvas.delete(a)
        global high_score
        if counter2 >= high_score:
            canvas.delete(all)
            canvas.create_text(200, 20, fill='darkblue', text='You bet or equaled the Previous High Score ')
            high_score = counter2
            canvas.create_text(40, 30, fill='darkblue', text='you scored ' + str(counter2))

        elif counter2 < high_score:
            canvas.create_text(100, 100, text='You lost better luck next time ')


app = APP()
app.master.title('Circle Game ')

app.mainloop()

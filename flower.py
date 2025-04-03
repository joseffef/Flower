import turtle as tr

layer = tr.Screen()

tr.setup(800, 800)
layer.bgcolor('#262626')
tr.pencolor('#540d6e')
tr.speed(0)
tr.tracer(100)
tr.pensize(1)

a = ('#FF78C4', '#97DBAE', '#C1EFFF', '#F0B86E')

for i in range(3):
    for n in range(400):
        tr.color(a [n % 4])
        tr.circle(190 - n / 2 , 90)
        tr.left(90)
        tr.circle(190 - n / 2 , 90)
        tr.color(a [n % 4])

    tr.left(30)

layer.exitonclick()        

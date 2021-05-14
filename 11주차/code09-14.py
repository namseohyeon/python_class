from myTurtle import *
import turtle
instr=''
swidth,sheight=300,300
tX,tY,tAngle,tSize=[0]*4

turtle.title('거북이 글자쓰기(모듈버전)')
turtle.shape('turtle')
turtle.setup(width=swidth+50, height=sheight+50)
turtle.screensize(swidth,sheight)
turtle.penup()
turtle.speed(5)

instr=getString()

for ch in instr :
    tX,tY,tAngle,txtsize=getXYAS(swidth,sheight)
    r,g,b=getRGB()

    turtle.goto(tX,tY)
    turtle.left(tAngle)

    turtle.pencolor((r,g,b))
    turtle.write(ch,font=('맑은고딕',txtsize,'bold'))
turtle.done()
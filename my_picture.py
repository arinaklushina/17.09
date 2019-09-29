from graphics import *
w = GraphWin("MyWin", 1000, 1000)

l_0 = Rectangle(Point(0,500), Point(1000, 1000))
l_0.draw(w)
l_0.setFill("#339900")
l_00 = Rectangle(Point(0, 0), Point(1000, 500))
l_00.draw(w)
l_00.setFill("#99FFFF")

def domik(x=0,y=0,k=1,color_dom='#FF9900',color_wind='#6666FF',color_roof='#FFFF00',color_left_eye='blue',color_right_eye='blue',t1=True,t2=True,t3=True,t4=True):
    a = x+100
    b = y+200

    r_1 = Rectangle(Point(a,b), Point(a+k*200, b+k*220))           #коробка дома

    r_1.draw(w)
    r_1.setFill(color_dom)

    r_2 = Rectangle(Point(a+k*50, b+k*75), Point(a+k*150, b+k*175))           #окно
    r_2.setWidth(k*6)
    r_2.draw(w)
    r_2.setFill(color_wind)


    p = Polygon(Point(a-k*50,b), Point(a+k*100,b-k*150), Point(a+k*250,b))       #крыша
    p.setWidth(k*7)
    p.draw(w)
    p.setFill(color_roof)


    c_1 = Circle(Point(a+k*50, b-k*50), k*20)
    c_2 = Circle(Point(a+k*150, b-k*50), k*20)
    c_1.setWidth(k*8)    
    c_2.setWidth(k*8)

    if t1==True:
        c_1.draw(w)
    if t2==True:
        c_2.draw(w)

    c_1.setFill(color_left_eye)
    c_2.setFill(color_right_eye)


    l_1 = Line(Point(a-k*50,b-k*150), Point(a,b-k*75))
    l_2 = Line(Point(a+k*200, b-k*75), Point(a+k*250, b-k*150))

    if t3==True:
        l_1.draw(w)
    if t4==True:
        l_2.draw(w)

    l_3 = Line(Point(a+k*100, b+k*75), Point(a+k*100, b+k*175))
    l_4 = Line(Point(a+k*50, b+k*125), Point(a+k*150, b+k*125))
    l_3.setWidth(k*5)
    l_4.setWidth(k*5)

    l_3.draw(w)
    l_4.draw(w)



def girl(x=0,y=0,k=1,color_head='#fac3b5',color_body='#d0608b'):
    a = x+50
    b = y+250
    g_head = Circle(Point(a, b), k*25)
    g_body = Polygon(Point(a, b+k*25), Point(a+k*30, b+k*140), Point(a-k*30, b+k*140))
    g_head.setFill(color_head)
    g_body.setFill(color_body)

    g_head.draw(w)
    g_body.draw(w)


def sun (x=100,y=100,k=1):
    sun = Circle(Point(x,y), k*50)
    sun.draw(w)
    sun.setFill("#FFCC00")


def tree(x=0,y=0,k=1,color_floor='green',color_trunk='brown'):
    a = x+300
    b = y+200
    g_trunk = Rectangle(Point(a,b), Point(a+k*50, b+k*290))
    g_floor1 = Polygon(Point(a-k*120, b+k*220), Point(a+k*190, b+k*220), Point(a+k*25, b+k*100))
    g_floor2 = Polygon(Point(a-k*90, b+k*140), Point(a+k*140, b+k*140), Point(a+k*25, b+k*40))
    g_floor3 = Polygon(Point(a-k*60, b+k*70), Point(a+k*110, b+k*70), Point(a+k*25, b-k*40)) 
    g_trunk.setFill(color_trunk)
    g_floor1.setFill(color_floor)
    g_floor2.setFill(color_floor)
    g_floor3.setFill(color_floor)


    g_trunk.draw(w)
    g_floor1.draw(w)
    g_floor2.draw(w)
    g_floor3.draw(w)


domik(300,450,1,'brown','cyan','white','blue','blue',True,False,False,True)
domik(600,100,0.7)
domik(0,100,0.5,'orange','pink','brown')

girl(200,450,2)

sun(500,60,3)

tree(0,0,0.5)
tree(80,0,0.5)
tree(120,50,0.7)
tree(200,60,0.8)
tree(300,100,0.9)
tree(50,300,0.4)
tree(400,400,1.2)


w.getMouse()
w.close()

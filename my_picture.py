from graphics import *
w = GraphWin("MyWin", 400, 400)

r_1 = Rectangle(Point(100, 200), Point(300, 390))

r_1.draw(w)
r_1.setFill("#FF9900")

r_2 = Rectangle(Point(150, 245), Point(250, 345))
r_2.setWidth(6)
r_2.draw(w)
r_2.setFill("#6666FF")


p = Polygon(Point(50,200), Point(200,50), Point(350,200))
p.setWidth(10)
p.draw(w)
p.setFill("#FFFF00")


c_1 = Circle(Point(150, 150), 20)
c_2 = Circle(Point(250, 150), 20)
c_1.setWidth(8)
c_2.setWidth(8)

c_1.draw(w)
c_2.draw(w)

c_1.setFill("#FFFFFF")
c_2.setFill('#FFFFFF')

#girl
g_head = Circle(Point(50, 250), 25)
g_body = Polygon(Point(50, 275), Point(80, 390), Point(20, 390))
g_head.setFill("#FFCC66")
g_body.setFill('#006633')

g_head.draw(w)
g_body.draw(w)


l_1 = Line(Point(50,50), Point(100, 125))
l_2 = Line(Point(300, 125), Point(350, 50))


l_1.draw(w)
l_2.draw(w)

l_3 = Line(Point(200, 245), Point(200, 345))
l_4 = Line(Point(150, 295), Point(250, 295))
l_3.setWidth(5)
l_4.setWidth(5)

l_3.draw(w)
l_4.draw(w)

w.getMouse()
w.close()

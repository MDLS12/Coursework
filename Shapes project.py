from graphics import *

def drawpolygon(topleft,  bottomleft, bottommiddle, topmiddle, topright, bottomright, colour1, win):
    polygon=Polygon(topleft,  bottomleft, bottommiddle, topmiddle, topright, bottomright)
    polygon.draw(window)
    polygon.setFill(colour1)
    polygon.setOutline(colour1)

def drawpolygon(topleft,  bottomleft, bottommiddle, topmiddle, topright, bottomright, colour3, win):
    polygon=Polygon(topleft,  bottomleft, bottommiddle, topmiddle, topright, bottomright)
    polygon.draw(win)
    polygon.setFill(colour3)
    polygon.setOutline(colour3)

def drawpolygonoutline(topleft,  bottomleft, bottommiddle, topmiddle, topright, bottomright, colour3, win):
    polygon=Polygon(topleft,  bottomleft, bottommiddle, topmiddle, topright, bottomright)
    polygon.draw(win)
    polygon.setOutline(colour1)

def drawpolygonoutline(topleft,  bottomleft, bottommiddle, topmiddle, topright, bottomright, colour3, win):
    polygon=Polygon(topleft,  bottomleft, bottommiddle, topmiddle, topright, bottomright)
    polygon.draw(win)
    polygon.setOutline(colour3)

def drawrectangle(topleft, bottomright, colour2, win):
    
    r = Rectangle(topleft, bottomright)
    r.draw(win)
    r.setFill(colour2)
    r.setOutline(colour2)

def drawarrows(xincrease, yincrease, colour1, window):

    yincrease=0
    yincrease2=0
    yincrease3=0

    for z in range (5):
        for y in range(9):
            for x in range (3):
                for i in range (0, 20*5, 20): 
                    topleft= Point(0+i+xincrease, 0+yincrease3)
                    bottomleft=Point(0+i+xincrease, 10+yincrease3)
                    bottommiddle=Point(10+i+xincrease,20+yincrease3)
                    bottomright= Point(20+i+xincrease, 10+yincrease3)
                    topright=Point(20+i+xincrease,0+yincrease3)
                    topmiddle=Point(10+i+xincrease, 10+yincrease3)
                    drawpolygon(topleft,  bottomleft, bottommiddle, bottomright, topright, topmiddle,colour1, window)
                            
                yincrease3=40+yincrease3
                    
            yincrease3=yincrease3-20
        xincrease=200+xincrease
        yincrease3=yincrease3-700
    yincrease3=0
    xincrease=0

    for z in range (5):
        for y in range (9):   
            for x in range (2):
                
                for i in range (0, 40*3, 40):
                    topleft= Point(0+i+xincrease, 20+yincrease2)
                    bottomleft=Point(0+i+xincrease, 30+yincrease2)
                    bottommiddle=Point(10+i+xincrease,40+yincrease2)
                    bottomright= Point(20+i+xincrease, 30+yincrease2)
                    topright=Point(20+i+xincrease,20+yincrease2)
                    topmiddle=Point(10+i+xincrease, 30+yincrease2)
                    drawpolygon(topleft,  bottomleft, bottommiddle, bottomright, topright, topmiddle, colour1, window)
                for i in range (0, 40*2, 40):
                    topleft= Point(20+i+xincrease,20+yincrease2)
                    bottomleft=Point(20+i+xincrease,30+yincrease2)
                    bottommiddle=Point(30+i+xincrease,40+yincrease2)
                    bottomright= Point(30+i+xincrease,30+yincrease2)
                    topright=Point(40+i+xincrease,20+yincrease2)
                    topmiddle=Point(40+i+xincrease,30+yincrease2)
                    drawpolygonoutline(topleft,  bottomleft, bottommiddle, topmiddle, topright, bottomright, colour1, window)

                yincrease2=40+yincrease2
            yincrease2=yincrease2+20
        xincrease=200+xincrease
        yincrease2=yincrease2-700
                   
    
def drawarrows2(xincrease, yincrease, colour3, window):

    xincrease=0
    yincrease2=0
    yincrease3=0

    for z in range (4):
        for y in range (8):
            for x in range (3):

                for i in range (0, 20*5, 20):
                    topleft= Point(100+i+xincrease, 100+yincrease3)
                    bottomleft=Point(100+i+xincrease, 110+yincrease3)
                    bottommiddle=Point(110+i+xincrease,120+yincrease3)
                    bottomright= Point(120+i+xincrease, 110+yincrease3)
                    topright=Point(120+i+xincrease,100+yincrease3)
                    topmiddle=Point(110+i+xincrease, 110+yincrease3)
                    drawpolygon(topleft,  bottomleft, bottommiddle, bottomright, topright, topmiddle,colour3, window)
                            
                yincrease3=40+yincrease3
                
            yincrease3=yincrease3-20
        xincrease=200+xincrease
        yincrease3=yincrease3-600
    xincrease=0
    yincrease3=0
        
    for z in range (4):
        for y in range (8):   

            for x in range (2):
                
                for i in range (0, 40*3, 40):
                    topleft= Point(100+i+xincrease, 120+yincrease2)
                    bottomleft=Point(100+i+xincrease, 130+yincrease2)
                    bottommiddle=Point(110+i+xincrease,140+yincrease2)
                    bottomright= Point(120+i+xincrease, 130+yincrease2)
                    topright=Point(120+i+xincrease,120+yincrease2)
                    topmiddle=Point(110+i+xincrease, 130+yincrease2)
                    drawpolygon(topleft,  bottomleft, bottommiddle, bottomright, topright, topmiddle, colour3, window)
                for i in range (0, 40*2, 40):
                    topleft= Point(120+i+xincrease, 120+yincrease2)
                    bottomleft=Point(120+i+xincrease, 130+yincrease2)
                    bottommiddle=Point(130+i+xincrease,140+yincrease2)
                    bottomright= Point(130+i+xincrease, 130+yincrease2)
                    topright=Point(140+i+xincrease,120+yincrease2)
                    topmiddle=Point(140+i+xincrease, 130+yincrease2)
                    drawpolygonoutline(topleft,  bottomleft, bottommiddle, topmiddle, topright, bottomright, colour3, window)

                yincrease2=40+yincrease2
            yincrease2=yincrease2+20    
        xincrease=200+xincrease
        yincrease2=yincrease2-600
        
def p1():
    patchwork = int(input("Please enter the size of the patchwork: "))
    colour1= (input("Please enter the first colour: "))
    colour2= (input("Please enter the second colour: "))
    colour3= (input("Please enter the third colour: "))

    patchwork= patchwork * 100
    window=GraphWin("polygon", patchwork, patchwork)

    yincrease=0
    xincrease=0


#Penultimate Graphic

    drawarrows(xincrease, yincrease, colour1, window)

    drawarrows2(xincrease, yincrease, colour3, window)
    
#Final digit graphic
    xincrease=0
    xincrease2=0
    xincrease3=0
    xincrease4=0
    xincrease5=0
    xincrease6=0
    xincrease7=0
    xincrease8=0


    for x in range (8):

        for i in range (0,10*10, 10):
            topleft= Point(100+i+xincrease,90-i)
            bottomright=Point(110+i+xincrease,100-i)
            drawrectangle(topleft, bottomright, colour2, window)
        
        xincrease=100+xincrease
    for x in range (7):

        for i in range (0,10*10, 10):
            topleft= Point(200+i+xincrease2,190-i)
            bottomright=Point(210+i+xincrease2,200-i)
            drawrectangle(topleft, bottomright, colour2, window)
        
        xincrease2=100+xincrease2
    for x in range (6):
         
        for i in range (0,10*10, 10):
            topleft= Point(300+i+xincrease3,290-i)
            bottomright=Point(310+i+xincrease3,300-i)
            drawrectangle(topleft, bottomright, colour2, window)
        
        xincrease3=100+xincrease3
    for x in range (5):

        for i in range (0,10*10, 10):
            topleft= Point(400+i+xincrease4,390-i)
            bottomright=Point(410+i+xincrease4,400-i)
            drawrectangle(topleft, bottomright, colour2, window)
        
        xincrease4=100+xincrease4
    for x in range (4):

        for i in range (0,10*10, 10):
            topleft= Point(500+i+xincrease5,490-i)
            bottomright=Point(510+i+xincrease5,500-i)
            drawrectangle(topleft, bottomright, colour2, window)
        
        xincrease5=100+xincrease5
    for x in range (3):

        for i in range (0,10*10, 10):
            topleft= Point(600+i+xincrease6,590-i)
            bottomright=Point(610+i+xincrease6,600-i)
            drawrectangle(topleft, bottomright, colour2, window)
        
        xincrease6=100+xincrease6
    for x in range (2):

        for i in range (0,10*10, 10):
            topleft= Point(700+i+xincrease7,690-i)
            bottomright=Point(710+i+xincrease7,700-i)
            drawrectangle(topleft, bottomright, colour2, window)
        
        xincrease7=100+xincrease7
    for x in range (1):

        for i in range (0,10*10, 10):
            topleft= Point(800+i+xincrease8,790-i)
            bottomright=Point(810+i+xincrease8,800-i)
            drawrectangle(topleft, bottomright, colour2, window)
        
        xincrease8=100+xincrease4
p1()

            




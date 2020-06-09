#this program to calculate fluid requirement intraop
w = float(input("give the weight? "))
t = float(input("how many hours pt not on maintainance? "))

o = float(input("how much on going loss ?  "))
def fluidmaintainance421(w):
    if w>20:
        w=60+(w-20)
    else:
        if w<=10:
            w=w*4
        else:
            w = 40 + ((w-10)*2)
    return w
    
def deficit(t):
	d = 0
	d = fluidmaintainance421(w)*t
	return d
	
def ongoing(o):
	o = o*w
	return o
	
def hourly ():
	first = 0
	second = 0
	third = 0
	
	first = fluidmaintainance421(w)+0.5*deficit(t)+ ongoing(o)
	
	print("first hour fluid : ",first, " cc/h ")
	
	second = fluidmaintainance421(w)+0.25*deficit(t)+ongoing(o)
	
	print("second hour fluid : ", second, " cc/h")
	
	print ("third hour fluid : ", second," cc/h" )
	
	third = fluidmaintainance421(w)+ongoing(o)
	
	print ("4th hour fluid : ", third, " cc/h")
	
	
hourly()


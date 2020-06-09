#calculatedrug

def getWeight(w):
	w=float(input("give weight please "))
	return w
#to take weight n calculaebdose between range	
def calDose(name, weight,y,z):
	name= name 
	dose1=weight*y
	dose1=round(dose1, 2)
	dose2=weight*z
	dose2=round(dose2, 4)
	print ("	", name, "dose ", dose1, " - ", dose2, " mg")
	print(" ")
	
def calDose1(name, weight,y,z):
	name= name 
	dose1=weight*y
	dose1=round(dose1, 2)
	dose2=weight*z
	dose2=round(dose2, 2)
	
	print ("	", name, "dose ", dose1, " - ", dose2, " mcg")
	print(" ")
	


	
def main():
	w=0
	w=getWeight(w)
	
	print ("induction agent")
	
	print("")
	calDose("propofol", w, 2.0,4.0)
	calDose("STP", w, 3.0, 6.0)
	calDose("ketamine", w,1.0,3.0)
	calDose("ketamine iv sedation", w, 0.2,0.75)
	calDose("midazolam ", w, 0.1,0.2)
	calDose("ethomidate", w, 0.2,0.3)
	
	print ("analgesia")
	
	calDose1("fentanyl", w, 1.0,2.0)
	calDose("morphine ", w, 0.1,0.2)
	calDose("supp pcm", w, 30.0,40.0)
	calDose("voren" , w, 1.0, 1.0)
	
	print ("muscle relaxant ")
	calDose("rocuronium ", w, 0.6,1.2)
	calDose("rocuronium maintainace ", w,0,0.1)
	calDose("suxamethonium", w, 1.0,2.0)
	calDose("atracurium", w, 0,0.5)
	
	print("emergency drug")
	
	calDose("ephedrine", w, 0,0.2)
	calDose1("adrenaline", w, 0,10.0)
	calDose("atropine",w, 0.01,0.02)
	
	print("reversal ")
	calDose("neostigmine", w, 0,0.05)
	calDose("glycopyrolate", w,0.0, 0.004)
	
	
	
main()
	
	
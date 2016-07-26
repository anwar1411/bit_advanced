import math
a=int(input("a?"))
b=int(input("b?"))
c=int(input("c?"))
delta=(b**2)-(4*a*c)
if delta>0:
	print((-b+math.sqrt(delta))/(2*a))
	print((-b-math.sqrt(delta))/(2*a))
elif delta==0 :
	print((-b)/(2*a))
else:
	print("pas de solutions")

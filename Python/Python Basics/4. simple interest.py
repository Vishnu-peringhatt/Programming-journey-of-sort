# wap to calculate simple interest
#pnr\100
#p- principle interest n- number of years,  r- rate

p=float(input("the amount of principle interest : "))
n=float(input("the number of years : "))
r=float(input("the rate of interest : "))

SI = (p*n*r)/100

print (" The simple interest is :" , SI)

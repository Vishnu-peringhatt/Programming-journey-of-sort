#wap to take coordinate values of a point from the user and print which quandrant the point lies

x = float(input("enter a value of x axis : "))
y = float(input("enter a vulue for the y axis : "))

coordinate = ((x,y))

if x == 0 and y == 0 :
    print (coordinate , " is origin")

elif x == 0 :
    print ( coordinate , " is on the x axis")
    
elif y == 0 :
    print (coordinate , " is on the y axis")
    
elif x > 0 and y > 0 :
    print (coordinate , " is in the 1st quadrant")

elif x < 0 and y > 0 :
    print (coordinate , "is in the 2nd quadrant")
    
elif x < 0 and y < 0 :
    print ( coordinate , " is in the 3rd quadrant" )

else :
    print ( coordinate ,  " is in the 4th quadrant " )
    

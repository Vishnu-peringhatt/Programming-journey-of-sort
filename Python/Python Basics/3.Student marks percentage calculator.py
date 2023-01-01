#wap to take marks of 5 subjects of a student,
#calculate total marks and percentage (max mark is 100)

M = float(input("enter the mark obtained for maths : "))
S = float(input("enter the marks obtained for science : "))
SS = float(input("enter the marks obtained for social studies: "))
E = float(input("enter the marks obtained for english : "))
H = float(input("enter the marks obtained for hindi : "))

Total = M+S+SS+E+H

print("The percentage of the mark obtainead by the student is " ,Total/5)

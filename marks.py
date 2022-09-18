active = False
while active == False:

    print("please enter your 5 marks below")

#read 5 inputs (missing int( before (input)))
    mark1 = int(input("enter mark 1: "))
    mark2 = int(input("enter mark 2: "))
    mark3 = int(input("enter mark 3: "))
    mark4 = int(input("enter mark 4: "))
    mark5 = int(input("enter mark 5: "))



#determine if scores are between 0 and 100, if not, reload program from beginning. (this was missing in the initial version)
    if mark1 < 0 or mark1 > 100 or mark2 < 0 or mark2 > 100 or mark3 < 0 or mark3 > 100 or mark4 < 0 or mark4 > 100 or mark5 < 0 or mark5 > 100:
        print("error: marks must be between 0 and 100")
    else:
        active = True
        
#create array/list with five marks
marksList = [mark1, mark2, mark3, mark4, mark5]

#print the array/list (simply added an asterisk before marksList to create a mathematical expression)
print(*marksList)

#calculate the sum and average
sumOfMarks = sum(marksList)
averageOfMarks = sum(marksList)/5

#display results
print("The sum of your marks is: "+str(sumOfMarks))
print("The average of your marks is: "+str(averageOfMarks))

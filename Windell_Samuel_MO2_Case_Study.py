#Samuel Windell 
#Windell_Samuel_MO2_Case_Study.py 
#This program allows the user to enter names of students along with their Grade Point Average. The program then tells them whether 
#they made the Dean's List or the Honor Roll. 
while True: 
   lastName = str(input("Enter a students last name or \"ZZZ\" to quit. \n")) 
   if lastName == "ZZZ": 
      break 
   else: 
      firstName = str(input("Enter that student's first name. \n")) 
      GPA = float(input("What is %s %s's GPA (Grade Point Average)? \n" % (firstName, lastName))) 
      if GPA >= 3.5: 
         print("%s %s made the Dean's List!" % (firstName, lastName)) 
      elif GPA >= 3.0: 
         print("%s %s made the Honor Roll" % (firstName, lastName)) 
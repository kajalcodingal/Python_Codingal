print("Enter the marks obtained in 4 subjects:")
math = int(input("Math: "))
english = int(input("English: "))
science = int(input("Science: "))
hindi = int(input("Hindi: "))

sum = math+english+science+hindi
perc = (sum/400)*100

print("Sum of subjects is:",sum," and perventage is: ",perc)
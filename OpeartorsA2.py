Amount = int(input("Plaease enter amount to widraw: "))

note1 = Amount//100
note2 = (Amount%100)//50
note3 = (Amount%100)%50//10

print("Note of 100 rupee: ", note1)
print("Note of 50 rupee: ", note2)
print("Note of 10 rupee: ", note3)
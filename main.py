user_input = str(input("Enter a Phrase: "))
txt = user_input.split()

a = ""

for i in txt:
    a = a + str(i[0]).upper()

print(a)    

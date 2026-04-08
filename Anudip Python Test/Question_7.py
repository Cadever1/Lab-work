age = int(input("Enter the age of the candidate: "))
if age>18:
    result= ("You are eligible for voting")

elif age == 18:
    result = ("You can vote now")

else:
    result= ("You are not eligible")

print(result)
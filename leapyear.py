x=int(input("Enter a year:"))
result="leap year" if x%400==0 else "leap year" if x%4==0 and x%100!=0 else "not a leap year"
print(result)
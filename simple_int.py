def calculate_si(principal,rate,time):
    return (principal*rate*time)/100
principal=float(input("Enter principal amount:"))
rate=float(input("Enter rate:"))
time=float(input("Enter time in years:"))

print("Simple Interest :",calculate_si(principal*rate*time))
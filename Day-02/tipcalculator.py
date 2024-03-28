print("welcome to the tip calculator")

t_bill = int(input("What was the total bill : "))

tip = int(input("how much tip you would like to give ? 10, 15, 20 :"))

n_ppl = int(input(" how many people will spit the bill : "))

final_total = t_bill + tip

split = final_total/n_ppl

print(f" Each person should pay {split} rs10000")


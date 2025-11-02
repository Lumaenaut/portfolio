# Write your code here
bubblegum = 202
toffee = 118
ice_cream = 2250
milk_chocolate = 1680
doughnut = 1075
pancake = 80

total = bubblegum + toffee + ice_cream + milk_chocolate + doughnut + pancake

print("Earned amount:")
print("Bubblegum: $202")
print("Toffee: $118")
print("Ice cream: $2250")
print("Milk chocolate: $1680")
print("Doughnut: $1075")
print("Pancake: $80")

print("\nIncome: $", total, sep="")
print("Staff expenses:")
staff_expenses = int(input())
print("Other expenses:")
other_expenses = int(input())

print("Net income: $", total - staff_expenses - other_expenses, sep="")
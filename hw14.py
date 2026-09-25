import random
import math
customers=input("enter the names of customers:")
order_placed=[]
for x in customers.split(","):
    x = x.strip()
    if x not in order_placed:
        order_placed.append(x)
print("customers",order_placed)
random.shuffle(order_placed)
winners = random.sample(order_placed, 2)
def reverse(s):
    result = ""
    for i in s:
        result = i + result
    return result

print("Winner 1:", reverse(winners[0]))
print("Winner 2:", reverse(winners[1]))
total = len(order_placed)
print("Total unique participants:", total)
print("Square root:", round(math.sqrt(total)))
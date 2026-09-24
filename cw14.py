import random
import math
names=input("enter the list of guest invited:")
invited =[]
for x in names.split(","):
    x = x.strip()
    if x not in invited:
        invited.append(x)
print("invited guests:", invited)
random_names = random.choice(invited)
print(random_names)
def reverse(s):
    if len(s) == 0: 
        return s 
    else: 
        return reverse(s[1:]) + s[0] 
  
s=random_names
print("reversed random names:",reverse(s));
unique_count = len(invited)
sqrt_value = math.sqrt(unique_count)
rounded_sqrt = round(sqrt_value)

print("Total number of unique names:", unique_count)
print("Rounded square root:", rounded_sqrt)

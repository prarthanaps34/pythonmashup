rice_price=45;
sugar_price=40;
oil_price=130;
rice=3;
sugar=2.5
oil=1.8
total_rice = rice_price*rice;
print(total_rice)
total_sugar = sugar_price*sugar;
print(total_sugar)
total_oil = oil_price*oil;
print(total_oil)
final_total = total_sugar + total_oil + total_rice;
print(final_total)
final_total=int(final_total);
print(final_total);
final_total=float(final_total);
print(final_total);
import random
delivery_charge=random.randrange(5,10)
print(delivery_charge);
final_bill=final_total+delivery_charge;
print(final_bill ,"is the total bill");



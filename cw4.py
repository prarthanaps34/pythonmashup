fruits=['apple','orange','grapes'];
vegetables=['tomato','chilli','potato']
beverages=['water','coke','orangejuice'];

fruits.append('banana');
print(fruits);

vegetables.insert(1,'cucumber');
print(vegetables);

del beverages[2]
print(beverages);

inventory=[fruits,vegetables,beverages]
print(inventory);

print(fruits[:2]);

print(vegetables[-1]);

length=[len(x) for x in fruits];
print(length);

if 'water' in beverages:
    print("yes,'water' is in list");
    
products=(fruits[0],vegetables[0],beverages[0]);
print(products)





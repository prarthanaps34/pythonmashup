grocery_list = ["milk", "bread", "eggs"]

def add_item(item):
    grocery_list.append(item)


def remove_last_item():
    grocery_list.pop()

add_item("butter")

print("Grocery List after adding an item:")
print(grocery_list)

remove_last_item()

print("\nGrocery List after removing the last item:")
print(grocery_list)

display_item = lambda item: print("Item:", item)

print("\nGrocery Items:")
for item in grocery_list:
    display_item(item)

def count_characters(items):
    if len(items) == 0:
        return 0
    
    return len(items[0]) + count_characters(items[1:])



total_characters = count_characters(grocery_list)
print("\nTotal characters:", total_characters)
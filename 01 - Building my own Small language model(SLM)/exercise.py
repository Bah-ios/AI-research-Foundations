from collections import defaultdict,Counter
# Initialize the nested counter
"""  
print(sales_tracker) """

# Record some sales data: (item_type, size)
sales_tracker = defaultdict(Counter)
sales_data = [
    ('shirt', 'M'),
    ('shirt', 'M'),
    ('shirt', 'L'),
    ('pants', 'S'),
    ('pants', 'M'),
    ('shirt', 'L')
]

# Populate the tracker without checking if keys exist
for item, size in sales_data:
    sales_tracker[item][size] += 1
    print(sales_tracker)

# Output the results
print(sales_tracker)

sales_data = [
    ("shirt", "small"),
    ("shirt", "small"),
    ("shoes", "large"),
    ("Trouser", "baggy"),
    ("Trouser", "Jeans")
]

cars = {}

for item,size in sales_data:
    if item not in cars:
        cars[item] = {}
    if size not in cars[item]:
        cars[item][size] = 0
    cars[item][size] += 1

print(cars) 
# Step 1: Define a list of product IDs, some of which are duplicated
product_ids = ["P100", "P101", "P102", "P101", "P103", "P100", "P104"]

# Step 2: Convert the list to a set to remove duplicates
unique_product_ids = set(product_ids)

# Step 3: Display the unique product IDs
print("Unique product IDs:", unique_product_ids)
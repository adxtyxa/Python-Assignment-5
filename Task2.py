num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"Original list: {num_list}")

extrd_list = num_list[0:5]
print(f"Extracted first five elements: {extrd_list}")

rvrsd_list = list(reversed(extrd_list))
print(f"Reversed extracted list: {rvrsd_list}")
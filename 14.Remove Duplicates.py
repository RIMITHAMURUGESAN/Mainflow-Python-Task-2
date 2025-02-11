def remove_duplicates(lst):
    unique_elements = set()
    new_list = []
    for item in lst:
        if item not in unique_elements:
            unique_elements.add(item)
            new_list.append(item)
    return new_list

lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("List without duplicates:", remove_duplicates(lst))

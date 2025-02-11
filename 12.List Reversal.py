def reverse_list(lst):
    reversed_lst = []
    for i in range(len(lst) - 1, -1, -1):
        reversed_lst.append(lst[i])
    return reversed_lst


lst = list(map(int, input("Enter numbers separated by space: ").split()))
print("Reversed list:", reverse_list(lst))

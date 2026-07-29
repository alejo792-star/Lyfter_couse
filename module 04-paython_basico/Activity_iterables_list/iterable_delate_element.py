my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for element in my_list:
    if element % 2 != 0:
        my_list.remove(element)
        print(f"Removed {element} from the list")

print(f"Final list: {my_list}")
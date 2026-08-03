my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list_final = []

for i in range(len(my_list)):
    if (i % 2 == 0):
        my_list_final.append(i)
        print(f"numbar pair {i}")
print(my_list_final)
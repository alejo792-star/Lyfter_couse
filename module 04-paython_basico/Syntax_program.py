name_user = str(input("what's your name: "))
age_user = int(input("How old are you: "))
if age_user <15:
    print(f"Hello {name_user}, you are a minor.")   
elif age_user <=17:
    print(f"Hello {name_user}, you are an pre-adolescent.")
elif age_user >=18 and age_user < 20:
    print(f"Hello {name_user}, you are an adolescent.")
elif age_user >=20 and age_user < 25:
    print(f"Hello {name_user}, you are a young adult.") 
elif age_user >=25 and age_user <30:
    print(f"Hello {name_user}, you are an adult.")
elif age_user >=30 and age_user < 60:
    print(f"Hello {name_user}, you are a senior adult.")
else:
    print(f"Hello {name_user}, you are a mature adult.")
print("end program")
 


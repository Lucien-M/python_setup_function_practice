#2-1 Create hello() function:
def hello():
    print("Hello user")

#3-1 Call function
hello()


#2-2 Create pack() function:
def pack(arg1, arg2, arg3):
    return [arg1, arg2, arg3]

#3-2 Call function and print output
print(pack("male", 40, "abc"))
print(pack("Dog", "Cat", "monkey"))


#2-3 Create eat_lunch() function:
def eat_lunch(food_list):
    if len(food_list) == 0:
        print("My lunchbox is empty")
    else:
        for i in range(len(food_list)):
            if i == 0:
                print(f"First I eat {food_list[0]}")
            else:
                print(f"Next I eat {food_list[i]}")

#3-3 Call function with various lists:
eat_lunch(["Veggie Burgers", "Sardines", "Pizza"])
eat_lunch(["Avocado and egg sandwich"])
eat_lunch([])


            
import random
#random whole number from 0 to 10
rand_num = random.randint(1,10)

#random float number from 0 to 1
rand_num_0_to_1 = round(random.random())

if rand_num_0_to_1 == 1:
    print("tails")
else:
    print("heads")

print(rand_num_0_to_1)


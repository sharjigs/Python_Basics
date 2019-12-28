# Comparison Operators

print('Greater Than 1 > 2:- ', 1 > 2)
print('Less Than 1 < 2:- ', 1 < 2)
print('Greater Than or equal 1 >= 2:- ', 1 >= 2)
print('Less Than or equal 1 <= 2:- ', 1 <= 2)
print('equal to  1 == 2:- ', 1 == 2)
print('not equal to  1 != 2:- ', 1 != 2)

# Logical Operator

print("Logical AND (1 > 2) and (2 < 3):- ", (1 > 2) and (2 < 3))
print("Logical OR (1 > 2) or (2 < 3):- ", (1 > 2) or (2 < 3))


# IF

if 1 < 2:
    print("Yes !")

if 1 < 2:
    if 2 < 3:
        print("True!")

if 1 < 2:
    print("First Block")
    if 20 < 3:
        print("Second Block")

# IF  and ELSE

if 10 < 2:
    print('Hello Yes !')
else:
    print("Wrong Baby")

# IF & ELSIF & ELSE

if 10 < 2:
    print("Okay")
elif 20 > 3:
    print("Yup")
else:
    print("Both Wrong")

if 10 < 2:
    print("Okay")
elif 20 > 30:
    print("Yup")
else:
    print("Both Wrong")

# For Loop

seq = [1,2,3,4,5,6]

for item in seq:
    print(item)

d = {"Sam": 1, "Frank": 2, "Dan": 3}

for items in d:
    print(items, d[items])

# Tuple 

my_pairs = [(1,2), (3,4), (5,6)]

for item in my_pairs:
    print(item)

for (tup1, tup2) in my_pairs:
    print(tup1)
    print(tup2)

# While Loops
i = 1
while i <5:
     print("i is {}".format(i))
     i = i + 1

# Range Function 
print('Range',range(6))
print('Use of Range',list(range(6)))
print('Get Event Number in Range 0 to 20',list(range(0, 20, 2)))

# List Comprehension
x = [1, 2, 3, 4]
out = []
for num in x:
    out.append(num**2)
print(out)

# optimise for loop

out = [num**3 for num in x ]
print(out)


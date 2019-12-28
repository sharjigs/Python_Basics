
# Problem 1
s = 'django'
print('Display D:- ', s[0])
print('Display O:- ', s[-1])
print('Display Starting to Range:- ', s[:4])
print('Display Middle Data:- ', s[1:4])
print('Display D:- ', s[4:])
print('Reverse String:- ', s[::-1])

# Problems 2
l = [3,7,[1,4,'hello']]
l[2][2] = 'goodbye'
print("Reassign Hello", l)

# Problem 3

d1 = {'simple_key': 'hello'}

d2 = {'k1': {'k2': 'hello'}}

d3 = {'k1':[{'nest_key':['this is deep',['hello']]}]}

print('D1', d1['simple_key'])
print('D2', d2['k1']['k2'])
print('D3', d3['k1'][0]['nest_key'][1][0])


# Problem 4

mylist = [1,1,1,1,1,2,2,2,2,3,3,3,3]

x = set(mylist)
print('Unique Value', x)

# Problem 5

age = 4
name = "summary"

print('Hello my dog name is {} and he is {} years old'.format(name, age))






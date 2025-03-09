# a = [1,2,3,4,5]
# b = []
# for i in a:
#     b.append(i)
# print('a : ', a)
# print('b : ', b)
a = [1,2,3,4,5]
# b = [i*2 for i in a if i == 3]
b = ['even' if i % 2 == 0 else 'odd' for i in a]
print('a : ', a)
print('b : ', b)
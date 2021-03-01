# a = [1, 2, 9, 6, 3, 4]
# for i in a:
#     if i < 5:
#         print(i)

# a = [1, 2, 3, 6, 3, 5, 9]
# b = [1, 6, 4, 3, 5, 4]
# for i in a:
#     for j in b:
#         if i == j:
#             print(i)


# a = {1:10, 2:12, 5:15, 6:16, 3:13, 4:14}
# b = sorted(dict.values(a))
# print(b)


# print(int('ABC', 25))


# def palindrom(string):
#     return string == string[::-1]
# print(palindrom('anna'))



# def a(n):
#     n1 = int(n)
#     n2 = int(n) ** 2
#     n3 = int(n) ** 3
#     n4 = n1 + n2 + n3
#     print(n4)
# print(a(6))

# a = [2, 6, 45, 73, 237, 2596]
# for i in a:
#     if i == 237:
#         break
#         i += 1
#     print(i)



# a = set([1, 3, 5, 7])
# b = set([1, 6, 7, 4])
# print(a - b)

# a = "hfyhfvkjifjih hvghy6g"
# result_a = a.replace('h', 'k')
# print(result_a)
# b = a.count('a')
# print(b)


# x = 5
# y = 6
# x, y = y, x
# print(x, y)


# a = [1, 6, 18, 7, 21 ]
# for i in a:
#     if i % 3 == 0:
#       print(i)


# a = []
# i = 0
# n = 5
# while i < n:
#     a = a + [i]
#     i += 1
# print(a)



# a = [1, 2, 4, 6, 9]
# i = 0
# for n in a:
#     if (n % 2) == 0:
#         i += 1
# print(i)

# a = [1, 2, 3, 4, 5, 6]
# c = i = 0
# n = len(a)
# while n > i:
#     c += (a[i] + 1) % 2
#     i += 1
# print(c)

# a = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
# for i in list(a.keys()):
#     a[i + str(len(i))] = a.pop(i)
# print(a)
#
# a = [8, 7, 6, 5, 4]
# i = 0
#
# while len(a) - 1 > i:
#     a[i] = a[i + 1]
#     i += 1
# a[i] = a[0]
# print(a)

# !
# a = [6, 5, 4, 3, 2]
# for i in len(a):
#     a[-1] = a.pop(0)
#     print(a)


while True:
    x = int(input("1: "))
    y = int(input("2: "))
    a = input("(+, -, /, *): ")
    if a == "o":
        break
    if a == "+":
        print(x + y)
    elif a == "-":
        print(x-y)
    elif a == "/":
        if y != 0:
            print(x / y)
        else:
            print("ошибка")

    elif a == "*":
        print(x * y)
















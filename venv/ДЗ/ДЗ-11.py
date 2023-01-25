# def rect_paral_square(a,b,c):
#     def rect_square (i,j):
#         return i * j
#
#     S = 2 * (rect_square (a,b) + rect_square(a,c) + rect_square(b,c))
#     return S
# print(rect_paral_square(2,4,6))
# print(rect_paral_square(5,8,2))
# print(rect_paral_square(1,6,8))

# S = 0
# def rect_paral_square(a,b,c):
#     def rect_square (i,j):
#         return i * j
#     global S
#     S = 2 * (rect_square (a,b) + rect_square(a,c) + rect_square(b,c))
#     return S
#
# (rect_paral_square(2,4,6))
# print(S)
# (rect_paral_square(5,8,2))
# print(S)
# (rect_paral_square(1,6,8))
# print(S)

def rect_paral_square(a, b, c):
    S = 0

    def rect_square(i, j):
        nonlocal S
        S+= i * j

    rect_square(a, b)
    rect_square(a, c)
    rect_square(b, c)
    return 2 * S


print(rect_paral_square(2, 4, 6))
print(rect_paral_square(5, 8, 2))
print(rect_paral_square(1, 6, 8))

print()
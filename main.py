# a = [[0.1, 0.5, 0.2],
#      [0.25, 0.4, 0.3]]
# b = [[0.6, 0.5, 0.5],
#      [0.9, 0.3, 0.2]]
# c = [[0.1, 0.2, 0.7],
#      [0.3, 0.4, 0.5]]
a = [[]]
resultant = []


def gen_matrix(mat1, value):
    mat2 = []
    for i in range(len(mat1)):
        mat2.append([])
        for j in range(len(mat1[0])):
            mat2[i].append(value)
    return mat2


def printf(matrix):
    for i in matrix:
        print(i)


def union(mat1, mat2):
    for i in range(len(mat1)):
        # resultant.append([])
        for j in range(len(mat1[0])):
            r = mat1[i][j] * mat2[i][j]
            resultant[i][j] = (max(round(r, 2), 0))
    return resultant


resultant = a
aub = union(a, b)
printf(aub)
resultant = a
bua = union(b, a)
print(bua)
resultant = c
aUbuc = union(aub, c)
print(aUbuc)
resultant = c
buc = union(b, c)
aubUc = union(a, buc)
print(aubUc)


def intersection(mat1, mat2):
    for i in range(len(mat1)):
        for j in range(len(mat1[0])):
            # print("j",j)
            r = mat1[i][j] + mat2[i][j]
            resultant[i][j] = (min(round(r, 2), 1.0))
    return resultant


resultant = a
anb = intersection(a, b)
printf(anb)
anbNc = intersection(anb, c)
printf(anbNc)
resultant = b
bnc = intersection(b, c)
aNbnc = intersection(a, bnc)
print(aNbnc)


def multi_identity(mat1):
    mat2 = gen_matrix(mat1, 1)
    resultant = union(mat1, mat2)
    return resultant


mul = multi_identity(a)
print(mul)


def mul_zeroprop(mat1):
    mat2 = gen_matrix(mat1, 0)
    resultant = union(mat1, mat2)
    return resultant


mulz = mul_zeroprop(a)
print(mulz)


def identity(mat1):
    mat2 = gen_matrix(mat1, 1)
    resultant = intersection(mat1, mat2)
    return resultant


id = identity(a)
printf(id)


def zero_identity(mat1):
    mat2 = gen_matrix(mat1, 0)
    resultant = intersection(mat1, mat2)
    return resultant


zi = zero_identity(a)
print(zi)

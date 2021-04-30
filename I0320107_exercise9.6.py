import array
A = array.array('i')

A.append(50)
A.append(-20)
A.append(30)
print(A)
A.insert(1, 40)
A.remove(-20)
print(A)

# menggunakan perintah for
for nilai in A:
    print("%d" % nilai, end=' ')
print()
# menggunakan perintah while
i = 0
while i < len(A):
    print("%d" % A[i], end=' ')
    i += 1
print()
print(A.index(30))


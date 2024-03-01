arrays = []

lengths = []

arraycount = int(input("Enter array count: "))

totalsim = 0


def finddiff(arr1, arr2):
    length = min(lengths[arr1], lengths[arr2])

    for i in range(length):

        if arrays[arr1][i] != arrays[arr2][i]:
            return i

    return length


for i in range(arraycount):

    arraylen = int(input("Enter length of array #" + str(i + 1) + ": "))

    arraydata = list(map(int, input("Enter array: ").split()))

    entry = []

    for j in range(arraylen):
        entry.append(arraydata[j])

    arrays.append(entry)
    lengths.append(arraylen)

print(arrays)

for i in range(arraycount):
    for j in range(i + 1, arraycount):
        totalsim += finddiff(i, j)

print(totalsim)

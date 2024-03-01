table = []

colnames = {}

def takecondition(columnname, operation, value):
    print(columnname, operation, value)
    targetindex = colnames[columnname]
    targetcomparison = False
    if operation == '<':
        targetcomparison = False
    elif operation == '>':
        targetcomparison = True

    i = 0
    length = len(table)
    while i < length:
        if table[i][targetindex] > value != targetcomparison or table[i][targetindex] == value:
            table.pop(i)
            length -= 1
            i -= 1
        i += 1

def sumup():
    total = 0
    for entry in table:
        total += sum(entry)
    return total


row_count, col_count, cond_count = map(int, input("Enter number of rows, columns and conditions: ").split())

inserted_names = list(input("Enter column names: ").split())

for i in range(col_count):
    colnames[inserted_names[i]] = i

for i in range(row_count):
    inserted_row = list(map(int, input("Enter row " + str(i + 1) + ": ").split()))
    table.append(inserted_row)

for i in range(cond_count):
    column, operation, val = input("Enter your filtering condition " + str(i + 1) + ": ").split()
    takecondition(column, operation, int(val))

print(sumup(), table)














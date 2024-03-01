way = []
waylangs = []

employees = int(input("Enter number of employees: "))

languages = list(input("Enter employees' language data: ").split())

languages = languages[:employees]

hierarchy = list(map(int, input("Enter company hierarchy: ").split()))

total_language_barrier = [None] * employees  # whether employees are defined in linear order is not defined


def findbarrier(targlang):
    barr = 0
    for lang in waylangs:
        if lang != targlang:
            barr += 1
    return barr


def processentry(employee):
    print(employee, way, waylangs)
    if employee in way:
        way.pop()
        waylangs.pop()
    else:
        thislang = languages[employee]
        total_language_barrier[employee] = findbarrier(thislang)
        way.append(employee)
        waylangs.append(thislang)


for i in range(1, len(hierarchy) - 1):
    processentry(hierarchy[i] - 1)

print(total_language_barrier)

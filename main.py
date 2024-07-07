students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

students_new = sorted(students)

def average(*args): print([sum(x) / len(x) for x in args])
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
average(*grades) #как мне здесь присвоить имя строки?

result = dict(zip(students_new, average(*grades)))
print(result)

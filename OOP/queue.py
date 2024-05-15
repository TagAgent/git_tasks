class Queue:
     def __init__(self):
         self.data = []

     def put(self, name):
         self.data.append(name)

     def out(self):
         self.data.pop(0)

q1 = Queue()
q1.put("бабушка Валя")
q1.put("дедушка Вася")
q1.put("дядя Сеня")
q1.put("Петя")

print(q1.out())

print(q1.out())

print(q1.out())

print(q1.out())

q1.put("Асан")

print(q1.out())

print(q1.out())
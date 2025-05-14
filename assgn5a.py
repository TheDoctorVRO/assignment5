students = {}
for _ in range(5):
 name = input('enter  name: ')   
 mark = input('enter  marks: ')
 students[name] = mark

for name, mark in students.items():
 print('Mark of',name,'is',mark)

a= input('enter a name')
if a not in students :
   print('Not a student')
else:
  print('marks of', a,'is',students[a])



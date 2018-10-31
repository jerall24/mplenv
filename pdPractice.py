import CourseSetsClass as csc

student = csc.CreateCourseSet(10755271,"Pandas Practice.xlsx",'Export Worksheet')
print(student.returnPennID(),student.returnCourses())

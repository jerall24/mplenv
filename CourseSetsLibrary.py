import CourseSetsClass as csc
import pandas as pd
from pandas import ExcelWriter
import numpy as np

excel_file_name = "Initial Data Pull.xlsx"
sheet_in_excel_file = 'Export Worksheet'
xl = pd.read_excel(excel_file_name, sheetname=sheet_in_excel_file)
list_of_courses = list(set(xl['COURSE_ID']))
list_of_courses.sort()
list_of_courses = tuple(list_of_courses)
list_of_penn_ids = list(set(xl['PENN_ID']))
list_of_penn_ids.sort()
list_of_penn_ids = tuple(list_of_penn_ids)
student_paths = list()
binary_course_list = list()
for pennid_loop in list_of_penn_ids:
   student_paths.append(csc.student_class(pennid_loop,list_of_courses,excel_file_name,sheet_in_excel_file))
for student in range(0,len(student_paths)):
   binary_course_list.append(student_paths[student].returnCourses())
  # print(student_paths[student].returnPennID(), student_paths[student].returnCourses())
aggregated_binary_list = [sum(x) for x in zip(*binary_course_list)]
# print(aggregated_binary_list)
# print(list_of_courses[65])
course_array = np.array(binary_course_list)
course_df = pd.DataFrame(data=course_array,index=list_of_penn_ids,columns=list_of_courses)
writer = pd.ExcelWriter('Student Course Matrix.xlsx')
course_df.to_excel(writer,'Sheet 1',index=True)
#create a  file that will write to an excel sheet the binary listing of the classes with classes as headers
#this is mostly be for reading and efficiency

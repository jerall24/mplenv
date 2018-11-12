import pandas as pd

class student_class:
    def __init__(self,penn_id,list_of_courses,excel_file_name,sheet_in_excel_file):
        #assign penn id to the student
        self.penn_id = int(penn_id)
        self.file_name = pd.read_excel(excel_file_name, sheetname=sheet_in_excel_file)
        self.indices_of_penn_ids = self.file_name['PENN_ID']
        #list of 0 and 1 if the student took the course at that index
        #the 0,1 correspond to the class in the list_of_courses
        self.courseList = [0,]*len(list_of_courses)
        self.populate_courses(list_of_courses,self.file_name)

    def populate_courses(self,list_of_courses,xl):
        start_index = list(xl['PENN_ID']).index(self.penn_id)
        end_index = len(list(xl['PENN_ID']))-1-list(xl['PENN_ID'])[::-1].index(self.penn_id)
        #print(self.penn_id, start_index, end_index)
        for i in range(start_index,end_index+1):
                #self.courseList.append(self.file_name['COURSE_ID'][i])
                #find index of course from file_name.index in list_of_courses
                #change the value of that class at that index in self.courseList to 1
                self.courseList[list_of_courses.index(self.file_name['COURSE_ID'][i])] = 1

    def returnCourses(self):
        return self.courseList

    def returnPennID(self):
        return self.penn_id

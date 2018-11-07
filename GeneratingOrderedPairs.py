import pandas as pd
import ManipulateExcelMatrix as mem
from ManipulateExcelMatrix import CreatePrepJSON

xl = pd.read_excel("psStudent Course Matrix.xlsx",sheetname='Sheet 1')
list_of_courses = list(xl)
dict_of_ordered_pairs = dict()
# test_student = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0]
#makes a list of the binary coding of the student's courses taken
#student = list(xl.iloc[1])

#loop to find the ordered pairs
for ind in xl.index:
    if ind != "Sum":
        # print(ind)
        test_student = list(xl.loc[ind])
        for i in range(0,len(test_student)-2):
            if test_student[i] == 1 and 1 in test_student[i+1:]:
                temp_pair = (test_student.index(1,i),test_student.index(1,i+1))
                # print(temp_pair)
                if temp_pair in dict_of_ordered_pairs.keys():
                    dict_of_ordered_pairs[test_student.index(1,i),test_student.index(1,i+1)] += 1
                else:
                    dict_of_ordered_pairs[test_student.index(1,i),test_student.index(1,i+1)] = 1

#check how to print out the length of the the CreatePrepJSON stuff from MEM file

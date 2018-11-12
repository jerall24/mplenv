import pandas as pd
# import ManipulateExcelMatrix as mem
# from ManipulateExcelMatrix import CreatePrepJSON

def CreateOrderedPairs(export_binary_file_name,sheet_in_excel_file):
    xl = pd.read_excel(export_binary_file_name,sheetname=sheet_in_excel_file)
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
    return dict_of_ordered_pairs,list_of_courses

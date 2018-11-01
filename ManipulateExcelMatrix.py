import CourseSetsLibrary as csl

mem_df = csl.course_df.copy().T
mem_df['Sum'] = mem_df.sum(axis=1)
mem_df = mem_df.sort_values(by='Sum',ascending=False)
mem_df = mem_df.copy().T
# print(list(mem_df.loc['Sum']))
count_of_students_in_course_desc = list(mem_df.loc['Sum'])
courses_desc = list(mem_df)
print(courses_desc)

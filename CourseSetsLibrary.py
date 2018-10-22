import CourseSetsClass as csc
import pandas as pd

xl = pd.read_excel("Initial Data Pull.xlsx", sheetname='Export Worksheet')
list_of_penn_ids = set(xl['PENN_ID'])
print(list_of_penn_ids)

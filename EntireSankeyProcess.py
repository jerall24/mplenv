import CourseSetsLibrary as csl
from CourseSetsLibrary import CreateDataFrame
import ManipulateExcelMatrix as mem
from ManipulateExcelMatrix import CreatePrepJSON
import CreateDiagram as cd
from CreateDiagram import CreateSankeyDiagram

def main():
    excel_file_name = input("What is the name of your file? Caps counts")
    if input('Is the sheet named "Sheet 1"? y/n').lower() == 'n':
        sheet_in_excel_file = input('What is your sheet named?')
    else:
        sheet_in_excel_file = 'Sheet 1'
    export_binary_file_name = "Binary " + excel_file_name
    json_file_name = 'JSON ' + excel_file_name
    try:
        csl.CreateDataFrame(excel_file_name,sheet_in_excel_file,export_binary_file_name)
        mem.CreatePrepJSON(export_binary_file_name,'Sheet 1',json_file_name)
        cd.CreateSankeyDiagram(json_file_name)
    except Exception as e:
        raise

if __name__ == '__main__':
    main()

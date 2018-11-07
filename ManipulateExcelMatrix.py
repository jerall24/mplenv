import CourseSetsLibrary as csl
import pandas as pd
from pandas import ExcelWriter
import GeneratingOrderedPairs as gop
import json
import random


def CreateBinaryExcelDoc():
    mem_df = csl.course_df.copy().T
    mem_df['Sum'] = mem_df.sum(axis=1)
    mem_df = mem_df.sort_values(by='Sum',ascending=False)
    mem_df = mem_df.copy().T
    mem_df = mem_df.replace({0:None})
    # print(list(mem_df.loc['Sum']))
    count_of_students_in_course_desc = list(mem_df.loc['Sum'])
    courses_desc = list(mem_df)
    # mem_df = mem_df.sort_values(by=courses_desc,ascending=False)
    # print([c for c in courses_desc if "MGMT" in c])
    writer = pd.ExcelWriter('pStudent Course Matrix.xlsx')
    mem_df.to_excel(writer,'Sheet 1',index=True)
    writer.close()

def CreatePrepJSON():
    path_counts_dict = gop.dict_of_ordered_pairs.copy()
    path_counts = list(path_counts_dict.values())
    path_count_keys = list(path_counts_dict.keys())
    path_starts = list()
    for index in range(0,len(path_count_keys)):
        path_starts.append(path_count_keys[index][0])
    path_ends = list()
    for index2 in range(0,len(path_count_keys)):
        path_ends.append(path_count_keys[index2][1])
    node_colors = list()
    for color in range(0,len(gop.list_of_courses)):
        node_colors.append('"rgba('+str(random.randint(1,255))+', '+str(random.randint(1,255))+', '+str(random.randint(1,255))+', 0.8)"')
    data = {
        "data": [
    {
        "type": "sankey",
        "domain": {
            "x": [
                0,
                1
            ],
            "y": [
                0,
                1
            ]
        },
        "orientation": "h",
        "valueformat": ".0f",
        "valuesuffix": "TWh",
        "node": {
            "pad": 15,
            "thickness": 15,
            "line": {
                "color": "black",
                "width": 0.5
            },
            "label": gop.list_of_courses,
            "color": node_colors
            },
            "link": {
                "source": path_starts,
                "target": path_ends,
                "value": path_counts,
                "color": ["rgba(0,0,96,0.2)",]*len(path_counts),
                "label": ['""',]*len(path_counts)
            }
        }],
    "layout": {
    "title": "Class of 2018 Student Paths",
    "width": 1118,
    "height": 772,
    "font": {
        "size": 10
    },
    "updatemenus": [
        {
            "y": 1,
            "buttons": [
                {
                    "label": "Light",
                    "method": "relayout",
                    "args": [ "paper_bgcolor", "white" ]
                },
                {
                    "label": "Dark",
                    "method": "relayout",
                    "args": [ "paper_bgcolor", "black"]
                }
            ]
        },
        {
            "y": 0.9,
            "buttons": [
                {
                    "label": "Thick",
                    "method": "restyle",
                    "args": [ "node.thickness", 15 ]
                },
                {
                    "label": "Thin",
                    "method": "restyle",
                    "args": [ "node.thickness", 8]
                }
            ]
        },
        {
            "y": 0.8,
            "buttons": [
                {
                    "label": "Small gap",
                    "method": "restyle",
                    "args": [ "node.pad", 15 ]
                },
                {
                    "label": "Large gap",
                    "method": "restyle",
                    "args": [ "node.pad", 20]
                }
            ]
        },
        {
            "y": 0.7,
            "buttons": [
                {
                    "label": "Snap",
                    "method": "restyle",
                    "args": [ "arrangement", "snap" ]
                },
                {
                    "label": "Perpendicular",
                    "method": "restyle",
                    "args": [ "arrangement", "perpendicular"]
                },
                {
                    "label": "Freeform",
                    "method": "restyle",
                    "args": [ "arrangement", "freeform"]
                },
                {
                    "label": "Fixed",
                    "method": "restyle",
                    "args": [ "arrangement", "fixed"]
                }
            ]
        },
        {
            "y": 0.6,
            "buttons": [
                {
                    "label": "Horizontal",
                    "method": "restyle",
                    "args": [ "orientation", "h" ]
                },
                {
                    "label": "Vertical",
                    "method": "restyle",
                    "args": [ "orientation", "v"]
                }
            ]
        }
    ]
    }
    }
    with open('Student Paths.json', 'w') as outfile:
        json.dump(data,outfile)

def main():
    CreatePrepJSON()

if __name__ == '__main__':
    main()

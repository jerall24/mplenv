import plotly.plotly as py
import json
import plotly.graph_objs as go

def CreateSankeyDiagram(json_file_name):
    with open(json_file_name) as json_file:
        data = json.loads(json_file.read())

    data_trace = dict(
        type='sankey',
        width = 20000,
        height = 1000,
        # #Domain is the aspect ratio really
        # domain = dict(
        #   x =  [0,1],
        #   y =  [0,1]
        # ),
        opacity = .1,
        orientation = "h",
        valueformat = ".0f",
        valuesuffix = " Students",
        arrangement = 'freeform',
        node = dict(
          pad = 5 ,
          thickness = 3,
          line = dict(
            color = "black",
            width = 0.5
          ),
          label =  data['data'][0]['node']['label'],
          color =  data['data'][0]['node']['color']
        ),
        link = dict(
          source =  data['data'][0]['link']['source'],
          target =  data['data'][0]['link']['target'],
          value =  data['data'][0]['link']['value'],
          color = "#DBE0E5",
          line = dict(
            color = ('#74777A'),
            width = .25
            # color = ["#444",]*len(data['data'][0]['link']['source'])
          )
          #don't need the label, just adds extra non-sense in the graph
          #label =  data['data'][0]['link']['label']
      ))

    layout =  dict(
        title = "Class of 2018 Paths by Jérémie Allard",
        #paper_bgcolor = "#fff",
        #plot_bgcolor = "#c7c3c3",
        titlefont = dict(
            size = 15
        ),
        autosize=False,
        font = dict(
          size = 3,
          color = "black"
        )
    )

    fig = dict(data=[data_trace], layout=layout)
    py.iplot(fig, validate=False)

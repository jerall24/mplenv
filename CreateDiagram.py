import plotly.plotly as py
import urllib, json

with open("Student Paths.json") as json_file:
    data = json.loads(json_file.read())

data_trace = dict(
    type='sankey',
    width = 20000,
    height = 500,
    domain = dict(
      x =  [0,1],
      y =  [0,1]
    ),
    orientation = "h",
    valueformat = ".0f",
    valuesuffix = " Students",
    node = dict(
      pad = 15,
      thickness = 5,
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
      label =  data['data'][0]['link']['label']
  ))

layout =  dict(
    title = "Class of 2018 Paths by Jérémie Allard",
    font = dict(
      size = 5
    )
)

fig = dict(data=[data_trace], layout=layout)
py.iplot(fig, validate=False)

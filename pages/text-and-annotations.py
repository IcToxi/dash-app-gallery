import dash

from utils.code_and_show import example_app


dash.register_page(__name__, description="Select text position of annotations")

filename = __name__.split("pages.")[1]


notes = """
### For more information see:
Plotly docs:  

- [How to add text labels and annotations to plots](https://plotly.com/python/text-and-annotations/)


### Contributed by:
This example app was contributed by [Plotly](https://plotly.com/python/)

"""


layout = example_app(filename, notes=notes)

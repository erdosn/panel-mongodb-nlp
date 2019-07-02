# Basicd App For Sentiment Analysis Using TextBlob

### Here are the import statements

```python
### Sentiment Analysis
import panel as pn

from components.app_functions import *

from textblob import TextBlob
from bokeh.models import ColumnDataSource, Title
from bokeh.plotting import figure
```

### Here is the code for the app

```python
text_box1 = pn.widgets.TextInput(name="Input 1 Here", value='this is an example of a good sentence')
text_box2 = pn.widgets.TextInput(name="Input 2 Here", placeholder='compare 2 sentences')

@pn.depends(text_box1.param.value, text_box2.param.value)
def plot_sentiment(sentence1, sentence2=None):
    polarity, subjectivity = get_sentiment(sentence1)
    source = create_data_source(polarity, subjectivity)
    
    # begin plotting
    categories = ['negative polarity', 'positive polarity', 'subjectivity']
    title = "Sentiment Analysis"
    subtitle = f"'{sentence1}'"
    if sentence2:
        subtitle = f"'{sentence1}' VS '{sentence2}'"
    
    
    p = figure(x_range=categories, y_range = (-1, 1), toolbar_location=None, tools="", plot_height=400)
    p.vbar(x='categories', top='values', width=0.9, color='color', alpha=0.5, legend='categories', source=source)
    p.legend.orientation = "horizontal"
    p.legend.location = "top_center"
    p.xgrid.grid_line_color = None
    p.y_range.start = 0
    p.add_layout(Title(text=subtitle, text_font_style="italic"), 'above')
    p.add_layout(Title(text=title, text_font_size="16pt"), 'above')
    if sentence2:
        plot_second_sentence(p, sentence2)
    return p

pn.extension()
p = pn.panel(pn.Row(
        pn.Column(text_box1,text_box2),
        plot_sentiment))
p.show()
```
### Notice that leaving the p.show() at the bottom is what allows you to deploy this to your local server. 


### Instructions for use
- ```fork``` and ```git clone``` this repository to your local
- make sure the dependencies are downloaded
    - TextBlob, Panel, Bokeh
- run the following command ```panel serve app.ipynb```

This should start a server

**Reach out with any questions!**
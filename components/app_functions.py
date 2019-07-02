from textblob import TextBlob
from bokeh.models import ColumnDataSource, Title


def get_sentiment(sentence):
    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity


def get_sentiment(sentence):
    blob = TextBlob(sentence)
    polarity = blob.sentiment.polarity
    subjectivity = blob.sentiment.subjectivity
    return polarity, subjectivity


def create_data_source(polarity, subjectivity, sentence2_colors=False):
    categories = ['negative polarity', 'positive polarity', 'subjectivity']
    negative_polarity = abs(polarity) if polarity < 0 else 0
    positive_polarity = polarity if polarity >=0 else 0
    colors = ['red', 'blue', 'black']
    if sentence2_colors:
        colors[-1] = 'green'
    values = [negative_polarity, positive_polarity, subjectivity]
    source = ColumnDataSource(data=dict(categories=categories, values=values, color=colors))
    return source


def plot_second_sentence(p, sentence2):
    polarity, subjectivity = get_sentiment(sentence2)
    source = create_data_source(polarity, subjectivity, sentence2_colors=True)
    categories = ['negative polarity', 'positive polarity', 'subjectivity']
    p.vbar(x='categories', top='values', width=0.9, color='color', alpha=0.5, source=source)
    return p


if __name__ == "__main__":
    print(get_sentiment('this is a cool sentence'))

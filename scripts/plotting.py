import plotly.express as px

def create_pie_chart(df, title):
    positive_count = len(df[df['polarity'] == 'positive'])
    negative_count = len(df[df['polarity'] == 'negative'])
    if 'neutral' in df['polarity'].unique():
        neutral_count = len(df[df['polarity'] == 'neutral'])
        labels = ['Positive', 'Negative', 'Neutral']
        values = [positive_count, negative_count, neutral_count]
    else:
        labels = ['Positive', 'Negative']
        values = [positive_count, negative_count]

    fig = px.pie(names=labels, values=values, title=title)
    return fig

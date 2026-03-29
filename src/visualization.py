import plotly.graph_objects as go
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

def visualize_funnel(df_funnel):
    fig = px.funnel(df_funnel, x = "number", y = "event", title="E-Commerce Funnel Analysis", text="prct")
    fig.update_traces(textposition='inside',texttemplate="%{x:.0f}<br>%{text:.2f}%")
    return fig

def visualize_price_segmented_funnel(df_funnel_price):
    fig = go.Figure(data=[
        go.Bar(name='View -> Cart', x = df_funnel_price["price_range"], y = df_funnel_price["Cart_Rates"]),
        go.Bar(name='Cart -> Purchase', x = df_funnel_price["price_range"], y = df_funnel_price["Purchase_Rates"]),
        go.Bar(name='View -> Purchase', x = df_funnel_price["price_range"], y = df_funnel_price["Overall_Conversion_Rate"]),
    ])
    fig.update_layout(barmode='group', title_text="Conversion Rates by Price Range",     
        xaxis={
            'title': {
                'text': 'Price Range'
            }
        },
        yaxis={
            'title': {
                'text': 'Conversion Rate (%)'
            }
        },)
    fig.update_traces(textfont_size=12, textangle=0, textposition="outside", cliponaxis=False,
                    texttemplate="%{y:.2f}"+'%')
    return fig

def visualize_cohort(df_cohort_pctg):
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(df_cohort_pctg, annot=True, fmt=".2%", cmap="Blues", linewidths=0.5,
                linecolor='white', cbar_kws={'label': 'Retention (%)'})

    plt.title("User Retention by Cohort (Weekly)")
    plt.xlabel("Weeks since first interaction")
    plt.ylabel("Cohort (First Week)")
    return plt
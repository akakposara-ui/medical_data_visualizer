import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np


df = pd.read_csv('medical_examination.csv')

df['bmi'] = ((df['weight']) / (df['height']*df['height']) )*10000
df['overweight'] = np.where(df['bmi'] > 25, 1, 0)

df['cholesterol'] = np.where(df['cholesterol'] == 1, 0, 1)
df['gluc'] = np.where(df['gluc'] == 1, 0, 1)

def draw_cat_plot():
    # 5
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])


    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')
    fig = sns.catplot(
        x="variable", 
        y="total", 
        hue="value", 
        col="cardio", 
        data=df_cat, 
        kind="bar"
    ).fig

    # 9
    fig.savefig('catplot.png')
    return fig


def draw_heat_map():
    # 11
    # Clean the data: filter out incorrect blood pressure and extreme height/weight percentiles
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # 12
    corr = df_heat.corr()

    # 13
    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14
    fig, ax = plt.subplots(figsize=(12, 12))

    # 15
    # Plot the correlation matrix
    sns.heatmap(
        corr, 
        mask=mask, 
        annot=True, 
        fmt=".1f", 
        center=0, 
        square=True, 
        linewidths=.5, 
        cbar_kws={"shrink": .5}
    )

    # 16
    fig.savefig('heatmap.png')
    return fig
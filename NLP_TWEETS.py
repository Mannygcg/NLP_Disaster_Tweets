import marimo

__generated_with = "0.9.11"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo
    import matplotlib.pyplot as plt
    import polars as pl
    import seaborn as sns
    import plotly.express as px
    import tensorflow
    import keras_core as keras
    import numpy as np
    from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix
    return (
        ConfusionMatrixDisplay,
        confusion_matrix,
        keras,
        mo,
        np,
        pl,
        plt,
        px,
        sns,
        tensorflow,
    )


@app.cell
def __(pl):
    _test_file_path = "Kaggle/Kaggle_NLP_Tweets/NLP_Disaster_Tweets/test.csv"
    _train_file_path = "Kaggle/Kaggle_NLP_Tweets/NLP_Disaster_Tweets//train.csv"
    df_test = pl.read_csv(_test_file_path)
    df_train = pl.read_csv(_train_file_path)
    return df_test, df_train


@app.cell
def __(df_train):
    df_train
    return


@app.cell
def __(mo):
    mo.md(
        r"""
        Data Exploration
        -
        For both the training and test datasets, these are both comprised of 5 columns and 7,613 rows:

        - id: represents the unique identifier for each row of the dataset.
        - keyword: what the 'keyword' of the tweet is/was. There are a total of 222 unique values, ~0.8% being null and the most common keyword 'fatalities' representing 0.59% of the rows.
        - location: location from which the tweet was tweeted. There are a total of 3,342 unique values, 33% having null values and the most common location being 'USA' representing 1.36%. However, it seems that the location values do not follow a strict format, with many other tweets having locations within the USA but also mentioning their state. Furthermore, it seems that the location is not limited to real world locations which can affect the veracity of the tweets when considering location.
        - text: string of text representing the tweet.
        """
    )
    return


@app.cell
def __():
    104/7613*100
    return


@app.cell
def __(df_train, pl):
    df_train.group_by('keyword').agg(pl.col('id').count())
    return


@app.cell
def __(df_train, pl):
    df_train.group_by('location').agg(pl.col('id').count())
    return


@app.cell
def __(df_test):
    df_test.describe()
    return


@app.cell
def __():
    return


if __name__ == "__main__":
    app.run()

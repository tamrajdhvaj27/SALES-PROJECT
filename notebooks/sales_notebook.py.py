# Databricks notebook source
# Databricks notebook source

sales = [
    ("ProductA", 100),
    ("ProductB", 200),
    ("ProductC", 150)
]

df = spark.createDataFrame(sales, ["product", "amount"])

display(df)

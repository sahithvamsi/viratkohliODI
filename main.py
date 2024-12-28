import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Title of the Application
st.title("Virat Kohli ODI Analysis")

# Upload CSV File
uploaded_file = st.file_uploader("Upload the CSV file", type=["csv"])

if uploaded_file:
    # Load Data
    data = pd.read_csv(uploaded_file)
    st.subheader("Dataset Overview")
    st.write(data.head())

    # Check for Missing Values
    st.subheader("Missing Values")
    st.write(data.isnull().sum())

    # Display Total and Average Runs
    total_runs = data["Runs"].sum()
    avg_runs = data["Runs"].mean()
    st.subheader("Statistics")
    st.write(f"Total Runs: {total_runs}")
    st.write(f"Average Runs: {avg_runs}")

    # Runs Scored Over Matches
    st.subheader("Runs Scored Over Matches")
    plt.figure(figsize=(10, 5))
    plt.plot(data.index, data["Runs"], label="Runs", color="b")
    plt.title("Runs Scored by Virat Kohli Between 18-Aug-08 - 22-Jan-17")
    plt.xlabel("Matches")
    plt.ylabel("Runs")
    plt.grid(True)
    st.pyplot()

    # Batting Positions
    data["Pos"] = data["Pos"].map({
        3.0: "Batting At 3", 4.0: "Batting At 4", 2.0: "Batting At 2", 
        1.0: "Batting At 1", 7.0: "Batting At 7", 5.0: "Batting At 5", 
        6.0: "Batting At 6"
    })
    st.subheader("Matches Played at Different Batting Positions")
    pos = data["Pos"].value_counts()
    plt.figure(figsize=(10, 5))
    sns.barplot(x=pos.index, y=pos.values, palette="viridis")
    plt.title("Number of Matches at Different Batting Positions")
    plt.xlabel("Batting Position")
    plt.ylabel("Number of Matches")
    st.pyplot()

    st.subheader("Runs Scored at Different Batting Positions")
    plt.figure(figsize=(10, 5))
    sns.barplot(x=data["Pos"], y=data["Runs"], palette="viridis")
    plt.title("Runs by Virat Kohli at Different Batting Positions")
    plt.xlabel("Batting Position")
    plt.ylabel("Runs")
    st.pyplot()

    # Centuries
    st.subheader("Centuries by Virat Kohli")
    centuries = data.query("Runs >= 100")
    plt.figure(figsize=(10, 5))
    sns.barplot(x="Inns", y="Runs", data=centuries, hue="Runs", palette="viridis")
    plt.title("Centuries in First Innings Vs. Second Innings")
    plt.xlabel("Innings")
    plt.ylabel("Runs")
    st.pyplot()

    # Dismissals
    st.subheader("Dismissals of Virat Kohli")
    dismissal = data["Dismissal"].value_counts()
    plt.figure(figsize=(10, 5))
    sns.barplot(x=dismissal.index, y=dismissal.values, palette="viridis")
    plt.title("Dismissals of Virat Kohli")
    plt.xlabel("Dismissal Type")
    plt.ylabel("Count")
    st.pyplot()

    # Most Runs Against Teams
    st.subheader("Most Runs Against Teams")
    plt.figure(figsize=(10, 5))
    sns.barplot(x="Opposition", y="Runs", data=data, palette="viridis")
    plt.title("Most Runs Against Teams")
    plt.xlabel("Opposition")
    plt.ylabel("Runs")
    st.pyplot()

    # Most Centuries Against Teams
    st.subheader("Most Centuries Against Teams")
    plt.figure(figsize=(10, 5))
    sns.barplot(x="Opposition", y="Runs", data=centuries, palette="viridis")
    plt.title("Most Centuries Against Teams")
    plt.xlabel("Opposition")
    plt.ylabel("Runs")
    st.pyplot()

    # High Strike Rates
    st.subheader("High Strike Rates")
    strike_rate = data.query("SR >= 120")
    st.write(strike_rate)
    plt.figure(figsize=(10, 5))
    sns.barplot(x="Inns", y="SR", data=strike_rate, hue="SR", palette="viridis")
    plt.title("High Strike Rates in First Innings Vs. Second Innings")
    plt.xlabel("Innings")
    plt.ylabel("Strike Rate")
    st.pyplot()

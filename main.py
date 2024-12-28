import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

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

    # Runs Scored Over Matches (Plotly)
    st.subheader("Runs Scored Over Matches")
    matches = data.index
    figure = px.line(data, x=matches, y="Runs", 
                     title='Runs Scored by Virat Kohli Between 18-Aug-08 - 22-Jan-17')
    st.plotly_chart(figure)

    # Batting Positions (Plotly)
    data["Pos"] = data["Pos"].map({
        3.0: "Batting At 3", 4.0: "Batting At 4", 2.0: "Batting At 2", 
        1.0: "Batting At 1", 7.0: "Batting At 7", 5.0: "Batting At 5", 
        6.0: "Batting At 6"
    })
    st.subheader("Matches Played at Different Batting Positions")
    Pos = data["Pos"].value_counts()
    fig = go.Figure(data=[go.Pie(labels=Pos.index, values=Pos.values)])
    fig.update_layout(title_text='Number of Matches at Different Batting Positions')
    st.plotly_chart(fig)

    st.subheader("Runs Scored at Different Batting Positions")
    fig = go.Figure(data=[go.Pie(labels=data["Pos"], values=data["Runs"])])
    fig.update_layout(title_text='Runs by Virat Kohli at Different Batting Positions')
    st.plotly_chart(fig)

    # Centuries by Virat Kohli (Plotly)
    st.subheader("Centuries by Virat Kohli")
    centuries = data.query("Runs >= 100")
    figure = px.bar(centuries, x="Inns", y="Runs", color="Runs",
                    title="Centuries in First Innings Vs. Second Innings")
    st.plotly_chart(figure)

    # Dismissals of Virat Kohli (Plotly)
    st.subheader("Dismissals of Virat Kohli")
    dismissal = data["Dismissal"].value_counts()
    fig = go.Figure(data=[go.Pie(labels=dismissal.index, values=dismissal.values)])
    fig.update_layout(title_text='Dismissals of Virat Kohli')
    st.plotly_chart(fig)

    # Most Runs Against Teams (Plotly)
    st.subheader("Most Runs Against Teams")
    figure = px.bar(data, x="Opposition", y="Runs", color="Runs",
                    title="Most Runs Against Teams")
    st.plotly_chart(figure)

    # Most Centuries Against Teams (Plotly)
    st.subheader("Most Centuries Against Teams")
    figure = px.bar(centuries, x="Opposition", y="Runs", color="Runs",
                    title="Most Centuries Against Teams")
    st.plotly_chart(figure)

    # High Strike Rates (Plotly)
    st.subheader("High Strike Rates")
    strike_rate = data.query("SR >= 120")
    st.write(strike_rate)
    figure = px.bar(strike_rate, x="Inns", y="SR", color="SR",
                    title="High Strike Rates in First Innings Vs. Second Innings")
    st.plotly_chart(figure)

    # Example of using Matplotlib (if you need non-interactive plots)
    fig, ax = plt.subplots()  # Create figure and axes
    ax.scatter([1, 2, 3], [1, 2, 3])  # Example plot
    st.pyplot(fig)  # Pass figure to st.pyplot() to avoid deprecation warning

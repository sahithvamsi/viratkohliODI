This mini project was developed as a **mini-project** to demonstrate automated performance analysis and visualization for a cricket legend using Python.

---

# **Virat Kohli ODI Performance Analyzer** 📊🏏

## Project Overview
The **Virat Kohli ODI Performance Analyzer** is an automated tool designed to analyze and visualize the **ODI career performance** of one of cricket's legends, **Virat Kohli**. Using a **Streamlit web application**, users can upload a dataset to dynamically generate detailed insights into his batting statistics, including runs scored, strike rates, centuries, and performance against various teams.

### Live Application
Experience the application here: [Virat Kohli ODI Performance Analyzer](https://viratkohliodi-gec49szjf4uuosm6tfosmw.streamlit.app/)

---

## Features
### 1. Automated Data Analysis
- Processes user-uploaded datasets to extract **Virat Kohli's key performance metrics**.
- Identifies and highlights missing values for enhanced data quality.

### 2. Performance Metrics
- **Total Runs**: Computes the total runs scored across all ODIs in the dataset.
- **Average Runs**: Calculates the batting average over the matches.

### 3. Interactive Visualizations
- **Runs Over Matches**:
  - Line plot to visualize runs scored across games.
- **Batting Position Analysis**:
  - Bar charts displaying the number of matches and runs scored at different batting positions.
- **Centuries**:
  - Breakdown of scores above 100 in first vs. second innings.
- **Dismissals**:
  - Visualization of dismissal types and their frequency.
- **Opposition Analysis**:
  - Highlights performance (runs and centuries) against various teams.
- **High Strike Rate Matches**:
  - Spotlights games with a strike rate above 120.

### 4. User-Friendly Deployment
- Built using **Streamlit** for a clean and interactive user interface.
- Available online for instant access via Streamlit Cloud.

---

## Installation and Usage
### Prerequisites
Ensure you have **Python 3.x** installed with the following libraries:
- **Streamlit**
- **Pandas**
- **NumPy**
- **Matplotlib**
- **Seaborn**

### Steps to Run Locally
1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   streamlit run main.py
   ```
4. Upload a CSV file to analyze Virat Kohli's ODI performance.

---

## Dataset
The application processes a CSV file with the following structure:
- **Columns Required**:
  - `Runs`: Runs scored in each match.
  - `SR`: Strike rate in each match.
  - `Pos`: Batting position.
  - `Inns`: Innings (1st or 2nd).
  - `Dismissal`: Mode of dismissal.
  - `Opposition`: Opponent team.

Ensure the dataset is correctly formatted for optimal performance analysis.

---

## Deployment
The project is deployed on **Streamlit Cloud** and can be accessed here:  
[Virat Kohli ODI Performance Analyzer](https://viratkohliodi-gec49szjf4uuosm6tfosmw.streamlit.app/)

---



---

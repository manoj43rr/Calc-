import streamlit as st
import numpy as np
import pandas as pd

st.header("Incentive Calculator")
options = ["Annual Calculator", "Non Annual Calculator"]

val = st.radio("Choose the type of calculator:", options)

annualData = {
    "start_range": [65, 70, 75],
    "end_range": [69.9, 74.9, 100],
    "incentive_multiplier": [0.005, 0.0075, 0.0125]
}
annualDf = pd.DataFrame(annualData)

nonAnnualData = {
    "start_range": [85, 90, 92.5],
    "end_range": [89.9, 92.4, 100],
    "incentive_multiplier": [0.01, 0.015, 0.02]
}
nonAnnualDf = pd.DataFrame(nonAnnualData)

if val is not None:
    revenueAssigned = st.number_input("Enter the Revenue Assigned:", min_value=0, value=0, step=1, format="%d")
    percAchieved = st.slider("Adjust the percentage Achieved:", min_value=50.0, max_value=100.0, step=0.1)

    incentive = 0.0

    if val == options[0]:
        if percAchieved >= 65.0:
            row = annualDf[(annualDf["start_range"] <= percAchieved) & (annualDf["end_range"] >= percAchieved)]
            if not row.empty:
                incentive = revenueAssigned * (percAchieved / 100) * row["incentive_multiplier"].iloc[0]
                incentive = round(incentive)

    elif val == options[1]:
        if percAchieved >= 85.0:
            row = nonAnnualDf[(nonAnnualDf["start_range"] <= percAchieved) & (nonAnnualDf["end_range"] >= percAchieved)]
            if not row.empty:
                incentive = revenueAssigned * (percAchieved / 100) * row["incentive_multiplier"].iloc[0]
                incentive = round(incentive)

    st.write(f"### Incentive: ₹ {incentive}")

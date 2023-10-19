# Fraud Verifier - Streamlit App

Welcome to the Fraud Verifier application. This Streamlit app allows you to enter customer information and predict whether the given scenario is fraudulent or not. You can toggle between fraudulent and non-fraudulent scenarios to observe the prediction results.

## Installation

To run this Streamlit app, you need to have Python installed on your system. If you haven't already, you can install Streamlit by running the following command:

```bash
pip install streamlit

Once Streamlit is installed, you can run the app by executing the following command in the directory where your code is located:

streamlit run your_file.py
Replace your_file.py with the actual name of your Python script.

Usage
After launching the app, you will see a toggle switch labeled "Show Fraudulent Example" in the sidebar.

Toggle the switch to choose between fraudulent and non-fraudulent scenarios.

The app provides input fields for various customer information parameters, including income, age, address counts, credit score, and more.

Modify the input values to represent the customer information you want to analyze.

The app will display the final prediction result in a clear and visually appealing format, including an emoji-based indicator.

Input Parameters
The input parameters in this app include:

Income
Name-Email Similarity
Previous Address Months Count
Current Address Months Count
Customer Age
Days Since Request
Intended Balcon Amount
ZIP Count in 4 Weeks
Velocity in 6 Hours
Velocity in 24 Hours
Velocity in 4 Weeks
Bank Branch Count in 8 Weeks
Distinct Emails in 4 Weeks
Credit Risk Score
Email is Free
Home Phone Valid
Mobile Phone Valid
Bank Months Count
Has Other Cards
Proposed Credit Limit
Foreign Request
Session Length in Minutes
Keep Alive Session
Distinct Emails in 8 Weeks
Device Fraud Count
Month
Employment Status
Housing Status
Source
Device OS
Payment Type
Prediction Results
After entering the customer information, the app will provide a final prediction:

If you are in a fraudulent scenario, the app will display a lock emoji :lock: and the text "Fraudulent."

If you are in a non-fraudulent scenario, the app will display a checkmark emoji :white_check_mark: and the text "Not Fraudulent."

About
This Streamlit app was developed as part of the MLE Group 5 project for fraud verification. It utilizes various customer information parameters to make predictions about the likelihood of a given scenario being fraudulent. The app provides a user-friendly interface to interact with and observe the predictions.

For any questions or issues related to this app, please feel free to contact the project team.

Thank you for using the Fraud Verifier Streamlit app!

import streamlit as st

st.write(
    """
# MLE group 5 project - Fraud Verifier
"""
)
st.write(
    """
Enter your customer information
"""
)

# Create Streamlit input widgets for the objects
st.sidebar.write("#### Customer Information")

# Create a toggle switch to switch between fraudulent and non-fraudulent scenarios
toggle_fraudulent = st.sidebar.checkbox("Show Fraudulent Example")

# Define default values for input widgets based on the toggle state
if toggle_fraudulent:
    # Default values for fraudulent scenario
    default_income = 1000.0
    default_name_email_similarity = 0.5
    default_prev_address_months_count = 12
    default_current_address_months_count = 6
    default_customer_age = 30
    default_days_since_request = 7.0
    default_intended_balcon_amount = 500.0
    default_zip_count_4w = 2
    default_velocity_6h = 5.0
    default_velocity_24h = 10.0
    default_velocity_4w = 20.0
    default_bank_branch_count_8w = 2
    default_date_of_birth_distinct_emails_4w = 1
    default_credit_risk_score = 700
    default_email_is_free = False
    default_phone_home_valid = False
    default_phone_mobile_valid = True
    default_bank_months_count = 12
    default_has_other_cards = 1
    default_proposed_credit_limit = 1000.0
    default_foreign_request = True
    default_session_length_in_minutes = 30.0
    default_keep_alive_session = False
    default_device_distinct_emails_8w = 1
    default_device_fraud_count = 0
    default_month = 10
else:
    # Default values for non-fraudulent scenario
    default_income = 5000.0
    default_name_email_similarity = 0.8
    default_prev_address_months_count = 24
    default_current_address_months_count = 12
    default_customer_age = 40
    default_days_since_request = 3.0
    default_intended_balcon_amount = 1000.0
    default_zip_count_4w = 5
    default_velocity_6h = 2.0
    default_velocity_24h = 5.0
    default_velocity_4w = 15.0
    default_bank_branch_count_8w = 3
    default_date_of_birth_distinct_emails_4w = 2
    default_credit_risk_score = 750
    default_email_is_free = True
    default_phone_home_valid = True
    default_phone_mobile_valid = True
    default_bank_months_count = 24
    default_has_other_cards = 2
    default_proposed_credit_limit = 1500.0
    default_foreign_request = False
    default_session_length_in_minutes = 45.0
    default_keep_alive_session = True
    default_device_distinct_emails_8w = 3
    default_device_fraud_count = 1
    default_month = 12

# Use st.columns for columns
col1, col2, col3, col4 = st.columns(4)
income = col1.number_input("Income", value=default_income)
name_email_similarity = col2.number_input(
    "Name-Email Similarity", value=default_name_email_similarity
)
prev_address_months_count = col3.number_input(
    "Previous Address Months Count", value=default_prev_address_months_count
)
current_address_months_count = col4.number_input(
    "Current Address Months Count", value=default_current_address_months_count
)

col5, col6, col7, col8 = st.columns(4)
customer_age = col5.number_input("Customer Age", value=default_customer_age)
days_since_request = col6.number_input(
    "Days Since Request", value=default_days_since_request
)
intended_balcon_amount = col7.number_input(
    "Intended Balcon Amount", value=default_intended_balcon_amount
)
zip_count_4w = col8.number_input("ZIP Count in 4 Weeks", value=default_zip_count_4w)

col9, col10, col11, col12 = st.columns(4)
velocity_6h = col9.number_input("Velocity in 6 Hours", value=default_velocity_6h)
velocity_24h = col10.number_input("Velocity in 24 Hours", value=default_velocity_24h)
velocity_4w = col11.number_input("Velocity in 4 Weeks", value=default_velocity_4w)
bank_branch_count_8w = col12.number_input(
    "Bank Branch Count in 8 Weeks", value=default_bank_branch_count_8w
)

col13, col14, col15, col16 = st.columns(4)
date_of_birth_distinct_emails_4w = col13.number_input(
    "Distinct Emails in 4 Weeks", value=default_date_of_birth_distinct_emails_4w
)
credit_risk_score = col14.number_input(
    "Credit Risk Score", value=default_credit_risk_score
)
email_is_free = col15.checkbox("Email is Free", value=default_email_is_free)
phone_home_valid = col16.checkbox("Home Phone Valid", value=default_phone_home_valid)

col17, col18, col19, col20 = st.columns(4)
phone_mobile_valid = col17.checkbox(
    "Mobile Phone Valid", value=default_phone_mobile_valid
)
bank_months_count = col18.number_input(
    "Bank Months Count", value=default_bank_months_count
)
has_other_cards = col19.number_input("Has Other Cards", value=default_has_other_cards)
proposed_credit_limit = col20.number_input(
    "Proposed Credit Limit", value=default_proposed_credit_limit
)

col21, col22, col23, col24 = st.columns(4)
foreign_request = col21.checkbox("Foreign Request", value=default_foreign_request)
session_length_in_minutes = col22.number_input(
    "Session Length in Minutes", value=default_session_length_in_minutes
)
keep_alive_session = col23.checkbox(
    "Keep Alive Session", value=default_keep_alive_session
)
device_distinct_emails_8w = col24.number_input(
    "Distinct Emails in 8 Weeks", value=default_device_distinct_emails_8w
)

col25, col26, col27, col28 = st.columns(4)
device_fraud_count = col25.number_input(
    "Device Fraud Count", value=default_device_fraud_count
)
month = col26.number_input("Month", value=default_month)
employment_status = col27.selectbox(
    "Employment Status", ["CA", "CB", "CC", "CD", "CE", "CF", "CG"]
)
housing_status = col28.selectbox(
    "Housing Status", ["BA", "BB", "BC", "BD", "BE", "BF", "BG"]
)

col29, col30, col31, col32 = st.columns(4)
source = col29.selectbox("Source", ["INTERNET", "TELEAPP"])
device_os = col30.selectbox(
    "Device OS", ["linux", "macintosh", "other", "windows", "x11"]
)
payment_type = col31.selectbox("Payment Type", ["AA", "AB", "AC", "AD", "AE"])

# Beautified and larger text with conditional emojis
if toggle_fraudulent:
    st.write("## **Final Prediction:** :lock: **Fraudulent** :lock:")
else:
    st.write("## **Final Prediction:** :white_check_mark: **Not Fraudulent** :unlock:")

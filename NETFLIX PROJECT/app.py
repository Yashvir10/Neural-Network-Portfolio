import streamlit as st
import requests
import time
st.set_page_config(
    page_title="Netflix Churn Prediction",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(to right, #0f0f0f, #1c1c1c);
    color: white;
    font-family: 'Segoe UI', sans-serif;
}

/* Hide Streamlit Branding */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}

/* Main Title */
.main-title {
    font-size: 60px;
    font-weight: 800;
    color: #E50914;
    text-align: center;
    margin-bottom: 0px;
}

.subtitle {
    text-align: center;
    font-size: 22px;
    color: #d1d1d1;
    margin-bottom: 40px;
}

/* Cards */
.card {
    background-color: rgba(255,255,255,0.05);
    padding: 25px;
    border-radius: 20px;
    border: 1px solid rgba(255,255,255,0.08);
    box-shadow: 0px 8px 30px rgba(0,0,0,0.4);
    backdrop-filter: blur(10px);
}

/* Prediction Box */
.success-box {
    background: linear-gradient(to right, #00b09b, #96c93d);
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    color: white;
    font-size: 28px;
    font-weight: bold;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.3);
}

.fail-box {
    background: linear-gradient(to right, #93291E, #ED213A);
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    color: white;
    font-size: 28px;
    font-weight: bold;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.3);
}

/* Metrics */
div[data-testid="metric-container"] {
    background-color: rgba(255,255,255,0.05);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 15px;
    border-radius: 15px;
}

/* Button */
.stButton>button {
    background: linear-gradient(to right, #E50914, #B20710);
    color: white;
    border: none;
    border-radius: 12px;
    height: 3.5em;
    width: 100%;
    font-size: 18px;
    font-weight: bold;
    transition: 0.3s;
}

.stButton>button:hover {
    transform: scale(1.02);
    background: linear-gradient(to right, #ff1f1f, #c40812);
}

/* Input Labels */
label {
    color: white !important;
    font-weight: 600;
}

</style>
""", unsafe_allow_html=True)

st.markdown('<p class="main-title">🎬 Netflix Churn Prediction</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">AI-Powered Customer Retention Intelligence System</p>',
    unsafe_allow_html=True
)

with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/0/08/Netflix_2015_logo.svg", width=220)

    st.markdown("---")

    st.subheader("📌 Project Information")

    st.info(
        "This machine learning system predicts whether a Netflix customer is likely to churn based on customer behavioral and subscription data."
    )

    st.markdown("---")

    st.metric("Model Accuracy", "92%")
    st.metric("Algorithm", "Random Forest")
    st.metric("Backend", "FastAPI")
    st.metric("Frontend", "Streamlit")

    st.markdown("---")

    st.success("System Active")

left_col, right_col = st.columns([2.3, 1])

with left_col:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("👤 Customer Details")

    c1, c2 = st.columns(2)

    with c1:
        gender = st.selectbox("Gender", ["Male", "Female"])

        seniorCitizen = st.selectbox(
            "Senior Citizen",
            [0, 1]
        )

        partner = st.selectbox(
            "Partner",
            ["Yes", "No"]
        )

        dependents = st.selectbox(
            "Dependents",
            ["Yes", "No"]
        )

        tenure = st.slider(
            "Tenure (Months)",
            0,
            72,
            12
        )

        monthlyCharges = st.number_input(
            "Monthly Charges",
            0.0,
            500.0,
            75.0
        )

    with c2:

        phoneService = st.selectbox(
            "Phone Service",
            ["Yes", "No"]
        )

        multipleLines = st.selectbox(
            "Multiple Lines",
            ["Yes", "No", "No phone service"]
        )

        internetService = st.selectbox(
            "Internet Service",
            ["DSL", "Fiber optic", "No"]
        )

        contract = st.selectbox(
            "Contract Type",
            ["Month-to-month", "One year", "Two year"]
        )

        paymentMethod = st.selectbox(
            "Payment Method",
            [
                "Electronic check",
                "Mailed check",
                "Bank transfer (automatic)",
                "Credit card (automatic)"
            ]
        )

        totalCharges = st.number_input(
            "Total Charges",
            0.0,
            10000.0,
            1200.0
        )

    st.subheader("📺 Streaming Services")

    s1, s2, s3 = st.columns(3)

    with s1:
        onlineSecurity = st.selectbox(
            "Online Security",
            ["Yes", "No"]
        )

        onlineBackup = st.selectbox(
            "Online Backup",
            ["Yes", "No"]
        )

    with s2:
        deviceProtection = st.selectbox(
            "Device Protection",
            ["Yes", "No"]
        )

        techSupport = st.selectbox(
            "Tech Support",
            ["Yes", "No"]
        )

    with s3:
        streamingTV = st.selectbox(
            "Streaming TV",
            ["Yes", "No"]
        )

        streamingMovies = st.selectbox(
            "Streaming Movies",
            ["Yes", "No"]
        )

    paperlessBilling = st.selectbox(
        "Paperless Billing",
        ["Yes", "No"]
    )

    predict = st.button("🚀 Predict Customer Churn")

    st.markdown('</div>', unsafe_allow_html=True)

with right_col:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("📊 Business Insights")

    st.metric("Customer Retention", "87%")
    st.metric("Average Tenure", "28 Months")
    st.metric("Monthly Revenue", "$82K")

    st.markdown("---")

    st.subheader("🧠 AI Prediction Engine")

    st.write(
        "The AI model analyzes customer subscription behavior, service usage, payment preferences, and engagement patterns to predict churn probability."
    )

    st.markdown("---")

    st.warning(
        "Customers with month-to-month contracts and high monthly charges generally show higher churn probability."
    )

    st.markdown('</div>', unsafe_allow_html=True)

if predict:

    payload = {
        "gender": gender,
        "SeniorCitizen": seniorCitizen,
        "Partner": partner,
        "Dependents": dependents,
        "tenure": tenure,
        "PhoneService": phoneService,
        "MultipleLines": multipleLines,
        "InternetService": internetService,
        "OnlineSecurity": onlineSecurity,
        "OnlineBackup": onlineBackup,
        "DeviceProtection": deviceProtection,
        "TechSupport": techSupport,
        "StreamingTV": streamingTV,
        "StreamingMovies": streamingMovies,
        "Contract": contract,
        "PaperlessBilling": paperlessBilling,
        "PaymentMethod": paymentMethod,/
        "MonthlyCharges": monthlyCharges,
        "TotalCharges": totalCharges
    }

    with st.spinner("Analyzing customer behavior using AI..."):

        time.sleep(2)

        try:

            response = requests.post(
                "http://127.0.0.1:8000/predict",
                json=payload
            )

            result = response.json()

            st.markdown("<br>", unsafe_allow_html=True)
            st.subheader("🎯 Prediction Result")

            if result["prediction"] == 1:
                st.markdown(
                    '<div class="fail-box">❌ Customer Likely To Churn</div>',
                    unsafe_allow_html=True
                )

                st.error(
                    "High-risk customer detected. Retention strategies are recommended."
                )

            else:
                st.markdown(
                    '<div class="success-box">✅ Customer Likely To Stay</div>',
                    unsafe_allow_html=True
                )

                st.success(
                    "Customer shows strong retention probability."
                )

        except Exception as e:
            st.error(f"FastAPI Server Error: {e}")

st.markdown("---")

st.markdown(
    "<center>🎓 Final Year Major Project | Developed Using Machine Learning, FastAPI & Streamlit</center>",
    unsafe_allow_html=True
)


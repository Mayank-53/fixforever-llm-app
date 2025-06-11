import streamlit as st
import requests

# Set page config for dark mode styling
st.set_page_config(page_title="FixForever Laptop Diagnosis", layout="centered", initial_sidebar_state="collapsed")

# Apply dark theme manually (if needed)
st.markdown("""
    <style>
        body {
            background-color: #0e1117;
            color: white;
        }
        .stTextInput>div>div>input {
            background-color: #262730;
            color: white;
        }
        .stTextArea textarea {
            background-color: #262730;
            color: white;
        }
        .stButton>button {
            background-color: #00c7b1;
            color: black;
            font-weight: bold;
            border-radius: 8px;
        }
    </style>
""", unsafe_allow_html=True)

st.title("🔧 FixForever: Laptop Issue Assistant")
st.markdown("""
Enter your laptop issue below and let our AI give you a diagnosis in under 15 words.
""")

# Input from user
user_input = st.text_area("💬 Describe the laptop issue:", placeholder="e.g. Laptop shuts down when unplugged", height=100)

# Call backend only when button is pressed
if st.button("🧠 Diagnose Issue"):
    if not user_input.strip():
        st.warning("⚠️ Please enter a valid issue description.")
    else:
        with st.spinner("Analyzing your issue with our AI model..."):
            try:
                response = requests.post(
                    "http://localhost:8000/reason",  # Your FastAPI backend endpoint
                    json={"issue": user_input.strip()}
                )
                if response.status_code == 200:
                    reason = response.json().get("reason", "No diagnosis returned")
                    st.success(f"💡 Likely Reason: {reason}")
                else:
                    st.error(f"❌ Server error: {response.status_code}")
            except Exception as e:
                st.error(f"🚫 Failed to connect to backend: {str(e)}")

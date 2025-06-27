import streamlit as st
import joblib

# Load model
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), 'cyberbullying_model.pkl')
VECTORIZER_PATH = os.path.join(os.path.dirname(__file__), 'vectorizer.pkl')

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECTORIZER_PATH)


# Title
st.title("🔍 Cyberbullying Detector")
st.markdown("Enter a tweet or message below to check for cyberbullying.")

# User input
user_input = st.text_area("✉️ Enter the text here", height=150)

# Predict button
if st.button("Detect"):
    if user_input.strip() == "":
        st.warning("⚠️ Please enter a message to analyze.")
    else:
        prediction = model.predict([user_input])[0]

        if prediction == 1:
            st.error("🚫 **Cyberbullying Detected!**")
            # For simplicity, label type based on keyword clues (you can improve this with ML later)
            if any(word in user_input.lower() for word in ["muslim", "hindu", "christian", "religion"]):
                st.info("Type: Religion-Based")
            elif any(word in user_input.lower() for word in ["gay", "lesbian", "trans"]):
                st.info("Type: LGBTQ+-Based")
            elif any(word in user_input.lower() for word in ["fat", "ugly", "appearance"]):
                st.info("Type: Appearance-Based")
            else:
                st.info("Type: Other Cyberbullying")
        else:
            st.success("✅ **No Cyberbullying Detected.**")

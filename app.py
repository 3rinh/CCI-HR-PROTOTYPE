import streamlit as st
from textblob import TextBlob
import json

st.set_page_config(
    page_title="Employee Wellbeing",
    page_icon="◉",
    layout="centered"
)

st.title("Employee Wellbeing Check-In")

st.write(
    "A daily check-in designed to help you reflect on your wellbeing at work."
)

st.divider()

st.subheader("How are you feeling today?")

text = st.text_area(
    "Write your response below:",
    placeholder="Tell us how your workday has been...",
    height=180
)

if st.button("Submit Check-In", use_container_width=True):

    if text.strip() == "":
        st.warning("Please enter a response before submitting.")

    else:

        # Analyse the employee's message
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

        # Classify sentiment and assign a fictional risk score
        if polarity > 0.3:
            emotion = "HAPPY"
            risk = 10

        elif polarity > 0:
            emotion = "NEUTRAL"
            risk = 30

        elif polarity > -0.3:
            emotion = "STRESSED"
            risk = 70

        else:
            emotion = "ANGRY"
            risk = 90

        # Employee-facing response
        st.divider()
        st.subheader("Your Check-In")

        if risk > 60:
            st.info(
                "Thank you for sharing how you are feeling. "
                "It sounds like you may be experiencing increased pressure. "
                "Remember that support is available if you need it."
            )

        else:
            st.success(
                "Thank you for checking in. "
                "Your response suggests a relatively positive wellbeing state."
            )

        # Save assessment for manager dashboard
        assessment = {
            "message": text,
            "emotion": emotion,
            "risk": risk,
            "polarity": polarity
        }

        with open("assessment.json", "w") as file:
            json.dump(assessment, file)

        st.caption("Your check-in has been recorded.")

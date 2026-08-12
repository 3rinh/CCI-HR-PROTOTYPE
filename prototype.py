from textblob import TextBlob

text = input("Enter your message: ")

analysis = TextBlob(text)
polarity = analysis.sentiment.polarity

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


# EMPLOYEE VIEW
print("\n--- EMPLOYEE WELLBEING ASSISTANT ---")
print("Emotion detected:", emotion)

if risk > 60:
    print("""
Thank you for sharing how you are feeling.

It appears you may be experiencing increased pressure.
Remember that support is available. Consider taking a break,
speaking with your manager, or accessing wellbeing resources.
""")

else:
    print("""
Thank you for checking in.

Your response suggests a positive wellbeing state.
Continue maintaining healthy working habits.
""")


# MANAGER VIEW
print("\n--- MANAGER DASHBOARD ---")
print("Employee Risk Score:", risk, "%")

if risk > 60:
    print("Risk Level: HIGH")
    print("Recommended action: Schedule a wellbeing check-in.")

elif risk > 30:
    print("Risk Level: MODERATE")
    print("Recommended action: Monitor workload.")

else:
    print("Risk Level: LOW")
    print("No action required.")

    import streamlit as st
from textblob import TextBlob

st.title("Employee Wellbeing Check-In")

st.write("Please describe how you are feeling about your work today.")

text = st.text_area("How are you feeling?", height=150)

if st.button("Submit Check-In"):

    if text.strip() == "":
        st.warning("Please enter a message before submitting.")

    else:
        analysis = TextBlob(text)
        polarity = analysis.sentiment.polarity

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

        st.subheader("Your Wellbeing Check")

        st.write("Sentiment detected:", emotion)

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

        st.divider()

        st.subheader("Manager Assessment")

        st.write("Risk Score:", str(risk) + "%")

        if risk > 60:
            st.error("Risk Level: HIGH")
            st.write("Recommended action: Consider a wellbeing check-in.")

        elif risk > 30:
            st.warning("Risk Level: MODERATE")
            st.write("Recommended action: Monitor workload.")

        else:
            st.success("Risk Level: LOW")
            st.write("Recommended action: No immediate action required.")

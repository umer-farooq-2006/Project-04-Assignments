import streamlit as st

st.title("💪 BMI Calculator")

# User inputs
height = st.number_input("Enter your height (in meters):", min_value=0.5, max_value=2.5, step=0.01)
weight = st.number_input("Enter your weight (in kilograms):", min_value=10, max_value=300, step=1)

if st.button("Calculate BMI"):
    if height > 0 and weight > 0:
        bmi = weight / (height ** 2)
        st.success(f"Your BMI is: {bmi:.2f}")
        
        # Health interpretation
        if bmi < 18.5:
            st.info("You're underweight.")
        elif 18.5 <= bmi < 24.9:
            st.success("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.warning("You're overweight.")
        else:
            st.error("You are obese.")
    else:
        st.error("Please enter valid height and weight.")

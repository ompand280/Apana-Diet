import streamlit as st

def calculate_bmi(weight, height):
    height_m = height / 100
    return weight / (height_m ** 2)

def generate_diet(bmi, sugar=None, cholesterol=None):
    if bmi < 18.5:
        plan = "High protein and calorie-rich foods. Include dry fruits, bananas, peanut butter, milkshakes."
    elif 18.5 <= bmi <= 24.9:
        plan = "Balanced diet: rice, dal, roti, sabzi, fruits, and milk."
    elif 25 <= bmi <= 29.9:
        plan = "Low-carb diet. Avoid fried food, sweets. Include vegetables, whole grains, lean protein."
    else:
        plan = "Obesity diet: salad, sprouts, boiled vegetables, no sugar or fried foods."

    if sugar and sugar > 140:
        plan += "\n⚠️ Avoid sugar. Include fiber-rich foods and monitor glucose."
    if cholesterol and cholesterol > 200:
        plan += "\n⚠️ Avoid oily food. Add oats, walnuts, and green tea."

    return plan

st.title("🥗 Apna Diet - Next Level Diet Planner")
st.write("Personalized diet plan based on your body and report")

name = st.text_input("Your Name")
age = st.number_input("Age", min_value=5, max_value=100)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
weight = st.number_input("Weight (kg)")
height = st.number_input("Height (cm)")
cholesterol = st.number_input("Cholesterol Level (optional)", value=0)
sugar = st.number_input("Sugar Level (optional)", value=0)

if st.button("Generate Diet Plan"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        plan = generate_diet(bmi, sugar, cholesterol)

        st.success(f"Hello {name}! Your BMI is {bmi:.2f}")
        st.markdown("### 🥦 Your Diet Plan:")
        st.write(plan)
    else:
        st.warning("Please enter valid weight and height")import streamlit as st

def calculate_bmi(weight, height):
    height_m = height / 100
    return weight / (height_m ** 2)

def generate_diet(bmi, sugar=None, cholesterol=None):
    if bmi < 18.5:
        plan = "High protein and calorie-rich foods. Include dry fruits, bananas, peanut butter, milkshakes."
    elif 18.5 <= bmi <= 24.9:
        plan = "Balanced diet: rice, dal, roti, sabzi, fruits, and milk."
    elif 25 <= bmi <= 29.9:
        plan = "Low-carb diet. Avoid fried food, sweets. Include vegetables, whole grains, lean protein."
    else:
        plan = "Obesity diet: salad, sprouts, boiled vegetables, no sugar or fried foods."

    if sugar and sugar > 140:
        plan += "\n⚠️ Avoid sugar. Include fiber-rich foods and monitor glucose."
    if cholesterol and cholesterol > 200:
        plan += "\n⚠️ Avoid oily food. Add oats, walnuts, and green tea."

    return plan

st.title("🥗 Apna Diet - Next Level Diet Planner")
st.write("Personalized diet plan based on your body and report")

name = st.text_input("Your Name")
age = st.number_input("Age", min_value=5, max_value=100)
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
weight = st.number_input("Weight (kg)")
height = st.number_input("Height (cm)")
cholesterol = st.number_input("Cholesterol Level (optional)", value=0)
sugar = st.number_input("Sugar Level (optional)", value=0)

if st.button("Generate Diet Plan"):
    if weight > 0 and height > 0:
        bmi = calculate_bmi(weight, height)
        plan = generate_diet(bmi, sugar, cholesterol)

        st.success(f"Hello {name}! Your BMI is {bmi:.2f}")
        st.markdown("### 🥦 Your Diet Plan:")
        st.write(plan)
    else:
        st.warning("Please enter valid weight and height")

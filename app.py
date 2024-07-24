import streamlit as st

def calculate_sgpa(subjects):
    total_credits = sum(subject['credit'] for subject in subjects)
    weighted_grades = sum(subject['credit'] * subject['grade'] for subject in subjects)
    sgpa = weighted_grades / total_credits
    return sgpa

def calculate_cgpa(semesters):
    total_credits = sum(semester['total_credits'] for semester in semesters)
    weighted_sgpas = sum(semester['sgpa'] * semester['total_credits'] for semester in semesters)
    cgpa = weighted_sgpas / total_credits
    return cgpa

# Display the image
image_path = 'pic.jpg'
st.image(image_path, use_column_width=True)

# App title and description
st.title("SGPA & CGPA Calculator")
st.write("Select the calculation type and enter the required details to calculate your SGPA or CGPA.")

# Calculation type selection
calculation_type = st.selectbox("Select Calculation Type", ["SGPA", "CGPA"])

# SGPA calculation
if calculation_type == "SGPA":
    subject_count = st.number_input("Number of Subjects", min_value=1, step=1)
    subjects = []
    for i in range(subject_count):
        st.write(f"Subject {i+1}")
        credit = st.number_input(f"Credit {i+1}", key=f"credit_{i}", step=0.1)
        grade = st.number_input(f"Grade {i+1}", key=f"grade_{i}", step=0.01)
        subjects.append({'credit': credit, 'grade': grade})

    if st.button("Calculate SGPA"):
        sgpa = calculate_sgpa(subjects)
        st.success(f"SGPA: {sgpa:.2f}")

# CGPA calculation
elif calculation_type == "CGPA":
    semester_count = st.number_input("Number of Semesters", min_value=1, step=1)
    semesters = []
    for i in range(semester_count):
        st.write(f"Semester {i+1}")
        sgpa = st.number_input(f"SGPA {i+1}", key=f"sgpa_{i}", step=0.01)
        total_credits = st.number_input(f"Total Credits {i+1}", key=f"total_credits_{i}", step=0.1)
        semesters.append({'sgpa': sgpa, 'total_credits': total_credits})

    if st.button("Calculate CGPA"):
        cgpa = calculate_cgpa(semesters)
        st.success(f"CGPA: {cgpa:.2f}")

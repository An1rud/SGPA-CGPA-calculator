# SGPA & CGPA Calculator

This Streamlit application allows users to calculate their Semester Grade Point Average (SGPA) and Cumulative Grade Point Average (CGPA) based on the provided credits and grades for each subject or semester.

## Features

- **SGPA Calculation**: Users can input the number of subjects, along with the credits and grades for each subject, to calculate their SGPA.
- **CGPA Calculation**: Users can input the number of semesters, along with the SGPA and total credits for each semester, to calculate their CGPA.
- **Background Image**: The app includes a customizable background image for a visually appealing interface.

## Requirements

- Python 3.x
- Streamlit
- Base64

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/An1rud/SGPA-CGPA-calculator.git
    cd SGPA-CGPA-calculator
    ```

2. Install the required packages:
    ```bash
    pip install streamlit
    ```

3. Place your background image in the `static/img` directory and name it `pic.jpg`.

## Usage

1. Run the Streamlit app:
    ```bash
    streamlit run app.py
    ```

2. Open the app in your web browser at `http://localhost:8501`.

3. Select the calculation type (SGPA or CGPA) from the dropdown menu.

4. For SGPA calculation:
    - Enter the number of subjects.
    - Input the credits and grades for each subject.
    - Click the "Calculate SGPA" button to see the result.

5. For CGPA calculation:
    - Enter the number of semesters.
    - Input the SGPA and total credits for each semester.
    - Click the "Calculate CGPA" button to see the result.

## Modifying the Formulas

If you want to modify the formulas used for SGPA or CGPA calculations, you can do so by changing the corresponding functions in the code.

### Example

Here is an example of how you can change the SGPA formula in the `calculate_sgpa` function:

```python
def calculate_sgpa(subjects):
    total_credits = sum(subject['credit'] for subject in subjects)
    # Modify this line to change the SGPA formula
    weighted_grades = sum(subject['credit'] * subject['grade'] for subject in subjects)
    sgpa = weighted_grades / total_credits
    return sgpa
```

To modify the CGPA formula, change the `calculate_cgpa` function:

```python
def calculate_cgpa(semesters):
    total_credits = sum(semester['total_credits'] for semester in semesters)
    # Modify this line to change the CGPA formula
    weighted_sgpas = sum(semester['sgpa'] * semester['total_credits'] for semester in semesters)
    cgpa = weighted_sgpas / total_credits
    return cgpa
```

## Code Explanation

### Functions

- **calculate_sgpa(subjects)**: 
    - Takes a list of subjects, each with their credit and grade.
    - Returns the SGPA based on the weighted grades and total credits.

- **calculate_cgpa(semesters)**: 
    - Takes a list of semesters, each with their SGPA and total credits.
    - Returns the CGPA based on the weighted SGPAs and total credits.

- **add_bg_from_local(image_path)**: 
    - Adds a background image to the Streamlit app.
    - Takes the path to the image file as input.

### Streamlit App

- The app starts by adding the background image.
- The user selects the calculation type (SGPA or CGPA).
- Based on the selection, the app dynamically generates input fields for the user to enter the required data.
- The app calculates and displays the SGPA or CGPA when the user clicks the respective button.


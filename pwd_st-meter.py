import streamlit as st
import re

# Function to evaluate password strength
def evaluate_password_strength(password):
    strength = 0
    feedback = []

    # Check length
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    # Check for uppercase letters
    if re.search(r"[A-Z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one uppercase letter A,B,C,.....")

    # Check for lowercase letters
    if re.search(r"[a-z]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one lowercase letter a,b,c,.....")

    # Check for numbers
    if re.search(r"[0-9]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one number 1,2,3,.....")

    # Check for special characters
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    else:
        feedback.append("Password should contain at least one special character @,#,$,&,*.....")

    # Determine strength level
    if strength == 5:
        return "Strong", feedback
    elif strength >= 3:
        return "Moderate", feedback
    else:
        return "Weak", feedback

# Streamlit app
def main():
    st.title("Password Strength Meter")
    st.write("Enter a password to evaluate its strength.")

    # Input field for password
    password = st.text_input("Enter your password:", type="password")

    if password:
        strength, feedback = evaluate_password_strength(password)
        st.write(f"**Password Strength:** {strength}")

        if feedback:
            st.write("**Feedback:**")
            for item in feedback:
                st.write(f"- {item}")

if __name__ == "__main__":
    main()
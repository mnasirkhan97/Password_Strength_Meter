import re
import random
import string
import streamlit as st

# List of common weak passwords
COMMON_PASSWORDS = ["password", "123456", "12345678", "qwerty", "abc123", "password123", "admin", "iloveyou"]

def check_password_strength(password):
    score = 0
    suggestions = []

    # Check for common weak passwords
    if password.lower() in COMMON_PASSWORDS:
        return "❌ Very Weak - This password is too common!", ["Avoid using common passwords like 'password123' or '123456'."]

    # Length Check
    if len(password) >= 8:
        score += 1
    else:
        suggestions.append("Password should be at least 8 characters long.")

    # Upper & Lowercase Check
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
        suggestions.append("Include both uppercase and lowercase letters.")

    # Digit Check
    if re.search(r"\d", password):
        score += 1
    else:
        suggestions.append("Add at least one number (0-9).")

    # Special Character Check
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        suggestions.append("Include at least one special character (!@#$%^&*).")

    # Strength Rating
    if score == 4:
        return "✅ Strong Password!", []
    elif score == 3:
        return "⚠️ Moderate Password - Consider adding more security features.", suggestions
    else:
        return "❌ Weak Password - Improve it using the suggestions below:", suggestions

def generate_strong_password(length=12):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Meter")

password = st.text_input("Enter your password:", type="password")

if password:
    strength, feedback = check_password_strength(password)
    
    # Display password strength
    st.markdown(f"### {strength}")
    
    # Show progress bar based on score
    score = sum(1 for _ in feedback)
    progress = (4 - score) / 4  # Normalize to 0-1
    st.progress(progress)

    if feedback:
        st.warning("Here are some improvements:")
        for tip in feedback:
            st.write(f"➡️ {tip}")

st.sidebar.header("🔑 Generate a Strong Password")
length = st.sidebar.slider("Select Password Length", min_value=8, max_value=24, value=12)
if st.sidebar.button("Generate Password"):
    strong_password = generate_strong_password(length)
    st.sidebar.success(f"💡 Suggested Strong Password: `{strong_password}`")


# import re
# import random
# import string
# import streamlit as st

# def check_password_strength(password):
#     score = 0
#     suggestions = []

#     # Length Check
#     if len(password) >= 8:
#         score += 1
#     else:
#         suggestions.append("Password should be at least 8 characters long.")

#     # Upper & Lowercase Check
#     if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
#         score += 1
#     else:
#         suggestions.append("Include both uppercase and lowercase letters.")

#     # Digit Check
#     if re.search(r"\d", password):
#         score += 1
#     else:
#         suggestions.append("Add at least one number (0-9).")

#     # Special Character Check
#     if re.search(r"[!@#$%^&*]", password):
#         score += 1
#     else:
#         suggestions.append("Include at least one special character (!@#$%^&*).")

#     # Strength Rating
#     if score == 4:
#         return "✅ Strong Password!", []
#     elif score == 3:
#         return "⚠️ Moderate Password - Consider adding more security features.", suggestions
#     else:
#         return "❌ Weak Password - Improve it using the suggestions below:", suggestions

# def generate_strong_password():
#     characters = string.ascii_letters + string.digits + "!@#$%^&*"
#     return ''.join(random.choice(characters) for _ in range(12))

# # Streamlit UI
# st.title("🔐 Password Strength Meter")

# password = st.text_input("Enter your password:", type="password")

# if st.button("Check Strength"):
#     if password:
#         strength, feedback = check_password_strength(password)
#         st.markdown(f"### {strength}")
#         if feedback:
#             st.warning("Here are some improvements:")
#             for tip in feedback:
#                 st.write(f"➡️ {tip}")
#             st.info(f"💡 Suggested Strong Password: `{generate_strong_password()}`")
#     else:
#         st.error("Please enter a password to check its strength.")

# if st.button("Generate Strong Password"):
#     st.success(f"💡 Suggested Strong Password: `{generate_strong_password()}`")

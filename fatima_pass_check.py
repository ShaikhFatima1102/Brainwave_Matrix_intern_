import re

# Dictionary of common words for simplicity
common_words = ["password", "123456", "qwerty", "letmein", "admin", "welcome"]

# Function to check if the password contains dictionary words
def contains_common_words(password):
    for word in common_words:
        if word in password.lower():
            return True
    return False

# Function to assess the strength of a password
def assess_password_strength(password):
    score = 0
    feedback = []

    # Check password length
    length = len(password)
    if length >= 12:
        score += 2
    elif 8 <= length < 12:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")
    
    # Check character variety
    if re.search(r'[a-z]', password):
        score += 1
    else:
        feedback.append("Password should include lowercase letters.")
    
    if re.search(r'[A-Z]', password):
         score += 1
    else:
        feedback.append("Password should include uppercase letters.")
    
    if re.search(r'[0-9]', password):
        score += 1
    else:
        feedback.append("Password should include digits.")
    
    if re.search(r'[\W_]', password):
        score += 1
    else:
        feedback.append("Password should include special characters.")

    # Check for common patterns
    if re.search(r'(.)\1\1', password):
        feedback.append("Password contains repeated characters.")
    
    if re.search(r'(012|123|234|345|456|567|678|789)', password):
        feedback.append("Password contains common numeric sequences.")
    
    if re.search(r'(abc|bcd|cde|def|efg|fgh|ghi)', password):
        feedback.append("Password contains common alphabetic sequences.")
    
    if contains_common_words(password):
        feedback.append("Password contains common dictionary words.")
    
    # Generate overall feedback
    if score >= 6:
        strength = "Strong"
    elif 4 <= score < 6:
        strength = "Moderate"
    else:
        strength = "Weak"
        feedback.append("Consider using a more complex password with greater length and variety.")
    
    # Display results
    return {
        'score': score,
        'strength': strength,
        'feedback': feedback
    }

# Example Usage
password = input("enter password here ")
result = assess_password_strength(password)

print(f"Password Strength: {result['strength']}")
print(f"Score: {result['score']}/6")
print("Feedback:")
for f in result['feedback']:
    print(f"- {f}")


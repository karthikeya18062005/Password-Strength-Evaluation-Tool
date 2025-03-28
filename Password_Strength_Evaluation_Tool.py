import math
import string
import itertools
import threading
import datetime
import csv

# Length & Character Diversity
def length_and_diversity_score(password):
    score = 0
    if len(password) >= 12:
        score += 10
    elif len(password) >= 8:
        score += 8
    elif len(password) >= 6:
        score += 5
    else:
        score += 2

    char_types = sum(bool(set(chars) & set(password)) for chars in 
                    [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation])
    
    score += char_types * 2
    reason = f"Length: {len(password)}, Character Types: {char_types}."
    return min(score, 10), reason

# Unpredictability, Uniqueness, & Dictionary Resistance
def unpredictability_score(password, word_file='words.csv'):
    try:
        with open(word_file, 'r') as file:
            word_list = set(line.strip().lower() for line in file)
        if any(word in password.lower() for word in word_list):
            return 6, "Partially unique (contains dictionary words)."
        return 10, "Fully unique with no dictionary words."
    except FileNotFoundError:
        return 6, "Word list not found; scored partially."

# Entropy Calculation
def calculate_entropy(password):
    character_set_size = (
        (26 if any(char.islower() for char in password) else 0) +
        (26 if any(char.isupper() for char in password) else 0) +
        (10 if any(char.isdigit() for char in password) else 0) +
        (32 if any(char in string.punctuation for char in password) else 0)
    )
    entropy = len(password) * math.log2(character_set_size)
    score = min(int(entropy / 4), 10)
    reason = f"Entropy value: {entropy:.2f}."
    return score, reason

# Password Age
def password_age_score(password_creation_date):
    today = datetime.date.today()
    age_days = (today - password_creation_date).days

    if age_days < 30:
        score = 10
        reason = "Recently created."
    elif age_days < 90:
        score = 8
        reason = "Moderately old."
    elif age_days < 180:
        score = 5
        reason = "Old password."
    else:
        score = 2
        reason = "Very old password."
    
    return score, reason

# PCFGCracker (Pattern-Based Analysis)
def pcfg_score(password, user_data):
    common_patterns = [
        user_data.get('name', ''), user_data.get('phone', ''), user_data.get('dob', '')
    ]
    if any(pattern in password for pattern in common_patterns):
        return 5, "Contains predictable user data."
    return 10, "No predictable patterns found."

# Strength Classification
def classify_strength(total_score):
    if total_score >= 45:
        return "Very Strong"
    elif total_score >= 35:
        return "Strong"
    elif total_score >= 25:
        return "Average"
    elif total_score >= 15:
        return "Weak"
    else:
        return "Very Weak"

# Main Program
def evaluate_password(password):
    scores = {}
    reasons = {}

    # User Data for PCFGCracker
    user_data = {
        "name": input("Enter your name: "),
        "phone": input("Enter your phone number: "),
        "dob": input("Enter your date of birth (YYYYMMDD): ")
    }

    # Ask for password creation date
    try:
        creation_date = input("Enter password creation date (YYYY-MM-DD): ")
        password_creation_date = datetime.datetime.strptime(creation_date, "%Y-%m-%d").date()
    except ValueError:
        password_creation_date = datetime.date.today()

    # Scores and Reasons
    scores['Length & Diversity'], reasons['Length & Diversity'] = length_and_diversity_score(password)
    scores['Unpredictability'], reasons['Unpredictability'] = unpredictability_score(password)
    scores['Entropy'], reasons['Entropy'] = calculate_entropy(password)
    scores['Password Age'], reasons['Password Age'] = password_age_score(password_creation_date)
    scores['PCFGCracker'], reasons['PCFGCracker'] = pcfg_score(password, user_data)

    # Total Score Calculation
    total_score = sum(scores.values())
    strength = classify_strength(total_score)

    # Output Results
    print("\n=== Password Strength Analysis ===")
    for param, score in scores.items():
        print(f"{param}: {score}/10 - {reasons[param]}")
    print(f"\nTotal Score: {total_score}/50")
    print(f"Password Strength: {strength}")

# Run the Program
password = input("Enter your password to evaluate: ")
evaluate_password(password)

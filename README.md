Password Strength Evaluation Tool

This Python tool evaluates the strength of a given password based on five key parameters:

Length & Character Diversity

Unpredictability, Uniqueness, & Dictionary Resistance

Entropy Calculation

Password Age

PCFGCracker (Pattern-Based Analysis)

The tool assigns individual scores to each parameter, calculates a total score, and provides a password strength classification.

Features

✅ Detailed score breakdown with explanations✅ Total score calculation out of 50✅ Strength classification (Very Weak, Weak, Average, Strong, Very Strong)✅ Custom word list support for dictionary resistance✅ PCFGCracker-based pattern recognition using user details like name, phone, and DOB

Installation

Install Python (if not already installed):

sudo apt install python3

Install dependencies:

pip install nltk

Download or create a words.csv file for dictionary-based checks.

Usage

Run the program:

python password_strength_tool.py

Enter your password when prompted.

Provide the following details for better evaluation:
Name
Phone number
Date of birth (YYYYMMDD format)
Password creation date (YYYY-MM-DD format)

The tool will output:

Individual scores for each parameter
Explanations for each score
Total score out of 50
Overall strength classification
Example Output

Enter your password to evaluate: Karthikeya@18$
Enter your name: Karthikeya
Enter your phone number: 1234567890
Enter your date of birth (YYYYMMDD): 20010515
Enter password creation date (YYYY-MM-DD): 2024-01-10

=== Password Strength Analysis ===
Length & Diversity: 10/10 - Length: 14, Character Types: 4.
Unpredictability: 5/10 - Contains dictionary words.
Entropy: 8/10 - Entropy value: 67.58.
Password Age: 8/10 - Moderately old.
PCFGCracker: 5/10 - Contains predictable user data.

Total Score: 36/50
Password Strength: Strong

Scoring Breakdown

Length & Diversity: Longer passwords with diverse characters score higher.

Unpredictability: Passwords containing common words score lower.

Entropy: Higher entropy = stronger password.

Password Age: Newer passwords score higher.

PCFGCracker: Predictable patterns like name, DOB, or phone reduce the score.

Contribution

If you'd like to enhance this tool, feel free to submit a pull request or suggest improvements. Ideas like additional scoring factors, improved UI, or enhanced pattern recognition are welcome!

License

This project is licensed under the MIT License. Feel free to modify and distribute it.


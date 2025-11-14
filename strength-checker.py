# Ask user to enter a password
password = input("Enter a password: ")


# Initialize flags for each condition
length_ok = False       # True if length >= 8
has_upper = False       # True if at least one uppercase letter exists
has_number = False      # True if at least one number exists
has_special = False     # True if at least one special character exists

# Check password length
if len(password) >= 8:
    length_ok = True    # Length condition satisfied

# Loop through each character in the password
for char in password:
    if char.isupper():              # Check if character is uppercase
        has_upper = True
    if char.isdigit():              # Check if character is a number
        has_number = True
    if not char.isalnum() and not char.isspace():  # Check for special character
        has_special = True


# Print results for each condition
if length_ok:
    print("Password length is good")
else:
    print("Password must be at least 8 characters")

if has_upper:
    print("It has at least one uppercase letter")
else:
    print("It needs at least one uppercase letter")

if has_number:
    print("It contains at least one number")
else:
    print("It needs at least one number")
if has_special:
    print("It contains at least one special character")
else:
    print("It needs at least one special character")

# Final check: Is the password strong?
if length_ok and has_upper and has_number and has_special:
    print("\nPassword is STRONG ✅")
else:
    print("\nPassword is WEAK ❌")
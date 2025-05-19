import re
import os

# INFO: We will give the user the option to choose how to provide the data.

print("Welcome to the Regex Data Extractor")
print("You can choose how to provide the text")
print("1. Manual input. Type or Paste.")
print("2. Provide a file path.")

choice = input("Enter 1 or 2: ").strip()

# INFO: INIT the text var.
text_to_search = ""

# INFO: Handle User input.

if choice == "1":
    print("\Input your text below (press enter twice to confirm):\n")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    text_to_search = "\n".join(lines)

elif choice == "2":
    file_path = input("\nPlease enter the file path: ").strip()
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as file:
            text_to_search = file.read()
        print(" File read successfully!")
    else:
        print(" Error: File not found. Try again.")
        exit()

else:
    print(" Invalid choice. Please run the program again and choose 1 or 2.")
    exit()

# INFO: Defining the regex patterns.

email_pattern = r'\b[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+\b'
url_pattern = r'https?://[^\s]+'
phone_pattern = r'\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}'
card_pattern = r'\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}'

# INFO: Run the patterns on the input.

found_emails = re.findall(email_pattern, text_to_search)
found_urls = re.findall(url_pattern, text_to_search)
found_phones = re.findall(phone_pattern, text_to_search)
found_cards = re.findall(card_pattern, text_to_search)

# INFO: This displays the results.

print("\n These are the results:")

print("\n Email Addresses:")
if found_emails:
    for email in found_emails:
        print(" -", email)
else:
    print(" - None found")

print("\n URLs:")
if found_urls:
    for url in found_urls:
        print(" -", url)
else:
    print(" - None found")

print("\n Phone Numbers:")
if found_phones:
    for phone in found_phones:
        print(" -", phone)
else:
    print(" - None found")

print("\n Credit Card Numbers:")
if found_cards:
    for card in found_cards:
        print(" -", card)
else:
    print(" - None found")

print("\n Done! Thank you for using Regex Extractor!")

"""estimated time 20 mins
    Actual time 120 mins"""

def split_email(email):
    """Split an email into first and last name parts"""
    name_part = email.split("@")[0]
    split_name = name_part.split(".")
    return split_name


email_set = []
email = input("Enter an email: ").lower()

while email != "":
    choice = input(f"is your email {email} Y/N:").lower()
    if choice == "y":
        split_name = split_email(email)
        email_set.append([email, split_name])
    elif choice == "n":
        pass
    else:
        print("Please press Y or N")
    email = input("Enter an email: ").lower()

print("\nSaved email list:")
for email, name_parts in email_set:
    first_name = name_parts[0].capitalize()
    last_name = name_parts[1].capitalize()
    print(f"{first_name} {last_name} ({email})")

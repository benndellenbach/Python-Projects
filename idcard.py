print("Please enter the following information")

fn = input("First name:")
ln = input("Last name:")
email = input("Email address:")
phone = input("Phone number:")
job = input("Job title:")
id = input("ID Number:")
month = input ("Starting month:")
hair = input("Hair color:")
eye = input ("Eye color:")
trn = input("Currently in training(yes/no):")

print("The ID Card is:")
print("----------------------------------------")
print(f"{ln.upper()}, {fn.capitalize()}")
print(job.title())
print(f"ID: {id}")
print("")
print(f"EMail: {email.lower()}")
print(phone)
print("")
print(f"Hair: {hair.capitalize():15} Eyes: {eye.capitalize()}")
print(f"Month: {month.capitalize():14} Training: {trn.capitalize()}")
print("----------------------------------------")
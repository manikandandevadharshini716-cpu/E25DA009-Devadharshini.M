import re
def check_password(pwd):
    rules = {
        "Length (≥8)": len(pwd) >= 8,
        "Uppercase": any(c.isupper() for c in pwd),
        "Lowercase": any(c.islower() for c in pwd),
        "Digit": any(c.isdigit() for c in pwd),
        "Special char": bool(re.search(r"[!@#$%^&*()\-_=+[\]{};:'\",.<>?/`~]", pwd))
    }

    score = sum(rules.values())
    print(f"Password: {pwd}")
    print(f"Score: {score}/5")

    if score == 5:
        print("Strong Password 💪✅")
    elif score >= 3:
        print("Medium Password ⚠️")
    else:
        print("Weak Password ❌")

check_password("Pass@123")  
check_password("hello")     
check_password("Admin2025")

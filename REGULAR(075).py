import re
email="likithadandhu@gmail.com"
print("valid" if re.match(r"^[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}$",email) else "mail is INVALID")

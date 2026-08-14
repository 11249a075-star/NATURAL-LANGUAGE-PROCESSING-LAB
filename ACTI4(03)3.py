import re
resume = """
Name: Rahul Sharma
Email: rahul123@gmail.com
Phone: 9876543210
Skills: Python, Java, SQL, Machine Learning
"""
name = re.search(r'Name:\s*(.*)', resume)
email = re.search(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', resume)
phone = re.search(r'\b[6-9]\d{9}\b', resume)
skills = re.search(r'Skills:\s*(.*)', resume)
print("Name:", name.group(1))
print("Email:", email.group())
print("Phone:", phone.group())
print("Skills:", skills.group(1))

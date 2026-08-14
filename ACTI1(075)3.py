import re
text = """
Contact us at student@gmail.com or admin@yahoo.com.
Call 9876543210 or 9123456789.
Visit https://www.google.com or http://example.com.
"""
emails = re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', text)
phones = re.findall(r'\b[6-9]\d{9}\b', text)
urls = re.findall(r'https?://\S+', text)
print("Email IDs:", emails)
print("Mobile Numbers:", phones)
print("URLs:", urls)

from bs4 import BeautifulSoup
import requests
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
PASSWORD = os.environ["EMAIL_PASSWORD"]
MY_EMAIL = os.environ["EMAIL_ADDRESS"]
TO_ADDRESS = "rahimjon4753@gmail.com"
smtp = os.environ["SMTP_ADDRESS"]

header = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"
}


response = requests.get(URL, headers=header)

soup = BeautifulSoup(response.text, "html.parser")
price = float(soup.find(class_="aok-offscreen").getText().split()[0].split("$")[1])
product_name = soup.find(id="productTitle").getText().strip()
MESSAGE = f"{product_name} is now only ${price}"

# Create the email message
subject = "Amazon low price alert"
msg = MIMEText(MESSAGE, 'plain', 'utf-8')  # Encode the message in UTF-8
msg['Subject'] = Header(subject, 'utf-8')  # Encode the subject in UTF-8
msg['From'] = MY_EMAIL
msg['To'] = TO_ADDRESS


BUY_PRICE = 60

if price < BUY_PRICE:

    try:
        with smtplib.SMTP(smtp) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=TO_ADDRESS, msg=msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
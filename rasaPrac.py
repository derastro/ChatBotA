import schedule
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


# Function to send email
def send_email(to, subject, message):
    try:
        msg = MIMEMultipart()
        msg['From'] = 'Testhabibi2310@gmail.com'
        msg['To'] = to  
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('Testhabibi2310@gmail.com', 'njcm kbhp tpwh kjdc')
        text = msg.as_string()
        server.sendmail('Testhabibi2310@gmail.com', to, text)
        server.quit()
        print(f"Email sent to {to} with subject: {subject}")

    except Exception as e:
        print(f"error {e}")
# Function to send prompts
def send_prompts():
    try:
        print(f"Morning prompt sent to")
        employees = [("anuragrahi50@gmail.com", "Anurag"), ("lakhwinder.decrypt@gmail.com", "Lucky bhia")]

        for email, name in employees:
            # Generate morning and evening prompts using the chatbot
            morning_prompt = "Have you logged in?"
            evening_prompt = "Have you logged out?"
            print(f"Morning prompt sent to {email}")
            # Send morning prompt
            send_email(email, "Morning Check-In", f"Hi {name}, {morning_prompt}")
            print(f"Morning prompt sent to {email}")

            # Schedule evening prompt 
            # schedule.every().day.at("09:52").do(send_email, email, "Evening Check-Out", f"Hi {name}, {evening_prompt}")
        
    except Exception as e:
        print(f"error {e}")

        print("habibi")
        print("al-habibi")


schedule.every().minutes.do(send_prompts)
# send_prompts
while True:
    schedule.run_pending()
    time.sleep(1)

# send_email("anuragrahi50@gmail.com","fgdg","fgdfg")
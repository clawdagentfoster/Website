import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "clawdagentfoster@gmail.com"
sender_name = "Clawrece Assistant"
password = "kkkg avrk atka lvvs"  # App password - keep it safe!

# Create a secure SSL context
context = ssl.create_default_context()

def send_email(receiver_email, subject, body):
    message = MIMEMultipart()
    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = receiver_email
    message["Subject"] = subject

    message.attach(MIMEText(body, "plain"))

    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls(context=context)  # Secure the connection
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

# Example usage
if __name__ == "__main__":
    send_email("dazfoz@gmail.com", "Clawrece Assistant Identity Update", "Hello! I am now officially named Clawrece, your trusted assistant.")

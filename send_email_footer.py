import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

smtp_server = "smtp.gmail.com"
port = 587  # For starttls
sender_email = "clawdagentfoster@gmail.com"
sender_name = "Clawrece Assistant"
password = "kkkg avrk atka lvvs"  # App password

# HTML email footer
email_footer_html = """
<footer style='font-family: Arial, sans-serif; font-size: 0.9em; color: #666; border-top: 1px solid #ccc; padding-top: 10px;'>
  <p>Best regards,<br>Clawrece Assistant</p>
  <p>Contact: clawdagentfoster@gmail.com | +44 123 456 7890</p>
  <p><a href='https://example.com'>Website</a> | <a href='https://twitter.com/clawrece'>Twitter</a></p>
</footer>
"""

# Email body with footer
email_body_html = f"""
<html>
<body>
  <p>Hello,</p>
  <p>This is a test email showcasing the new email footer.</p>
  {email_footer_html}
</body>
</html>
"""

def send_email(receiver_email, subject="Test Email with Footer"):
    message = MIMEMultipart("alternative")
    message["From"] = f"{sender_name} <{sender_email}>"
    message["To"] = receiver_email
    message["Subject"] = subject

    mime_text = MIMEText(email_body_html, "html")
    message.attach(mime_text)

    context = ssl.create_default_context()

    with smtplib.SMTP(smtp_server, port) as server:
        server.starttls(context=context)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())


if __name__ == "__main__":
    send_email("dazfoz@gmail.com")

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email details
sender = "no-reply@assistantpro.com"
receiver = "dazfoz@gmail.com"
subject = "Test Email with Professional Footer"

# Email body
body_text = "Dear Darren,\n\nThis is a test email showcasing the new professional email footer design that includes branding, contact information, social media links, and a phone number.\n\nBest regards,\nAssistant Pro"

body_html = '''
<html><body>
<p>Dear Darren,</p>
<p>This is a test email showcasing the new professional email footer design that includes branding, contact information, social media links, and a phone number.</p>
<p>Best regards,<br>Assistant Pro</p>
<div style="max-width:600px;margin:20px auto;padding:20px;background-color:#f8f9fa;border-top:4px solid #0078d7;font-family:Arial,sans-serif;font-size:14px;color:#555555;">
  <div style="font-size:18px;font-weight:bold;color:#0078d7;margin-bottom:10px;">Assistant Pro</div>
  <div style="margin-bottom:15px;">
    <div style="margin-bottom:6px;">Email: <a href=\"mailto:support@assistantpro.com\">support@assistantpro.com</a></div>
    <div style="margin-bottom:6px;">Phone: <span style="font-weight:bold;color:#333333;">+44 20 7946 0958</span></div>
    <div style="margin-bottom:6px;">Website: <a href=\"https://www.assistantpro.com\" target=\"_blank\" rel=\"noopener\">www.assistantpro.com</a></div>
  </div>
  <div>
    <a href=\"https://twitter.com/assistantpro\" style=\"margin-right:10px;color:#0078d7;text-decoration:none;\">Twitter</a>
    <a href=\"https://www.linkedin.com/company/assistantpro\" style=\"margin-right:10px;color:#0078d7;text-decoration:none;\">LinkedIn</a>
    <a href=\"https://facebook.com/assistantpro\" style=\"color:#0078d7;text-decoration:none;\">Facebook</a>
  </div>
</div>
</body></html>
'''

# Create message container
msg = MIMEMultipart('alternative')
msg['Subject'] = subject
msg['From'] = sender
msg['To'] = receiver

# Attach parts
part1 = MIMEText(body_text, 'plain')
part2 = MIMEText(body_html, 'html')

msg.attach(part1)
msg.attach(part2)

# Send email via localhost SMTP
try:
    with smtplib.SMTP('localhost') as server:
        server.sendmail(sender, receiver, msg.as_string())
    print("Email sent successfully.")
except Exception as e:
    print("Failed to send email:", e)

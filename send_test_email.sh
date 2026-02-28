#!/bin/bash

# This script uses sendmail to send a test email with the designed footer to dazfoz@gmail.com

recipient="dazfoz@gmail.com"
subject="Test Email with Professional Footer"

body="Dear Darren,\n\nThis is a test email showcasing the new professional email footer design that includes branding, contact information, social media links, and a phone number.\n\nBest regards,\nAssistant Pro" 

footer='<div style="max-width:600px;margin:20px auto;padding:20px;background-color:#f8f9fa;border-top:4px solid #0078d7;font-family:Arial,sans-serif;font-size:14px;color:#555555;">\n  <div style="font-size:18px;font-weight:bold;color:#0078d7;margin-bottom:10px;">Assistant Pro</div>\n  <div style="margin-bottom:15px;">\n    <div style="margin-bottom:6px;">Email: <a href="mailto:support@assistantpro.com">support@assistantpro.com</a></div>\n    <div style="margin-bottom:6px;">Phone: <span style="font-weight:bold;color:#333333;">+44 20 7946 0958</span></div>\n    <div style="margin-bottom:6px;">Website: <a href="https://www.assistantpro.com" target="_blank" rel="noopener">www.assistantpro.com</a></div>\n  </div>\n  <div>\n    <a href="https://twitter.com/assistantpro" style="margin-right:10px;color:#0078d7;text-decoration:none;">Twitter</a>\n    <a href="https://www.linkedin.com/company/assistantpro" style="margin-right:10px;color:#0078d7;text-decoration:none;">LinkedIn</a>\n    <a href="https://facebook.com/assistantpro" style="color:#0078d7;text-decoration:none;">Facebook</a>\n  </div>\n</div>'

boundary="=====_BOUNDARY_====="

(
  echo "To: $recipient"
  echo "Subject: $subject"
  echo "MIME-Version: 1.0"
  echo "Content-Type: multipart/alternative; boundary=\"$boundary\""
  echo ""
  echo "--$boundary"
  echo "Content-Type: text/plain; charset=UTF-8"
  echo "Content-Transfer-Encoding: 7bit"
  echo ""
  echo -e "$body"
  echo ""
  echo "--$boundary"
  echo "Content-Type: text/html; charset=UTF-8"
  echo "Content-Transfer-Encoding: 7bit"
  echo ""
  echo "<html><body><p>${body//\n/<br>}</p>" 
  echo "$footer"
  echo "</body></html>"
  echo "--$boundary--"
) | sendmail -t

Add-Type -AssemblyName Microsoft.Office.Interop.Outlook
$outlook = New-Object -ComObject Outlook.Application
$mail = $outlook.CreateItem(0)
$mail.To = 'dazfoz@gmail.com'
$mail.Subject = 'test'
$mail.Body = 'main'
$mail.Send()
Write-Host "Email sent successfully."
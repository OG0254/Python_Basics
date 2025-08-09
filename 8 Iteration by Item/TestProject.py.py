import smtplib
from email.message import EmailMessage

# Create the email
email = EmailMessage()
email['From'] = 'ogadabrian2@gmail.com'
email['To'] = 'ogadabrian2@gmail.com'
email['Subject'] = 'Hello from Python!'
email.set_content('This is a test email sent from a Python script.')

# Set up the SMTP server
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.starttls()  # Secure the connection
    # your email & app password
    smtp.login('ogadabrian2@gmail.com', 'shanesteven')
    smtp.send_message(email)

print('Email sent successfully!')


# What to do:
# You need to generate an App Password — a special 16-character code just for your Python email-sending app.

# 📌 How to Get an App Password:
# Go to: Google Account Security Settings

# Scroll down to Signing in to Google

# Ensure 2-Step Verification is turned ON

# After it’s on, go back to that section — you’ll see App Passwords

# Select App Passwords

# Choose:

# App: Mail

# Device: Other (name it something like PythonScript)

# Google will give you a 16-character password — no spaces
# Example: abcd efgh ijkl mnop

# Use that code in your smtp.login() in place of your regular password

# 📌 Then run your script again — should be flawless.
# No more SMTPAuthenticationError.

# i will creat e a dummy account for testing purposes later

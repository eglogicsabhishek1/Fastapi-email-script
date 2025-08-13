
# Import required modules
from fastapi import FastAPI, Form  # FastAPI for API creation, Form for form data parsing
import smtplib  # For sending emails via SMTP
from email.message import EmailMessage  # For constructing email messages
import os  # For environment variable access
import dotenv  # For loading environment variables from .env file

# Load environment variables from .env file
dotenv.load_dotenv()

# Get SMTP credentials from environment variables
USER = os.getenv("SMTP_USER")  # Sender's email address
PASS = os.getenv("SMTP_PASSWORD")  # Sender's email password or app password

# Initialize FastAPI app
app = FastAPI()

# Define the API endpoint for sending emails
@app.post("/send-mail/")
async def send_mail(
    to: str = Form(...),        # Recipient's email address
    subject: str = Form(...),   # Subject of the email
    body: str = Form(...)       # Body/content of the email
):
    # Create the email message
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = USER
    msg["To"] = to
    msg.set_content(body)

    # SMTP server configuration
    smtp_server = "smtp.gmail.com"  # SMTP server address (Gmail used here)
    smtp_port = 587                 # SMTP port for TLS
    smtp_user = USER                # Sender's email (from .env)
    smtp_password = PASS            # Sender's password (from .env)

    try:
        # Connect to the SMTP server and send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to secure TLS
            server.login(smtp_user, smtp_password)  # Login with credentials
            server.send_message(msg)  # Send the email
        # Return success response
        return {"status": "success", "message": "Email sent"}
    except Exception as e:
        # Return error response if something goes wrong
        return {"status": "error", "message": str(e)}
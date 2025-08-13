# FastAPI Email Sender

This project provides a simple FastAPI service to send emails using SMTP. The API accepts parameters for recipient email, subject, and body, and sends the email using credentials stored in a `.env` file.

## Project Structure

```
EmailScript/
├── main.py         # FastAPI application with email sending endpoint
├── .env            # Environment variables for SMTP credentials
```

## Setup Instructions

1. **Clone or download the repository.**
2. **Install dependencies:**
   ```sh
   pip install fastapi uvicorn python-dotenv
   ```
3. **Configure SMTP credentials:**
   - Edit the `.env` file with your SMTP username and password:
     ```
     SMTP_USER=your_email@example.com
     SMTP_PASSWORD=your_app_password
     ```
   - For Gmail, use an App Password (not your regular password).
   - to generate your app password for google "https://myaccount.google.com/apppasswords" 

## Running the API

Start the FastAPI server with Uvicorn:
```sh
uvicorn main:app --reload
```

## Usage

Send a POST request to `/send-mail/` with form data:
- `to`: Recipient email address
- `subject`: Email subject
- `body`: Email body

Example using `curl`:
```sh
curl -X POST "http://127.0.0.1:8000/send-mail/" \
     -F "to=recipient@example.com" \
     -F "subject=Hello" \
     -F "body=This is a test email."
```

## Notes
- SMTP credentials are loaded from `.env` for security.
- Never commit real credentials to public repositories.
- For Gmail, enable App Passwords and use that password in `.env`.

## License
MIT

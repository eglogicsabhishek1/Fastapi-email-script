# FastAPI Email Sender

This project provides a simple FastAPI service to send emails using SMTP. The API accepts parameters for recipient email, subject, and body, and sends the email using credentials stored in a `.env` file.

## Project Structure

```
project-root/
├── env/                # (Recommended) Virtual environment folder
├── EmailScript/
│   ├── main.py         # FastAPI application with email sending endpoint
│   ├── .env            # Environment variables for SMTP credentials
```

## Setup Instructions

1. **Clone or download the repository.**

2. **Create a virtual environment (recommended to keep it outside your project folder):**
   Open a terminal and run:
   ```sh
   python -m venv 
   ```
   This will create a folder named `env` directory.

3. **Activate the virtual environment:**
   On Windows, run:
   ```sh
   \env\Scripts\activate
   ```
   On macOS/Linux, run:
   ```sh
   source /env/bin/activate
   ```

4. **Navigate to your cloned repository folder:**
   ```sh
   cd "EmailScript"
   ```
2. **Install dependencies:**
    -write given code in cmd line of your code editor
   ```sh
   pip install fastapi[standard]
   ```
3. **Configure SMTP credentials:**
   - Edit the `.env` file with your SMTP username and password:
     ```
     SMTP_USER=your_email@example.com
     SMTP_PASSWORD=your_app_password
     ```
   - For Gmail, use an App Password (not your regular password).
   - to generate your app password for google "https://myaccount.google.com/apppasswords" 

4. **Steps to generate app password for google**
   - make sure your 2-factor authentication in on.
   -to check 2-F Authentication: "https://myaccount.google.com/intro/security". Here you will see whether your 2FA is on or not.
   -after 2fA is on goes to app password for google "https://myaccount.google.com/apppasswords".
      -Login your account.
      - a pop up page will appear to enter <app name>. Enter name of your desire.
      - app password will appear. copy it and use it in .env.   
         **Note**: Make sure there is no space between app password


## Running the API

Start the FastAPI server with Uvicorn:
**make sure you are in same directory as main.py**
```sh
uvicorn main:app --reload
```
   Then goes to Browser and hit 
   - http://127.0.0.1:8000/docs


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

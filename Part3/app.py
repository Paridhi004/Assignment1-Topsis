from flask import Flask, render_template, request
from topsis_logic import topsis
import os
import smtplib
from email.message import EmailMessage
import threading  
import uuid       

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


EMAIL_ADDRESS = "paridhirastogi85@gmail.com"
APP_PASSWORD = "grvcdqnqqmoofhje" 

def send_email_background(receiver, file_path):
    """
    This function runs in the background. 
    It handles the email sending so the user doesn't have to wait.
    """
    try:
        msg = EmailMessage()
        msg["Subject"] = "TOPSIS Result"
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = receiver
        msg.set_content("Please find attached the TOPSIS result file.")

        with open(file_path, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="octet-stream",
                filename="output.csv"
            )

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, APP_PASSWORD)
            server.send_message(msg)
        
        print(f"Email successfully sent to {receiver}") # Check your server logs to see this
        
    except Exception as e:
        print(f"Failed to send email: {e}")

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            file = request.files["file"]
            weights = request.form["weights"]
            impacts = request.form["impacts"]
            email = request.form["email"]

            if not file or not weights or not impacts or not email:
                return "All fields are required"

            # 1. Create a unique filename so multiple users don't overwrite each other
            unique_id = str(uuid.uuid4().hex)
            input_filename = f"input_{unique_id}.csv"
            output_filename = f"output_{unique_id}.csv"

            input_path = os.path.join(UPLOAD_FOLDER, input_filename)
            output_path = os.path.join(UPLOAD_FOLDER, output_filename)

            # 2. Save and Run TOPSIS
            file.save(input_path)
            topsis(input_path, weights, impacts, output_path)

            # 3. START BACKGROUND THREAD (The Magic Fix)
            # This tells Python: "Go send this email, but let me continue immediately."
            email_thread = threading.Thread(target=send_email_background, args=(email, output_path))
            email_thread.start()

            return "Result calculated! Check your email in a few moments."

        except Exception as e:
            return f"An error occurred: {str(e)}"

    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    

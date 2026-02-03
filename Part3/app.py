from flask import Flask, render_template, request
from topsis_logic import topsis
import os
import smtplib
from email.message import EmailMessage

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

EMAIL_ADDRESS = "paridhirastogi85@gmail.com"
APP_PASSWORD = "grvcdqnqqmoofhje"

def send_email(receiver, file_path):
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

            input_path = os.path.join(UPLOAD_FOLDER, file.filename)
            output_path = os.path.join(UPLOAD_FOLDER, "output.csv")

            file.save(input_path)
            topsis(input_path, weights, impacts, output_path)
            send_email(email, output_path)

            return "Result sent to your email successfully"

        except Exception as e:
            return str(e)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

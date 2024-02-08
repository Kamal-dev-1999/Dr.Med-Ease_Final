from flask import Flask, render_template, request, jsonify
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from flask import jsonify

app = Flask(__name__)

def initialize_smtp_connection():
    try:
        smtp = smtplib.SMTP('smtp.gmail.com', 587)
        smtp.ehlo()
        smtp.starttls()
        return smtp
    except Exception as e:
        print(f"SMTP Connection Error: {e}")
        return None

def close_smtp_connection(smtp):
    if smtp:
        smtp.quit()

def send_email(subject="Python Notification", text="", to_email=None):
    smtp = initialize_smtp_connection()

    if not smtp:
        return False

    try:
        smtp.login('kamaltripathi1431@gmail.com', 'iqvu nepd bjxo qsny')

        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'plain'))

        to = to_email if to_email else ["dr.medease@gmail.com", "anshv54321@gmail.com", "ajeet1973.at@gmail.com", "dangivishnu316@gmail.com"]

        smtp.sendmail(from_addr="kamaltripathi1431@gmail.com", to_addrs=to, msg=msg.as_string())
        print("Email sent successfully!")
        return True
    except Exception as e:
        print(f"Error sending email: {e}")
        return False
    finally:
        close_smtp_connection(smtp)

@app.route('/send-email', methods=['POST'])
def send_email_route():
    try:
        data = request.get_json()

        to_email = data.get('toEmail')
        subject = data.get('subject')
        message = data.get('message')

        # Call the send_email function with the provided subject
        send_email(subject=subject, text=message, to_email=[to_email])

        return jsonify({'success': True})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

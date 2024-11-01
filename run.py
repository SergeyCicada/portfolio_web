from crypt import methods

import requests
from dotenv import load_dotenv
from flask import Flask, request, render_template, flash, redirect, url_for
import os
from function.function_send_mail import send_email

load_dotenv()
app = Flask(__name__)
app.secret_key = os.environ.get('FLASK_SECRET_KEY')

@app.route('/')
def get_main():
    return render_template('main/index.html')


@app.route('/about/')
def get_about():
    return render_template('main/about.html')


@app.route('/contacts/')
def get_contacts():
    recaptcha_site_key = os.environ.get('RECAPTCHA_SITE_KEY')
    return render_template('main/contacts.html', recaptcha_site_key=recaptcha_site_key)

@app.route('/thank/')
def get_thank():
    return render_template('main/thank_message.html')



@app.route('/message/', methods=['POST'])
def get_message():
    name = request.form.get('name')
    email = request.form.get('email')
    phone = request.form.get('phone')
    message = request.form.get('text')
    recaptcha_response = request.form.get('g-recaptcha-response')

    # Check reCAPTCHA
    secret_key = os.environ.get('RECAPTCHA_SECRET_KEY')
    payload = {
        'secret': secret_key,
        'response': recaptcha_response
    }
    response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=payload)
    result = response.json()

    if not result.get('success'):
        print(result)
        flash('reCAPTCHA verification failed. Please try again.', 'error')
        return redirect(url_for('get_thank'))

    string_send = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    try:
        send_email(string_send)
        flash('Your message has been sent successfully!', 'success')
    except Exception as e:
        # Error handling during submission.
        flash(f'An error occurred while sending your message: {str(e)}', 'error')
        return redirect(url_for('get_thank'))

    return redirect(url_for('get_thank'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

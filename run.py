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
    return render_template('main/contacts.html')

@app.route('/thank/')
def get_thank():
    return render_template('main/thank_message.html')



@app.route('/message/')
def get_message():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    message = request.args.get('text')

    string_send = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    try:
        send_email(string_send)
        flash('Your message has been sent successfully!', 'success')
    except Exception as e:
        # Обработка ошибок при отправке
        flash(f'An error occurred while sending your message: {str(e)}', 'error')
        return redirect(url_for('get_thank'))

    return redirect(url_for('get_thank'))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

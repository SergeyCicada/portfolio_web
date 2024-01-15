from flask import Flask, request, render_template

from function.function_send_mail import send_email

app = Flask(__name__)


@app.route('/')
def get_main():
    return render_template("index.html")


@app.route('/about/')
def get_about():
    return render_template("about.html")


@app.route('/contacts/')
def get_contacts():
    return render_template("contacts.html")


@app.route('/message/')
def get_message():
    name = request.args.get('name')
    email = request.args.get('email')
    phone = request.args.get('phone')
    message = request.args.get('text')

    string_send = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    send_email(string_send)

    return render_template("thank_message.html")


if __name__ == '__main__':
    app.run(debug=True)

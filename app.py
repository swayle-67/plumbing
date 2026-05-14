from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def landing():
    return render_template('landing.html')

@app.route('/assistant')
def assistant():
    return render_template('assistant.html')

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/booking')
def booking():
    return render_template('bookings.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
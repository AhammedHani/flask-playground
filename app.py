import os.path

from flask import Flask, render_template, request

app = Flask(__name__)

app.config['UPLOAD_PATH'] = 'static/images'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    file.save(os.path.join(app.config['UPLOAD_PATH'], file.filename))
    return 'uploaded successfully'


@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    return render_template('register.html', name=name, number=number, email=email)


@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/products")
def products():
    return render_template('products.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, redirect, url_for, render_template, request
import hashlib
app = Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html')


@app.route('/submit', methods=['POST','GET'])
def submit():
    if request.method == 'POST':
        img = request.form['Path']
        with open(img, "rb") as f:
            im_bytes = f.read()
        im_hash = str(hashlib.md5(im_bytes).hexdigest())
        return "<b>Here is the md5Hash of the Image :  </b>"+ im_hash
        
            

if __name__ == '__main__':
    app.run(debug=True)

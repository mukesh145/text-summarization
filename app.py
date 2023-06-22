from flask import Flask, render_template, request
from summarizer import summarize
from speach_to_text import s_to_t
import os


app = Flask(__name__)

UPLOAD_FOLDER = os.getcwd() 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def res():

    if 'text' in request.form:
        text = request.form['text']
        if text=="":
            file = request.files['file']
            filename = file.filename
            filename = "audio.mp3"
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            text = s_to_t()

        
    print(text)
    summary = summarize(text)
    return render_template('index.html', summary=summary)

if __name__ == '__main__':
    app.run(debug=True)














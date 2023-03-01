from flask import Flask, render_template, request
from static.emojis import emojis as cheatsheet

app = Flask(__name__)

keys = list(cheatsheet.keys())

def e_to_e(sentence):
    words = sentence.split()
    emojified = []
    for word in words:
        if word.lower() in keys:
            emojified.append(cheatsheet.get(word))
        else:
            emojified.append(word)
    emojified_string = ' '.join(emojified)
    return emojified_string

@app.route('/')
@app.route('/home')
def index():
    if 'english' in request.args:
        text = request.args['english']
        con_text = e_to_e(text)
        return render_template('index.html', translated=con_text)
    return render_template('index.html', translated='')

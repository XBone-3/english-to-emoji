from flask import Flask, render_template, request
import emoji_list as emojis

app = Flask(__name__)


key_list = list()
value_list = list()
for key, value in emojis.emoji_sorted.items():
    key_list.append(key)
    value_list.append(value)

value_as_key = dict()
for i, value in enumerate(value_list):
    for item in value:
        value_as_key[item.lower()] = key_list[i]


def e_to_e(sentence):
    words = sentence.split(' ')
    emojified = []
    for word in words:
        if word.lower() in value_as_key.keys():
            emojified.append(value_as_key[word])
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

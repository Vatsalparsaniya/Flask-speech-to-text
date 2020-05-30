import speech_recognition as sr
from flask import logging, Flask, render_template, request, flash
r = sr.Recognizer()

app = Flask(__name__)
app.secret_key = "VatsalParsaniya"

@app.route('/')
def index():
    flash(" Welcome to Vatsal's site")
    return render_template('index.html')

@app.route('/audio_to_text/')
def audio_to_text():
    flash(" Press Start to start recording audio and press Stop to end recording audio")
    return render_template('audio_to_text.html')

@app.route('/audio', methods=['POST'])
def audio():
    with open('upload/audio.wav', 'wb') as f:
        f.write(request.data)
  
    with sr.AudioFile('upload/audio.wav') as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='en-IN', show_all=True)
        return_text = " Did you say : <br> "
        try:
            for num, texts in enumerate(text['alternative']):
                return_text += str(num+1) +") " + texts['transcript']  + " <br> "
                print(texts['transcript'])
        except:
            return_text = " Sorry!!!!"
        
    return str(return_text)


if __name__ == "__main__":
    app.run(debug=True)

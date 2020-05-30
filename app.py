from flask import Flask, request, render_template, flash
import speech_recognition as sr

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/audio_to_text/')
def audio_to_text():
    return render_template("audio_to_text.html")

@app.route('/audio_to_text_prediction/', methods=['GET', 'POST'])
def audio_to_text_prediction():
    if request.method == "POST":
        if not request.files['audio_data']:
            flash("No File Found")
        else:
            audio_data = request.files['audio_data']
            audio_data.save('temp.wav')
            with audio_data as source:
                audio = recognizer.record(source)
                text = recognizer.recognize_google(audio, language='en-IN')
                print(text)
            # audio_data = request.files['audio_data']
            print(text,audio_data)
            # print(r.recognize_google(audio_data))
            # audio_data.save("temp.wav")
            return "Successfull"

if __name__ == "__main__":
    recognizer = sr.Recognizer()
    app.run(port=1234, debug=True)
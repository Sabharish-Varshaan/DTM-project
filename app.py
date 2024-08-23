from flask import Flask, request, render_template

app = Flask(__name__)

# Function to convert text to sign language images
def text_to_sign_language(text):
    # Dictionary mapping letters to image filenames
    sign_language_dict = {
        'a': 'a.png',
        'b': 'b.png',
        'c': 'c.png',
        'd': 'd.png',
        'e': 'e.png',
        'f': 'f.png',
        'g': 'g.png',
        'h': 'h.png',
        'i': 'i.png',
        'j': 'j.png',
        'k': 'k.png',
        'l': 'l.png',
        'm': 'm.png',
        'n': 'n.png',
        'o': 'o.png',
        'p': 'p.png',
        'q': 'q.png',
        'r': 'r.png',
        's': 's.png',
        't': 't.png',
        'u': 'u.png',
        'v': 'v.png',
        'w': 'w.png',
        'x': 'x.png',
        'y': 'y.png',
        'z': 'z.png',
        ' ': 'space.png'  # Image for space
    }
    # Convert text to list of images
    images = [sign_language_dict.get(char.lower(), 'unknown.png') for char in text]
    return images

@app.route('/', methods=['GET', 'POST'])
def home():
    images = []
    if request.method == 'POST':
        text = request.form['text']
        images = text_to_sign_language(text)
    print("Rendering template now")  # Add this line
    return render_template('index.html', images=images)


if __name__ == "__main__":
    app.run(debug=True)


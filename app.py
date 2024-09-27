from flask import Flask, render_template, request

app = Flask(__name__)

def text_to_sign_language(text):
    # Dictionary mapping letters and specific words to image filenames
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
        ' ': 'space.png',  # Image for space
        'when': 'when.png',  # Example of a word with a specific sign
    }

    # Split the input text into words
    words = text.split()
    images = []
    
    for word in words:
        if word.lower() in sign_language_dict:  # Handle predefined words like 'when'
            images.append(sign_language_dict[word.lower()])
        else:
            for char in word:  # Handle each character in the word
                images.append(sign_language_dict.get(char.lower(), 'unknown.png'))
            images.append(sign_language_dict[' '])  # Add a space image between words

    # Remove the last space image to avoid trailing space after the last word
    if images and images[-1] == 'space.png':
        images.pop()

    return images

@app.route('/', methods=['GET', 'POST'])
def index():
    images = []
    if request.method == 'POST':
        # Get the text input, if no input is provided, default to an empty string
        text = request.form.get('text_input', '').strip()
        
        if text:  # Only process if text is not empty
            images = text_to_sign_language(text)
    
    return render_template('index.html', images=images)

if __name__ == '__main__':
    app.run(debug=True)

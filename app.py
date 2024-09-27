from flask import Flask
app = Flask(__name__)

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
        ' ': 'space.png',  # Image for space
        'when': 'when.png',
    }
    
    # Split the input text into words
    words = text.split()
    images = []
    
    for word in words:
        if word in sign_language_dict:
            images.append(sign_language_dict[word])
        else:
            for char in word:
                images.append(sign_language_dict.get(char.lower(), 'unknown.png'))
            images.append(sign_language_dict[' '])  # Add space after each word

    return images

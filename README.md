# Text to Hand Sign Converter

## Overview
The Text to Hand Sign Converter is a web application designed to facilitate communication between the hearing and deaf communities by converting text input into corresponding sign language images. This project utilizes Flask as the web framework and provides a user-friendly interface for real-time text conversion.

## Project Structure
```
DTM-project-main
├── __pycache__
│   └── app.cpython-312.pyc
├── templates
│   └── index.html
├── static
│   └── googlef838eb7a0a1fa0b5.html
├── app.py
├── requirements.txt
├── Procfile
└── README.md
```

## Files Description
- **app.py**: The main application file that initializes the Flask web application, defines the `text_to_sign_language` function for converting text to sign language images, and sets up the routing for the application.
  
- **templates/index.html**: The HTML template for the web application, containing the structure and styling for the user interface, allowing users to input text and view the converted sign language images.

- **static/googlef838eb7a0a1fa0b5.html**: A file used for Google site verification, containing a simple verification string.

- **requirements.txt**: A file that lists the dependencies required for the project, specifying the versions of libraries needed to run the application.

- **Procfile**: A file used for deployment, specifying the command to run the application using Gunicorn.

## Setup Instructions
1. Clone the repository:
   ```
   git clone <repository-url>
   cd DTM-project-main
   ```

2. Create a virtual environment:
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

5. Run the application:
   ```
   python app.py
   ```

6. Open your web browser and navigate to `http://127.0.0.1:5000` to access the application.

## Usage
- Enter the text you wish to convert into sign language in the provided text area and click the "Convert" button.
- The application will display the corresponding sign language images based on the input text.

## Contributing
Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

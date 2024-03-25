# speech-recognition-model

ATOM.VOICE is a web application that allows users to control car functions using voice commands. The application provides an interface for sending voice commands to the car and processes these commands to perform various actions.

## Contents

- [Features](#features)
- [Required components](#required-components)
- [Installation](#installation)
- [Usage](#usage)
- [Used technologies](#used-technologies)
- [API Documentation](#api-documentation)

## Features

- Sending voice commands to control the functions of the car.
- Recognition of voice commands and performing appropriate actions.
- A web interface for user interaction.
- Support for selecting the user's location (inside, near, away from the car).

## Required components

Before you start, make sure that you have the following components:

- Python: The server part of the application is created in Python using Flask.
- Flask: Python is a web framework used to create a server.
- SpeechRecognition: Python library for speech recognition.
- jQuery: Used for processing AJAX requests and DOM manipulation.

## Installation

1. Clone the repository:

```
git clone https://github.com/vovandreevik/speech-recognition-model.git
```

2. Install the necessary Python packages:
```
pip install flask SpeechRecognition
```

## Usage
Start the server:
```
python app.py
```
1. Open a web browser and go to http://localhost:5000 /.
2. Select your location (inside, near, away from the car) from the drop-down list.
3. Press the button.
4. Allow the app to access your microphone.
5. Say a voice command, the application will process it and provide a response.

## Used technologies
- Flask: Микрофреймворк для веб-разработки на Python.
- SpeechRecognition: Библиотека для распознавания речи в Python.
- HTML, CSS и JavaScript: Для веб-интерфейса.
- jQuery: Для обработки AJAX-запросов и манипуляции DOM.

## API Documentation

- Documentation [API.docx ](https://github.com/vovandreevik/speech-recognition-model/files/12882927/API.docx )

- The start window

![photo_2023-10-12_18-58-47](https://github.com/vovandreevik/speech-recognition-model/assets/116523390/24663fe6-ea0c-4ba3-a622-74b5607bbef0)

- Request processing
  
![photo_2023-10-12_18-58-57](https://github.com/vovandreevik/speech-recognition-model/assets/116523390/e7758043-ad7c-4107-a0aa-694e9e13e33f)

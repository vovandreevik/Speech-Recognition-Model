# speech-recognition-model

ATOM.VOICE is a web application that allows users to control car functions using voice commands. The application provides an interface for sending voice commands to the car and processes these commands to perform various actions.

## Contents

- [Особенности](#особенности)
- [Необходимые компоненты](#необходимые-компоненты)
- [Установка](#установка)
- [Использование](#использование)
- [Используемые технологии](#используемые-технологии)
- [Документация API](#api)

## Особенности

- Отправка голосовых команд для управления функциями автомобиля.
- Распознавание голосовых команд и выполнение соответствующих действий.
- Веб-интерфейс для взаимодействия пользователя.
- Поддержка выбора местоположения пользователя (внутри, рядом, вдали от автомобиля).

## Необходимые компоненты

Перед началом убедитесь, что у вас есть следующие компоненты:

- Python: Серверная часть приложения создана на Python с использованием Flask.
- Flask: Python-веб-фреймворк, используемый для создания сервера.
- SpeechRecognition: Библиотека Python для распознавания речи.
- jQuery: Используется для обработки AJAX-запросов и манипуляции DOM.

## Установка

1. Клонируйте репозиторий:

```
git clone https://github.com/vovandreevik/speech-recognition-model.git
```

2.тановите необходимые пакеты Python:
```
pip install flask SpeechRecognition
```

## Использование
Запустите сервер:
```
python app.py
```
Откройте веб-браузер и перейдите по адресу http://localhost:5000/.

Выберите своё местоположение (внутри, рядом, вдали от автомобиля) из выпадающего списка.

Нажмите кнопку.

Разрешите приложению доступ к вашему микрофону.

Произнесите голосовую команду, приложение обработает её и предоставит ответ.

## Используемые технологии
- Flask: Микрофреймворк для веб-разработки на Python.
- SpeechRecognition: Библиотека для распознавания речи в Python.
- HTML, CSS и JavaScript: Для веб-интерфейса.
- jQuery: Для обработки AJAX-запросов и манипуляции DOM.

## Документация API

- Документация [API.docx](https://github.com/vovandreevik/speech-recognition-model/files/12882927/API.docx)

- Старотовое окно
  
![photo_2023-10-12_18-58-47](https://github.com/vovandreevik/speech-recognition-model/assets/116523390/24663fe6-ea0c-4ba3-a622-74b5607bbef0)

- Обработка запроса
  
![photo_2023-10-12_18-58-57](https://github.com/vovandreevik/speech-recognition-model/assets/116523390/e7758043-ad7c-4107-a0aa-694e9e13e33f)

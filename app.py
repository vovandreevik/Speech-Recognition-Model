from flask import Flask, render_template, jsonify
import speech_recognition as sr


def launch_car(action):
    if action == "on":
        return "автомобиль запущен"
    elif action == "off":
        return "автомобиль заглушен"
    else:
        return "недопустимая команда"


def doors(action):
    if action == "open":
        return "автомобиль открыт"
    elif action == "close":
        return "автомобиль закрыт"
    else:
        return "недопустимая команда"


def signaling(action):
    if action == "on":
        return "сигнализация включена"
    elif action == "off":
        return "сигнализация выключена"
    else:
        return "недопустимая команда"


def mileage():
    return "Пробег: 10000 км"


def power_reserve():
    return "Запас хода: 150 км"


def heated_seats(action):
    if action == "on":
        return "Подогрев сидений включен"
    elif action == "off":
        return "Подогрев сидений выключен"
    else:
        return "недопустимая команда"


def music(action):
    if action == "+":
        return "Уровень громкости увеличен"
    elif action == "-":
        return "Уровень громкости уменьшен"
    else:
        return "недопустимая команда"


def heated_steering_wheel(action):
    if action == "on":
        return "Подогрев руля включен"
    elif action == "off":
        return "Подогрев руля выключен"
    else:
        return "недопустимая команда"


def call(action):
    if action == "true":
        return "Звонок принят"
    elif action == "false":
        return "Звонок отклонен"
    else:
        return "недопустимая команда"


def trunk(action):
    if action == "open":
        return "Багажник открыт"
    elif action == "close":
        return "Багажник закрыт"
    else:
        return "недопустимая команда"


def automatic_seat_mirror():
    return "Настройка сиденья и зеркал для Владимира завершена"


car_commands = {
    "открыть автомобиль": doors("open"),
    "открой автомобиль": doors("open"),
    "закрыть автомобиль": doors("close"),
    "закрой автомобиль": doors("close"),
    "включить сигнализацию": signaling("on"),
    "включи сигнализацию": signaling("on"),
    "выключить сигнализацию": signaling("off"),
    "выключи сигнализацию": signaling("off"),
    "запустить двигатель": launch_car("on"),
    "запусти двигатель": launch_car("on"),
    "заглушить двигатель": launch_car("off"),
    "заглуши двигатель": launch_car("off"),
    "пробег": mileage(),
    "запас хода": power_reserve(),
    "включить подогрев сидений": heated_seats("on"),
    "включи подогрев сидений": heated_seats("on"),
    "выключить подогрев сидений": heated_seats("off"),
    "выключи подогрев сидений": heated_seats("off"),
    "увеличить громкость": music("+"),
    "увеличь громкость": music("+"),
    "уменьшить громкость": music("-"),
    "уменьши громкость": music("-"),
    "включить подогрев руля": heated_steering_wheel("on"),
    "включи подогрев руля": heated_steering_wheel("on"),
    "выключить подогрев руля": heated_steering_wheel("off"),
    "выключи подогрев руля": heated_steering_wheel("off"),
    "принять звонок": call("true"),
    "отклонить звонок": call("false"),
    "открой багажник": trunk("open"),
    "открыть багажник": trunk("open"),
    "закрой багажник": trunk("close"),
    "закрыть багажник": trunk("close"),
    "настрой сиденье и зеркала для владимира": automatic_seat_mirror(),
    "настрой сиденья и зеркала для владимира": automatic_seat_mirror(),
    "настройка сиденья и зеркал для владимира": automatic_seat_mirror(),
    "настроить сиденье и зеркала для владимира": automatic_seat_mirror(),
    "настроить сиденья и зеркала для владимира": automatic_seat_mirror()
}


app = Flask(__name__, static_url_path='/static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/recognize', methods=['POST'])
def recognize():
    audioCommand = sr.Recognizer()
    textCommand = ""

    with sr.Microphone() as source:
        try:
            audio = audioCommand.listen(source, timeout=10)
        except sr.WaitTimeoutError:
            return jsonify({"status": "error", "message": "Время вышло. Повторите попытку", "speech_text": ""})

    if audio:
        try:
            textCommand = audioCommand.recognize_google(audio, language='ru-RU').lower()
        except sr.UnknownValueError:
            return jsonify({"status": "error", "message": "Речь не распознана. Повторите попытку", "speech_text": ""})
        except sr.RequestError as e:
            return jsonify({"status": "error", "message": str(e), "speech_text": ""})

    if textCommand in car_commands:
        response = {
            "status": "success",
            "speech_text": textCommand,  # Include the recognized speech text in the response
            "message": car_commands[textCommand]
        }
    else:
        response = {
            "status": "error",
            "speech_text": textCommand,  # Include the recognized speech text in the response
            "message": "Неизвестная программа"
        }

    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)

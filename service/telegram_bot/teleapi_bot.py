import typer
import telebot
from PIL import Image
from io import BytesIO
import logging
import numpy as np
import uuid

from inference import inference_f

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def format_list_of_dicts(lst):
    formatted_lines = []
    for d in lst:
        values = list(d.values())
        formatted_line = f'<b>{values[0]}</b>, ({values[1]}, {values[2]})'
        formatted_lines.append(formatted_line)
    return '\n'.join(formatted_lines)


def start():

    bot = telebot.TeleBot({'Токен'})

    @bot.message_handler(commands=['start'])
    def message(message):
        bot.send_message(
            message.chat.id, 'Отправьте фото участка трубы'
        )

    @bot.message_handler(commands=['help'])
    def message(message):
        bot.send_message(
            message.chat.id, 'Чтобы начать работу, отправьте фото участка трубы, который вы хотите проверить на наличие дефектов'
        )

    @bot.message_handler(content_types=['photo'])
    def photo(message):

        print(
            f"Обработка сообщения с ID: {message.message_id} и фотографиями: {len(message.photo)}")

        fileID = message.photo[-1].file_id
        file_info = bot.get_file(fileID)
        downloaded_file = bot.download_file(file_info.file_path)
        image = Image.open(BytesIO(downloaded_file)).convert(mode="RGB")
        image = np.asarray(image)
        proccess_image(message, image)

    def proccess_image(message, path):
        visualize_filename = f'visualize_{uuid.uuid4()}.jpg'
        defects = inference_f(path, visualize_filename)
        formatted_defects = format_list_of_dicts(defects)

        if not formatted_defects.strip():
            bot.send_message(message.chat.id, "Дефекты не обнаружены.")
        else:
            bot.send_message(
                message.chat.id, f'Изображение с распознанными дефектами, их координаты и типы')
            bot.send_photo(message.chat.id, photo=open(
                visualize_filename, 'rb'))
            bot.send_message(
                message.chat.id, formatted_defects, parse_mode='HTML')

    bot.infinity_polling()


if __name__ == '__main__':
    typer.run(start)

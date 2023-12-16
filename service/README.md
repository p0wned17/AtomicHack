## Сервис по детекции производственных дефектов на изображении от команды "GigaFlex"

### Обучение модели
Создаём виртуальную среду и устанавливаем зависимости из `requirements.txt`.

### Запуск сервиса

Устанавливаем необходимый зависимости:
```
pip install -r requirements.txt
```
Запускаем сервис streamlit:
```bash
streamlit run streamlit_gui/Главная\ страница.py
```

Запускаем сервис TelegramBot:
```bash
python telegram_bot/teleapi_bot.py
```
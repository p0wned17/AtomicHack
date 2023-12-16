# AtomicHack - Решение команды GigaFlex

## Конвертация датасета в удобный формат
### Обязательно, поменяйте пути к датасетам в скриптах на свои!

Создаём аннотации:
```bash
python ./train/prepare_dataset/convert_labels.py
```

Нарезаем датасет на кропы:
```bash
python ./train/prepare_dataset/crop_dataset.py
```

Делим на train и validation:
```bash
python ./train/prepare_dataset/make_annotations.py
```

## Создания среды обучения в docker
Создаём докер контейнер:
```bash
cd docker_env
docker build -t gigafastenv .
```
Запускаем созданный контейнер:
```bash
./start.sh
```
> **Warning**
> Поменяйте volume на свои! Нужно прокинуть код обучения и датасет в докер.

## Обучение модели


Запуск обучения:

```bash
python main.py
```

## Конвертация модели в torchscript

```bash
python train/convert_to_torchscript.py 
```

## Инференс
Пример инференса лежит в ./inference/inference.py, inference_on_dir.py


Для запуска модели в продакшн в виде веб сервиса и телеграм бота обратитесь к инструкции [запуск модели в продакшн](service/README.md)

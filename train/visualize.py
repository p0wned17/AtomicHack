import cv2
import pandas as pd
import os


def hex_to_bgr(hex_color):
    """Преобразует шестнадцатеричный цвет в формат BGR."""
    hex_color = hex_color.lstrip("#")
    if len(hex_color) == 8:  # Если присутствует альфа-канал
        hex_color = hex_color[:-2]  # Удаляем альфа-канал
    b, g, r = [int(hex_color[i : i + 2], 16) for i in (0, 2, 4)]
    return (b, g, r)


# Словарь классов с цветом, номером и названием
classes = {
    0: ("66FF66AA", "не дефект"),
    1: ("8833FFFF", "потертость"),
    2: ("0000FFFF", "черная точка"),
    3: ("FF8800FF", "плена"),
    4: ("FF0000FF", "маркер"),
    5: ("AE7C10FF", "грязь"),
    6: ("FFFFFFFF", "накол"),
    7: ("FFDDAAFF", "н.д. накол"),
    8: ("FF00FFFF", "микровыступ"),
    9: ("880088FF", "н.д. микровыступ"),
    10: ("FFAA88FF", "вмятина"),
    11: ("3366FFFF", "мех.повреждение"),
    12: ("009900FF", "риска"),
    13: ("CC9900FF", "царапина с волчком"),
}

# Преобразование шестнадцатеричных цветов в BGR
for class_id, (hex_color, name) in classes.items():
    classes[class_id] = (hex_to_bgr(hex_color), name)


def visualize_and_save_dataset(csv_path, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    df = pd.read_csv(csv_path)
    grouped = df.groupby("image_path")

    for image_path, group in grouped:
        image = cv2.imread(image_path)
        if image is None:
            print(f"Не удалось загрузить изображение: {image_path}")
            continue

        for index, row in group.iterrows():
            x, y, class_id = int(row["x"]), int(row["y"]), int(row["class_id"])
            color, class_name = classes.get(
                class_id, ((255, 255, 255), "Неизвестный класс")
            )
            cv2.circle(image, (x, y), radius=5, color=color, thickness=-1)
            cv2.putText(
                image,
                f"{class_id}, {class_name}",
                (x, y - 10),
                cv2.FONT_HERSHEY_COMPLEX,
                0.4,
                color,
                1,
            )

        base_name = os.path.basename(image_path)
        save_path = os.path.join(output_folder, base_name)
        cv2.imwrite(save_path, image)


# Пример использования
visualize_and_save_dataset("output.csv", "visualized_images")

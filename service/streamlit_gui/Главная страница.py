import os
import pandas as pd
import streamlit as st
import torch
from utils import *
import numpy as np

device = "cuda" if torch.cuda.is_available() else "cpu"

st.set_page_config(
    page_title="Главная страница",
)

st.sidebar.markdown("# Главная страница")

st.markdown(
    "<h2 style='text-align: center; color: #34495e; font-size: 300%'>Главная страница</h2>",
    unsafe_allow_html=True,
)


@st.cache_data
def convert_df(df):
    return df.to_csv(index=False).encode('utf-8')


def upload_image_ui():
    uploaded_images = st.file_uploader(
        "Пожалуйста, выберите файлы с изображениями:",
        type=["png", "jpg", "jpeg", "bmp"],
        accept_multiple_files=True,
        help="Нажмите, чтобы загрузить фото трубы для поиска дефектов",
    )
    return uploaded_images


def process_images(list_images: list):
    my_bar = st.progress(0)

    col1, col2, col3 = st.columns(3)
    df_main = pd.DataFrame(columns=['filename', 'x', 'y', 'class'])
    if col2.button("Загрузить изображение"):
        with col1:
            st.write(" ")
        with col2:
            proccess_image = st.empty()
        with col3:
            st.write(" ")

        count_images = len(list_images)

        with col2:
            st.empty()

        for i, image in enumerate(list_images):
            filename, extension = os.path.splitext(image.name)

            opencv_image = bytes_to_numpy(image)

            name_defect = inference_data(opencv_image)

            if isinstance(opencv_image, np.ndarray):
                st.image(
                    opencv_image,
                    channels="BGR",
                )

                df = pd.DataFrame(columns=['X', 'Y', 'CLASS'])

                for i in name_defect:

                    print({
                        'X': i['x'],
                        'Y': i['y'],
                        'CLASS': i['class_name']
                    })
                    df.loc[len(df.index)] = [i['x'], i['y'], i['class_name']]
                    df_main.loc[len(df_main.index)] = [
                        image.name, i['x'], i['y'], i['class_id']]
                if not df.empty:
                    st.write(df)

                else:
                    st.write(
                        f'На изображении {filename} не было найдено дефектов!')

            else:
                st.error(
                    "С изображением что-то не так, проверьте и загрузите заново!"
                )
            with col1:
                st.write(" ")

            with col3:
                st.write(" ")
        csv = convert_df(df_main)

        st.download_button(
            "Скачать файл аннотаций к загруженным снимкам",
            csv,
            "file.csv",
            "text/csv",
            key='download-csv'
        )


def main():
    st.write("Здесь вы можете загрузить фото трубы")
    list_images = upload_image_ui()
    process_images(list_images)


if __name__ == "__main__":
    main()

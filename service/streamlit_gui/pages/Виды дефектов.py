import os
from glob import glob
import streamlit as st

PATH = "database_image"

st.set_page_config(
    page_title="База китов",
)


def get_images():
    list_images = glob(os.path.join(PATH, "*"))
    return list_images


st.markdown(
    "<h2 style='text-align: center; color: black; font-size: 2.5rem'>Галерея дефектов</h2>",
    unsafe_allow_html=True,
)

col1, col2, col3 = st.columns(3)

list_images = get_images()
len_images = len(list_images)

percent = int(len_images * 0.33)

with col1:
    for image_path in list_images[:percent]:
        st.image(image_path, use_column_width=True, caption=os.path.splitext(os.path.basename(image_path))[0])

with col2:
    for image_path in list_images[percent:2*percent]:
        st.image(image_path, use_column_width=True, caption=os.path.splitext(os.path.basename(image_path))[0])

with col3:
    for image_path in list_images[2*percent:]:
        st.image(image_path, use_column_width=True, caption=os.path.splitext(os.path.basename(image_path))[0])

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown(
    "<h3 style='text-align: center; color: black'>Коллекция всех фото</h3>",
    unsafe_allow_html=True,
)

st.image(list_images, width=600, caption=[os.path.splitext(os.path.basename(image_path))[0] for image_path in list_images])
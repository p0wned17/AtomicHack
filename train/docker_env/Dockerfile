FROM nvcr.io/nvidia/pytorch:23.05-py3
# ENV HTTP_PROXY="http://proxy.ufanet.ru:3128"
# ENV HTTPS_PROXY="http://proxy.ufanet.ru:3128"
# ENV NO_PROXY="127.0.0.1,localhost,git.ufanet.ru,minio.lo.ufanet.ru,10.2.88.0/24,ufanet.ru"
RUN apt-get update && apt-get install libturbojpeg


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt --no-cache-dir
RUN pip install -U git+https://github.com/albumentations-team/albumentations --no-binary qudida,albumentations
RUN pip install timm --pre -U
# Set up user

# ENV HOST_UID 1001
# ENV HOST_GID 1001


# ENV USER_NAME cv_user 
# ENV HOME_DIR /home/$USER_NAME

# RUN adduser --disabled-password \
#     --gecos "Default user" \
#     --uid ${HOST_UID} \
#     ${USER_NAME}



# USER ${USER_NAME}
# WORKDIR ${HOME_DIR}


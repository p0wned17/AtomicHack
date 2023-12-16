docker run --gpus all -it --rm --network host --ipc=host \
    -v /mnt/:/mnt/ \
    -v /home/cv_user/:/home/cv_user \
    gigafastenv:latest /bin/bash

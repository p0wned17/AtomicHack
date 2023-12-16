import albumentations as A
from albumentations.pytorch import ToTensorV2
import cv2


train_transform = A.Compose(
    [
        A.Resize(
            always_apply=False,
            p=1,
            height=160,
            width=160,
            interpolation=cv2.INTER_AREA,
        ),
        A.Flip(p=0.5),
        # A.GaussNoise(
        #     always_apply=False,
        #     p=0.5,
        #     var_limit=(10.0, 50.0),
        #     per_channel=True,
        #     mean=0.0,
        # ),
        A.RandomBrightnessContrast(
            always_apply=False,
            p=0.5,
            brightness_limit=(-0.1, 0.1),
            contrast_limit=(-0.1, 0.1),
            brightness_by_max=True,
        ),
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ToTensorV2(),
    ]
)


val_transform = A.Compose(
    [
        A.Resize(
            always_apply=False,
            p=1.0,
            height=160,
            width=160,
            interpolation=cv2.INTER_AREA,
        ),
        A.Normalize(mean=(0.485, 0.456, 0.406), std=(0.229, 0.224, 0.225)),
        ToTensorV2(),
    ]
)

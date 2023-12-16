import torch.nn as nn
import timm
import torch.nn.functional as F


class ClassificationModel(nn.Module):
    def __init__(
        self,
        backbone="convnextv2_nano.fcmae_ft_in22k_in1k",
        pretrained=True,
        num_classes=14,
        dropout=0.2,
    ) -> None:
        super().__init__()

        self.model = timm.create_model(
            backbone,
            pretrained=pretrained,
            num_classes=num_classes,
            drop_rate=dropout,
        )

    def forward(self, x):
        x = self.model(x)
        return x

from pathlib import Path

import pandas as pd
import typer
from sklearn.model_selection import train_test_split


def split_dataset(input_path: Path, output_path: Path, val_size: float):
    data = pd.read_csv(input_path, delimiter=",")

    train, val = train_test_split(
        data,
        test_size=val_size,
        random_state=42,
        shuffle=True,
        stratify=data["class_id"],
    )

    train.to_csv(output_path.joinpath("train.csv"), index=False, sep=",")
    val.to_csv(output_path.joinpath("val.csv"), index=False, sep=",")


def main(
    input_path: Path = typer.Argument(
        "cropped_dataset.csv", help="Путь до .csv файла с классами"
    ),
    output_path: Path = typer.Argument(
        "",
        help="Путь, куда выгрузить трейн и тест разметку.",
    ),
    val_size: float = typer.Argument(0.15, help="Размер валидационной выборки."),
):
    split_dataset(input_path, output_path, val_size)
    typer.secho(input_path, fg=typer.colors.BRIGHT_CYAN)


if __name__ == "__main__":
    try:
        typer.run(main)
    except SystemExit:
        typer.secho("Программа завершена", fg=typer.colors.GREEN)

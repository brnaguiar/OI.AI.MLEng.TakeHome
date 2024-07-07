from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_image, label",
    [
        ("seal.jpg", 150),
        ("turtle.jpg", 33),
        ("white-shark.jpg", 2),
    ],
)
def test_prediction(input_image, label, preprocessed_data, model, images_path):
    # Run Prediction
    image = preprocessed_data(Path(images_path) / input_image)
    assert model.predict(image) == label

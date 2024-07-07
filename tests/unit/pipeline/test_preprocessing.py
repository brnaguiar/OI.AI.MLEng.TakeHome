import pytest
from PIL import Image


@pytest.fixture(params=[(10, 10), (512, 512)], scope="module")
def sample_image(request):
    image = Image.new("RGB", request.param, color="red")
    return image


def test_img_transformations(preprocessor, sample_image):
    transformation = preprocessor.transform(sample_image)
    assert list(transformation.shape) == [3, 224, 224]

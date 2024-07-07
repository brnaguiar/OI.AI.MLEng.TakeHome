import hydra
import pytest

from oi.ai.mleng.takehome.pipeline.model import MarineAnimalClassifier
from oi.ai.mleng.takehome.pipeline.postprocessing import ClassLoader
from oi.ai.mleng.takehome.pipeline.preprocessing import ImagePreprocessor

hydra.initialize(version_base=None, config_path="../conf")
cfg = hydra.compose(config_name="tests.yaml", return_hydra_config=True)


@pytest.fixture(scope="session")
def preprocessor():
    return ImagePreprocessor()


@pytest.fixture(scope="session")
def images_path():
    return cfg.files.data.images


@pytest.fixture
def model():
    return MarineAnimalClassifier()


@pytest.fixture(scope="session")
def preprocessed_data(preprocessor):
    def _preprocessed_data(image_path):  # Emulates a Fixture Factory
        return preprocessor(image_path)

    return _preprocessed_data


@pytest.fixture(scope="session")
def class_json():
    return ClassLoader(cfg.files.data.labels).load_data()  # cs

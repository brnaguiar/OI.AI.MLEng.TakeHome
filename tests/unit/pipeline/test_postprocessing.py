import pytest


@pytest.mark.parametrize(
    "label_number, label_text",
    [
        (150, "sea lion"),
        (33, "loggerhead"),
        (2, "great white shark"),
        (1, "goldfish"),
    ],
)
def test_get_animal_name_by_index(label_number, label_text, class_json):
    assert class_json.get_animal_name_by_index(label_number) == label_text

from dataclasses import dataclass


@dataclass
class Data:
    """
    A class representing data with labels.

    Attributes:
        labels (str): A string representing labels associated with the data.
        Images (str): A string representing the directory of images about \
                marine animals.
    """

    labels: str
    images: str = ""


@dataclass
class Files:
    """
    A class representing files containing data.

    Attributes:
        data (Data): An instance of the Data class containing labels.
    """

    data: Data

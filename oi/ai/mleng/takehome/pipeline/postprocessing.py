import json

from pydantic import Json


class ClassLoader:
    """
    A class used to load and process a JSON file containing \
            animal class information.

    The ClassLoader class reads a JSON file, \
            processes the data to format the animal
    names by removing underscores, and provides methods to retrieve \
    and print this information.

    Attributes
    ----------
    json_file : Json
        The path to the JSON file containing animal class data.
    class_to_str : dict
        A dictionary mapping class indices to formatted animal names.

    Methods
    -------
    __init__(json_file: Json):
        Initializes the ClassLoader with the path to the JSON file.

    load_data() -> self:
        Reads and processes the JSON file, loading the data into the \
                class_to_str attribute.

    get_animal_name_by_index(index: int) -> str:
        Retrieves the formatted animal name corresponding to the \
                given class index.

    print_animal_dict() -> None:
        Prints the dictionary of class indices and their corresponding\
                formatted animal names.
    """

    def __init__(self, json_file: Json):
        """
        Initializes the ClassLoader with the path to the JSON file.

        Parameters
        ----------
        json_file : Json
            The path to the JSON file containing animal class data.
        """
        self.json_file = json_file
        self.class_to_str: dict = {}

    def load_data(self):
        """
        Reads and processes the JSON file, loading the data into the \
                class_to_str attribute.

        This method reads the JSON file, parses the data into a dictionary,\
                and formats the animal names by replacing underscores \
                with spaces.

        Returns
        -------
        self
            The instance of the ClassLoader with the loaded and processed data.
        """
        # Read JSON data from file
        with open(self.json_file, "r", encoding="utf-8") as f:
            json_data = f.read()

        # Parse JSON data into Python dictionary
        self.class_to_str = json.loads(json_data)

        # Modify dictionary to remove underscores from animal names
        self.class_to_str = {
            str(key): self.class_to_str[key][1].replace("_", " ")
            for key in self.class_to_str
        }
        return self

    def get_animal_name_by_index(self, index) -> str:
        """
        Retrieves the formatted animal name corresponding to the given \
                class index.

        Parameters
        ----------
        index : int
            The class index for which the animal name is to be retrieved.

        Returns
        -------
        str
            The formatted animal name with an exclamation mark, or "unknown \
                    class :(" if the index is not found.

        Raises
        ------
        ValueError
            If the animal dictionary is not loaded before calling this method.
        """
        if not self.class_to_str:
            raise ValueError(
                "Animal dictionary is not loaded. Call load_data() first."
            )

        class_str = self.class_to_str.get(str(index))

        return class_str if class_str else "unknown class"

import json


class ClassLoader:
    def __init__(self, json_file):
        self.json_file = json_file
        self.class_to_str = None

    def load_data(self):
        # Read JSON data from file
        with open(self.json_file, "r") as f:
            json_data = f.read()

        # Parse JSON data into Python dictionary
        self.class_to_str = json.loads(json_data)

        # Modify dictionary to remove underscores from animal names
        self.class_to_str = {
            str(key): self.class_to_str[key][1].replace("_", " ")
            for key in self.class_to_str
        }
        return self

    def get_animal_name_by_index(self, index):
        if not self.class_to_str:
            raise ValueError(
                "Animal dictionary is not loaded. Call load_data() first."
            )

        return self.class_to_str.get(str(index))

    def print_animal_dict(self):
        if not self.class_to_str:
            raise ValueError(
                "Animal dictionary is not loaded. Call load_data() first."
            )

        # Print the resulting dictionary
        for key, value in self.class_to_str.items():
            print(f"{key}: {value}")

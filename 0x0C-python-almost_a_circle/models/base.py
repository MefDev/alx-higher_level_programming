#!/usr/bin/python3
import json
import os


class Base:
    """Manage id attribute in all your future classes
    and avoid duplicating the same code"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize the code"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        jsons = cls.to_json_string([obj.to_dictionary() for obj in list_objs])

        with open(f"{cls.__name__}.json", "w", encoding="utf-8") as file:
            file.write(jsons)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string"""
        return json.loads(json_string or "[]")

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            inst = cls(1, 1)
        elif cls.__name__ == "Square":
            inst = cls(1)
        else:
            inst = None
        if inst:
            inst.update(**dictionary)
            return inst

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        if not os.path.isfile(f"{cls.__name__}.json"):
            return []
        else:
            with open(f"{cls.__name__}.json", "r") as file:
                list_dicts = cls.from_json_string(file.read())
            return [cls.create(**inst) for inst in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save to CSV file"""
        import csv

        try:
            csvs = [x.to_dictionary() for x in list_objs]
        except FileNotFoundError:
            csvs = '[]'
        keys = csvs[0].keys()
        with open(f"{cls.__name__}.csv", 'w', newline='') as file:
            writer = csv.DictWriter(file, keys)
            writer.writeheader()
            writer.writerows(csvs)

    @classmethod
    def load_from_file_csv(cls):
        """Load from CSV file"""
        import csv
        if not os.path.isfile(f"{cls.__name__}.csv"):
            return []

        csvs = []
        with open(f"{cls.__name__}.csv", 'r', newline='') as file:
            reader = csv.DictReader(file)

            for row in reader:
                for key, val in row.items():
                    try:
                        row[key] = int(val)
                    except ValueError:
                        pass
                csvs.append(row)
        return [cls.create(**dic) for dic in csvs]

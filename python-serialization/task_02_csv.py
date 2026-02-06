#!/usr/bin/python3
"""
Docstring for python-serialization.task_02_csv
"""
import csv
import json


def convert_csv_to_json(csv_filename):
    """
        Docstring for convert_csv_to_json

        :param csv_filename: Description
        """
    try:
        data = []
        with open(csv_filename, 'r', encoding='utf-8') as f:
            value = csv.DictReader(f)
            for row in value:
                data.append(row)

        with open('data.json', 'w', encoding='utf-8') as file:
            json.dump(data, file)

        return True
    except (FileNotFoundError, PermissionError, csv.Error):
        return False
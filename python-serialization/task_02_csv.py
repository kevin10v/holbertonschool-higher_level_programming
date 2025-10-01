#!/usr/bin/python3
"""
Module for converting CSV data to JSON format
"""

import csv
import json


def convert_csv_to_json(csv_filename):
    """
    Converts a CSV file into a JSON file (data.json)

    Args:
        csv_filename (str): The name of the CSV file to read

    Returns:
        bool: True if successful, False otherwise
    """
    try:
        data = []
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            reader = csv.DictReader(csv_file)
            for row in reader:
                data.append(row)

        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)

        return True
    except Exception:
        return False

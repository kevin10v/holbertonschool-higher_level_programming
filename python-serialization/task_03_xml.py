#!/usr/bin/python3
"""
Serialization and deserialization using XML
"""

import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    Serialize a Python dictionary into an XML file

    Args:
        dictionary (dict): dictionary to serialize
        filename (str): file where XML will be saved
    """
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
    except Exception:
        return None


def deserialize_from_xml(filename):
    """
    Deserialize XML data from a file back into a Python dictionary

    Args:
        filename (str): file containing XML data

    Returns:
        dict: dictionary reconstructed from XML
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text
        return result
    except Exception:
        return None

import os
import json
from pathlib import Path


class RunicData:
    def __init__(self):
        self.alphabets = {
            "Elder Futhark": self._load_alphabet("Elder Futhark"),
            "Younger Futhark": self._load_alphabet("Younger Futhark"),
            "Anglo-Saxon Futhorc": self._load_alphabet("Anglo-Saxon Futhorc"),
        }

    def _load_alphabet(self, alphabet_name):
        """Load runic alphabet data from files"""
        # In a real implementation, you would load from JSON or a database
        # This is a simplified example

        if alphabet_name == "Elder Futhark":
            return {
                "f": {
                    "name": "fehu",
                    "meaning": "cattle, wealth",
                    "latin_equivalent": "f",
                },
                "u": {
                    "name": "uruz",
                    "meaning": "aurochs (wild ox)",
                    "latin_equivalent": "u",
                },
                "z": {
                    "name": "algiz",
                    "meaning": "protection, elk",
                    "latin_equivalent": "z",
                },
                # Add more runes...
            }
        elif alphabet_name == "Younger Futhark":
            # Similar structure for Younger Futhark
            return {}
        elif alphabet_name == "Anglo-Saxon Futhorc":
            # Similar structure for Anglo-Saxon Futhorc
            return {}

    def get_alphabet(self, name):
        """Get a specific alphabet by name"""
        alphabet_data = self.alphabets.get(name, {})
        for key, rune in alphabet_data.items():
            # Use absolute path based on the current file location
            base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            image_path = os.path.join(
                base_dir, "data", "images", name, f"{rune['name']}.png"
            )
            rune["image_path"] = image_path
        return alphabet_data

    def get_all_alphabet_names(self):
        """Get list of all alphabet names"""
        return list(self.alphabets.keys())

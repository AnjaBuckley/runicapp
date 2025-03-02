import os
import json
from pathlib import Path


class RunicData:
    def __init__(self):
        self.alphabets = {
            "Elder Futhark": self._load_alphabet("elder_futhark"),
            "Younger Futhark": self._load_alphabet("younger_futhark"),
            "Anglo-Saxon Futhorc": self._load_alphabet("anglo_saxon_futhorc"),
        }

    def _load_alphabet(self, alphabet_name):
        """Load runic alphabet data from files"""
        # In a real implementation, you would load from JSON or a database
        # This is a simplified example

        if alphabet_name == "elder_futhark":
            return {
                "f": {
                    "name": "fehu",
                    "image_path": f"data/elder_futhark/fehu.png",
                    "meaning": "cattle, wealth",
                    "latin_equivalent": "f",
                },
                "u": {
                    "name": "uruz",
                    "image_path": f"data/elder_futhark/uruz.png",
                    "meaning": "aurochs (wild ox)",
                    "latin_equivalent": "u",
                },
                # Add more runes...
            }
        elif alphabet_name == "younger_futhark":
            # Similar structure for Younger Futhark
            return {}
        elif alphabet_name == "anglo_saxon_futhorc":
            # Similar structure for Anglo-Saxon Futhorc
            return {}

    def get_alphabet(self, name):
        """Get a specific alphabet by name"""
        return self.alphabets.get(name, {})

    def get_all_alphabet_names(self):
        """Get list of all alphabet names"""
        return list(self.alphabets.keys())

import json
import glob


class LevelsJson:

    def __init__(self):
        self.data = []
        self.levels_json = {}

        self.merge_files()
        self.add_other_info()
        self.generate_final_json()

    def merge_files(self):
        for f in glob.glob("../outputs/*.json"):
            with open(f, ) as infile:
                self.data.append(json.load(infile))

    def add_other_info(self):
        self.levels_json = {"levels": self.data}

    def generate_final_json(self):
        with open("../final/levels.json", 'w') as outfile:
            json.dump(self.levels_json, outfile)


levels = LevelsJson()

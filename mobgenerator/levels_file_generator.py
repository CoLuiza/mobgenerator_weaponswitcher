import json
import glob


class LevelsJson:
    def __init__(self, levels_path, output_path):
        self.data = []
        self.levels_json = {}
        self.levels_path = levels_path
        self.output_path = output_path

        self.merge_files()
        self.add_other_info()
        self.generate_final_json()

    def merge_files(self):
        for f in glob.glob(self.levels_path):
            with open(f, ) as infile:
                self.data.append(json.load(infile))

    def add_other_info(self):
        self.levels_json = {"levels": self.data}

    def generate_final_json(self):
        with open(self.output_path, 'w') as outfile:
            json.dump(self.levels_json, outfile, indent=4)


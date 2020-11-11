from mobgenerator.levels_file_generator import LevelsJson
from mobgenerator.mobgenerator import MobGenerator


def main():
    mob_generator = MobGenerator("levels/level4.xlsx")
    mob_generator.generate_file("level4.json")
    levels = LevelsJson("./outputs/*.json", "./final/levels.json")


if __name__ == '__main__':
    main()

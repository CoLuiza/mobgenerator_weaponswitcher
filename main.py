from mobgenerator.levels_file_generator import LevelsJson
from mobgenerator.mobgenerator import MobGenerator


def main():
    level = 50

    mob_generator = MobGenerator(f"levels/level{level}.xlsx")
    mob_generator.generate_file(f"level{level}.json")
    levels = LevelsJson("./outputs/*.json", "./final/levels.json")


if __name__ == '__main__':
    main()

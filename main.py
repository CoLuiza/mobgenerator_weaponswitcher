from mobgenerator.mobgenerator import MobGenerator


def main():
    mob_generator = MobGenerator("levels/level1.xlsx")
    mob_generator.generate_file("level1.json")


if __name__ == '__main__':
    main()

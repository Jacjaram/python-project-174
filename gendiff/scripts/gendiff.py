import argparse
import json

def main():
    parser = argparse.ArgumentParser(
        description="Compares two configuration files and shows a difference."
    )
    parser.add_argument("first_file", help="First file to compare")
    parser.add_argument("second_file", help="Second file to compare")

    args = parser.parse_args()

    with open(args.first_file) as file1:
        data1 = json.load(file1)

    with open(args.second_file) as file2:
        data2 = json.load(file2)
    print('Contenido primer archivo', data1)
    print('Contenido segundo archivo', data2)


if __name__ == "__main__":
    main()
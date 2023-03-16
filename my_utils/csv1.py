import csv
from pprint import pprint


class HandleCSV:
    filename = (
        "E:\\Python Class\\Pycharm_Project\\pythonProject\\HRConnect\\employees.csv"
    )

    @classmethod
    def read_entire_csv(cls):
        with open(cls.filename, "r") as foo:
            result = csv.DictReader(foo)
            data = []
            for i in result:
                data.append(i)
            return data

    @classmethod
    def read_csv_line_by_line(cls):
        with open(cls.filename) as bar:
            yield bar.readline()


# TODO - ADD MORE SUCH METHODS HERE
# TODO - UNDERSTAND USAGE OF `classmethod


def main():
    h = HandleCSV()
    pprint(h.read_entire_csv())
    pprint(h.read_csv_line_by_line())


if __name__ == "__main__":
    main()

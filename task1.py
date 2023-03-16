"""
Write a program to get details of employees who's salary is > 9000. The output should
be in following format

"""


from pprint import pprint
from my_utils.csv1 import HandleCSV


def first_task():
    data_ = HandleCSV.read_entire_csv()
    final_dict = {}
    for i in data_:
        if int(i["SALARY"]) > 9000:
            number = str(i["PHONE_NUMBER"]).split(".")
            number = "".join(number)
            print(number)
            final_dict["Name"] = i["FIRST_NAME"] + " " + i["LAST_NAME"]
            final_dict["email"] = i["EMAIL"]
            final_dict["phone number"] = number
            pprint(final_dict)


if __name__ == "__main__":
    (first_task())

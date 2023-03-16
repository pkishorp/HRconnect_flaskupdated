"""
Write a program to get "HIRE DATE" of employee who's department is within range 30
to 110 AND who's salary is > 4200.
The output should be in following format.

"""

from my_utils.csv1 import HandleCSV
from pprint import pprint
from datetime import datetime


def second_task():
    data_ = HandleCSV.read_entire_csv()
    final_dict = {}
    for i in data_:
        if 30 < int(i["DEPARTMENT_ID"]) < 110 and int(i["SALARY"]) > 4200:
            str_stamp = i["HIRE_DATE"]
            result = datetime.strptime(str_stamp, "%d-%b-%y")
            hire_date = datetime.strftime(result, "%Y-%m-%d")
            final_dict.setdefault(hire_date, []).append(
                i["FIRST_NAME"] + " " + i["LAST_NAME"]
            )

    return final_dict


if __name__ == "__main__":
    pprint(second_task())

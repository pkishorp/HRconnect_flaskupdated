from my_utils.csv1 import HandleCSV
from datetime import datetime
from flask import Flask

app = Flask(__name__)


@app.route("/tasktwo")
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
    app.run(host="localhost", port=5000, debug=True)

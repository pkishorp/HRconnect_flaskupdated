from my_utils.csv1 import HandleCSV
from flask import Flask


app = Flask(__name__)


@app.route("/taskone")
def first_task():
    data_ = HandleCSV.read_entire_csv()
    final_dict = {}
    j = 1
    for i in data_:
        if int(i["SALARY"]) > 9000:
            final_dict[j] = {
                "Name": i["FIRST_NAME"] + " " + i["LAST_NAME"],
                "Email": i["EMAIL"],
                "Phone number": i["PHONE_NUMBER"].replace(".", ""),
            }
            j += 1
    return final_dict


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

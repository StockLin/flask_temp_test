import io, os
import datetime
from uuid import uuid4
import csv
import pandas as pd
from flask import Flask, render_template, request, send_file, send_from_directory, jsonify


app = Flask(__name__)

@app.route('/')
def home():
    return  render_template("home.html")

@app.route('/export', methods=["POST"])
def export_csv():
    if request.method == "POST":
        base_path = os.path.join(os.getcwd(), "medias")

        data = request.get_json()

        today = datetime.datetime.today() 
        today = today.strftime('%Y%m%d')
        filename = f"{today}-{data['filename']}.csv"

        head = ["Data1", "Data2"]
        body = [
            [data["data1"], data["data1"]],
            [data["data2"], data["data2"]]
        ]

        with open(os.path.join(base_path, filename), 'w', newline='') as csvfile:
            cw = csv.writer(csvfile)
            cw.writerow(head)
            cw.writerows(body)

        return filename

    return render_template("home.html")


@app.route('/download/<path:filename>', methods=['GET', 'POST'])
def download(filename):
    base_path = os.path.join(os.getcwd(), "medias")
    # return send_from_directory(directory=base_path, filename=filename, as_attachment=True)
    return send_file(os.path.join(base_path, filename), as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
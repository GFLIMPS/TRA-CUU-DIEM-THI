from flask import Flask, request, render_template
import csv

app = Flask(__name__)

def load_data():
    data = {}
    with open('diem.csv', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            data[row["SBD"]] = {"hoten": row["HoTen"], "diem": row["Diem"]}
    return data

@app.route("/", methods=["GET", "POST"])
def index():
    ketqua = None
    if request.method == "POST":
        sbd = request.form["sbd"]
        data = load_data()
        if sbd in data:
            ketqua = data[sbd]
        else:
            ketqua = "Không tìm thấy số báo danh."
    return render_template("index.html", ketqua=ketqua)

if __name__ == "__main__":
    app.run()

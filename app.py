from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import pandas as pd #For reading data from excel
import json

app = Flask(__name__)
# Using PyODBC for MS SQL Server connection
app.config["SQLALCHEMY_DATABASE_URI"] = "mssql+pyodbc://sa:1234@May_Lap\\SQLEXPRESS/test?driver=ODBC+Driver+17+for+SQL+Server"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # Disables unnecessary notifications

# Initialize the database
db = SQLAlchemy(app)

#Fetching data from excel
df = pd.read_excel("data.xlsx")  # Load Excel file
columns=[]
col_dtype=[]
for col in df.columns:
    columns.append(col)
    if str(df[col].dtype) == "object":
        col_dtype.append(db.String(500))
    elif str(df[col].dtype) == "datetime64[ns]":
        col_dtype.append(db.DateTime)
    elif str(df[col].dtype) in ["int64", "float64"]:
        col_dtype.append(db.Float)

dic_values={}
#Creating database
class data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)

    for i in range(len(columns)):
        dic_values[columns[i]] = db.Column(col_dtype[i])
    locals().update(dic_values) # Adds each key-value pair of dictionary as class attributes

with app.app_context():
    db.drop_all()
    db.create_all()
with app.app_context():
    db.drop_all()
    db.create_all()

    # Only load if table is empty
    if data.query.count() == 0:
        for _, row in df.iterrows():
            # convert NaN → None for SQL
            record = {k: (v if pd.notna(v) else None)
                      for k, v in row.to_dict().items()}
            db.session.add(data(**record))
        db.session.commit()


@app.route("/")
@app.route("/page/<int:page>")
def home(page=1):
    rows_per_page = 50
    offset = (page - 1) * rows_per_page
    comp_data = data.query.order_by(data.id).offset(offset).limit(rows_per_page).all()
    heading = data.__table__.columns.keys()

    # Prepare chart data from database
    df = pd.read_excel("data.xlsx")
    df_chart = (
        df.groupby("Date")[[
            "Very much satisfied",
            "Satisfied to some extent",
            "Not at all satisfied",
            "Don't Know/Can’t say"
        ]]
        .mean()
        .reset_index()
        .sort_values("Date")
    )
    chart_data = {
        col: [[int(row["Date"].timestamp() * 1000), row[col]] for _, row in df_chart.iterrows()]
        for col in ["Very much satisfied", "Satisfied to some extent", "Not at all satisfied", "Don't Know/Can’t say"]
    }

    return render_template("index.html", Data=comp_data, header=heading, page=page, chart_data=json.dumps(chart_data))
    """return columns"""

@app.route("/msatisfied")
@app.route("/msatisfied/page/<int:page>")
def msatisfied(page=1):
    rows_per_page = 50
    offset = (page - 1) * rows_per_page
    col = data.__table__.c["Very much satisfied"]      # look up by the literal column name
    comp_data = (
        data.query
            .order_by(col.desc())
            .offset(offset)
            .limit(rows_per_page)
            .all()
        )


    heading = data.__table__.columns.keys()
    return render_template("index.html", Data=comp_data, header=heading, page=page)

@app.route("/lsatisfied")
@app.route("/lsatisfied/page/<int:page>")
def lsatisfied(page=1):
    rows_per_page = 50
    offset = (page - 1) * rows_per_page
    col = data.__table__.c["Not at all satisfied"]      # look up by the literal column name
    comp_data = (
        data.query
            .order_by(col.desc())
            .offset(offset)
            .limit(rows_per_page)
            .all()
        )
    heading = data.__table__.columns.keys()
    return render_template("index.html", Data=comp_data, header=heading, page=page)

@app.route("/latest")
@app.route("/latest/page/<int:page>")
def latest(page=1):
    rows_per_page = 50
    offset = (page - 1) * rows_per_page
    comp_data = data.query.order_by(data.Date.desc()).offset(offset).limit(rows_per_page).all()
    heading = data.__table__.columns.keys()
    return render_template("index.html", Data=comp_data, header=heading, page=page)

@app.route("/oldest")
@app.route("/oldest/page/<int:page>")
def oldest(page=1):
    rows_per_page = 50
    offset = (page - 1) * rows_per_page
    comp_data = data.query.order_by(data.Date.asc()).offset(offset).limit(rows_per_page).all()
    heading = data.__table__.columns.keys()
    return render_template("index.html", Data=comp_data, header=heading, page=page)    

if __name__ == "__main__":
    app.run(debug=True)


from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "SF,USA",
    "Salary":"$100,000"
  },
  {
    "id": 2,
    "title": "Data Engineer",
    "location": "Florida,USA",
    "Salary":"$120,000"
  },
  {
    "id": 3,
    "title": "ML Engineer",
    "location": "Remote",
    "Salary":"$200,000"
  },
  {
    "id": 4,
    "title": "Data Scientist",
    "location": "New York, USA",
    "Salary":"$150,000"
  },
  
]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs = JOBS)


@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host = '0.0.0.0', debug = True)
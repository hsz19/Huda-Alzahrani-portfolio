from flask import Flask, render_template

from database import load_projects_from_db

app = Flask(__name__)



@app.route("/")
def hello_world():
  projects = load_projects_from_db()
  return render_template("home.html", myskills = projects, myname = 'Huda AlZahrani')
  
  
if __name__ == "__main__":
  print("i'm inside the if")
  app.run(host="0.0.0.0", debug=True)
  
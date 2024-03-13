from flask import Flask, render_template

app = Flask(__name__)
project = [
  {'id':1,
  'project' : 'web scrapping',
 'skills' : 'urllib python,python requests,selenium'},
  {'id':2,
    'project' : 'Ai model for flear',
   'skills' : 'python pandas , matbolotlip,microsoft azure,pychapgpt'}  
]


@app.route("/")
def hello_world():
  return render_template("home.html", myskills = project,
                        myname = 'Huda AlZahrani')
  
  
if __name__ == "__main__":
  print("i'm inside the if")
  app.run(host="0.0.0.0", debug=True)
  
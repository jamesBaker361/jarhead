import unirest
from appJar import gui
import csv

def print_res(response):
	app.setLabel("Pos %",response.body.get('pos_percent'))
	app.setLabel("Neg %",response.body.get('neg_percent'))
	app.setLabel("Mid %",response.body.get('mid_percent'))

def sendText(b):
	text=app.getEntry("text")
	response = unirest.post("https://text-sentiment.p.mashape.com/analyze",
  headers={
    "X-Mashape-Key": "sHqWQJNzJ5mshM3H9EFUCNeG08nzp13N39JjsnjzH8bxFL8tHZ",
    "Content-Type": "application/x-www-form-urlencoded",
    "Accept": "application/json"
  },
  params={
    "text": text
  },
  callback=print_res
)


app=gui()
#app.setIcon("sofia.png")
app.setTitle("Analyzer")
app.setGeometry(400,400)
app.setFg("yellow")
app.setBg("purple")

app.addEntry("text",1,0,3,1)

app.addButton("Analyze",sendText,5,0,1,1)

app.addLabel("Result","Results")

app.addLabel("Neg Label","Neg %: ",8,0)
app.addLabel("Pos Label","Pos %: ",8,5)
app.addLabel("Mid Label","Mid %: ",8,10)

app.addLabel("Neg %","",10,0)
app.addLabel("Pos %","",10,5)
app.addLabel("Mid %","",10,10)

app.addLabel("secret","",15,15)
#app.

app.go()
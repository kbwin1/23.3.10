from collections import Counter
from flask import Flask
from flask import request, render_template,redirect,flash,session

from random import randint,choice,sample
from surveys import satisfaction_survey

app=Flask(__name__)
app.config['SECRET_KEY'] = "test_flask_23"



Questions=len(satisfaction_survey.questions)
@app.route("/")
def wlecome():
    session['response']=[]
    return render_template("home.html")



@app.route("/survey")
def question_Generator():
    count =len(session["response"])
    title=satisfaction_survey.title
    instructions=satisfaction_survey.instructions
    question=satisfaction_survey.questions[count].question
    choices=satisfaction_survey.questions[count].choices
    return render_template('html.html',count=count,title=title,instructions=instructions,question=question,choices=choices)

@app.route("/q/0", methods=["POST"])
def add():
    answer=request.form['answer']
    an=session['response']
    count =len(an)

    if answer in an:
        return redirect("/survey")
    else:
        an.append(answer)
        session['response']= an
        
    if (count + 1 )== Questions:
        return render_template('thanks.html',)
    else:
        return redirect("/survey")

@app.route("/reset")
def rese(): 
    an=session['response']
    an.clear()
    session['response']= an
    return redirect("/survey")

@app.route("/back")
def back():
    an=session['response']
    session['response'].pop()
    session['response']= an
    return redirect("/survey")




     
     
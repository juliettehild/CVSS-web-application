from flask import Flask, render_template, request, url_for, redirect, session, flash
from vardata import avlist, aclist, prlist, uilist, slist, clist, ilist, alist
from string import Template
from datetime import timedelta
from werkzeug.utils import secure_filename
# from flask_sqlalchemy import SQLAlchemy
import sys, os 

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes=5)
"""
app.config['SQLALCHEMY_DATABASE-URI'] = 'sqlite:///users.sqlite3'
app.config["SQLALCHEMY_TRACK-MODIFICATIONS"] = False

db = SQLAlchemy(app)

class cves(db.Model): 
    _id = db.Column("id", db.Integer, primary_key=True)
    name = db.Column("name", db.String(100))
    cve = db.Column("cve", db.String(100))

def __init__(self, name, cve):
    self.name = name
    self.cve = cve
"""


@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        session.permanent = True
        cve = request.form['cve']
        session['cve'] = cve
        return redirect(url_for('report'))
    else:
        return render_template('login.html')

@app.route('/logout', methods=['GET', 'POST'])
def logout():
    if "cve" in session:
        cve = session["cve"]
        flash(f"You finished the session with {cve}", "info")
        if request.method == "POST":
            session.pop('cve', None)
            session.pop('question', None)
            session.pop('ques', None)
            session.pop('quest', None)
            session.pop('questi', None)
            session.pop('questio', None)
            session.pop('cquestion', None)
            session.pop('iquestion', None)
            session.pop('aquestion', None)
            session.pop('sum', None)
            return redirect(url_for('login'))
        else:
            return render_template('report.html')
    else:
        return render_template('report.html')

@app.route('/decisionTree')
def decisionTree():
    if "cve" in session:
        # adress the html file
        # be cautios that the file is named templates, to work
        ques = aclist[0]
        quest = prlist[0]
        questi = uilist[0]
        questio = slist[0]
        question = avlist[0]
        cquestion = clist[0]
        iquestion = ilist[0]
        aquestion = alist[0]
        return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questio=questio)
    else:
        flash(f"Please enter an Id first.", "info")
        return redirect(url_for('login'))  

@app.route('/calculator')
def calculator():
    if "cve" in session:
        return render_template('calculator.html')
    else:
        flash(f"Please enter an Id first.", "info")
        return redirect(url_for('login'))  

@app.route('/report', methods=['GET', 'POST'])
def report():
    # email = None
    if "cve" in session:
        avTableNew =  session.get('question', None)
        acTableNew =  session.get('ques', None)
        prTableNew =  session.get('quest', None)
        uiTableNew =  session.get('questi', None)
        sTableNew =  session.get('questio', None)
        cTableNew =  session.get('cquestion', None)
        iTableNew =  session.get('iquestion', None)
        aTableNew =  session.get('aquestion', None)
        sum =  session.get('sum', None)
        cve =  session.get('cve', None)
        return render_template('report.html', avTableNew=avTableNew, acTableNew=acTableNew, prTableNew=prTableNew, uiTableNew=uiTableNew, sTableNew=sTableNew, cTableNew=cTableNew, iTableNew=iTableNew, aTableNew=aTableNew, sum=sum, cve=cve)
    else:
        flash(f"Please enter an Id first.", "info")
        return redirect(url_for('login'))    


@app.route('/reportsend', methods=['GET', 'POST'])
def reportsend():
    if request.method == "POST":
        avPath =  session.get('static', None)
        avPath2 =  session.get('sttic', None)
        avPath3 =  session.get('stic', None)
        avPath4 =  session.get('stc', None)
        avPath5 =  session.get('sc', None)
        acPath =  session.get('acst', None)
        prPath =  session.get('prstatic', None) 
        prPath2 =  session.get('prsttic', None) 
        prPath3 =  session.get('prsttc', None) 
        uiPath =  session.get('uist', None)
        sPath =  session.get('sst', None)
        cPath =  session.get('cstatic', None)
        cPath2 =  session.get('cstatic2', None)
        iPath =  session.get('istatic', None)
        iPath2 =  session.get('istatic2', None)
        aPath =  session.get('astatic', None)
        aPath2 =  session.get('astatic2', None)
        avTableNew =  session.get('question', None)
        acTableNew =  session.get('ques', None)
        prTableNew =  session.get('quest', None)
        uiTableNew =  session.get('questi', None)
        sTableNew =  session.get('questio', None)
        cTableNew =  session.get('cquestion', None)
        iTableNew =  session.get('iquestion', None)
        aTableNew =  session.get('aquestion', None)
        sum =  session.get('sum', None)
        cve =  session.get('cve', None)
        filename = request.form['filename']
        description = request.form['description']
        flash(f"You have saved the file {filename}.txt", "info")
        with open(os.path.join(os.path.dirname(__file__), '{}.txt'.format(filename)), 'w') as textfile:
            textfile.write('The CVE: {}\n\n The Description:\n {}\n\n Attack Vector Path:\n {}\n {}\n {}\n {}\n {}\n {}\n\n Attack Complexity Path:\n {}\n {}\n\n Privileges Required Path:\n {}\n {}\n {}\n {}\n\n User Interface Path:\n {}\n {}\n\n Scope Path:\n {}\n {}\n\n Confidentiality Path:\n {}\n {}\n {}\n\n Integrity Path:\n {}\n {}\n {}\n\n Availability Path:\n {}\n {}\n {}\n\n The final score: {}\n'.format(cve, description, avPath, avPath2, avPath3, avPath4, avPath5, avTableNew, acPath, acTableNew, prPath, prPath2, prPath3, prTableNew, uiPath, uiTableNew, sPath, sTableNew, cPath, cPath2, cTableNew, iPath, iPath2, iTableNew, aPath, aPath2, aTableNew, sum,))
        return redirect(url_for('login'))
        # return render_template('report.html', avTableNew=avTableNew, acTableNew=acTableNew, prTableNew=prTableNew, uiTableNew=uiTableNew, sTableNew=sTableNew, cTableNew=cTableNew, iTableNew=iTableNew, aTableNew=aTableNew, sum=sum, cve=cve, filename=filename, description=description)
    else:
        return render_template('report.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == "POST":
        return render_template('report.html')
    else:
        return render_template('report.html')

@app.route('/send', methods=['GET', 'POST'])
def send(sum=sum):
    if request.method == 'POST':
        AV = request.form['AV']
        AC = request.form['AC']
        PR = request.form['PR']
        UI = request.form['UI'] 
        S = request.form['S']
        C = request.form['C']
        I = request.form['I']
        A = request.form['A']
        
        ISS = 1 - ((1 - float(C)) * (1 - float(I)) * (1 - float(A)))
        exploiability = 8.22 * float(AV) * float(AC) * float(PR) * float(UI)

        if S == 'unchanged':
            impact = 6.42 * ISS
            if impact <= 0:
                sum = 0
                session['sum'] = sum
                return redirect(url_for('report'))
                # return render_template('report.html', sum=sum)
                # return render_template('calculator.html', sum=sum)
            else: 
                sum = round((impact + exploiability), 2)
                session['sum'] = sum
                return redirect(url_for('report'))
                # return render_template('report.html', sum=sum)
                # return render_template('calculator.html', sum=sum)
        elif S == 'changed':
            impact = (7.52 * (ISS - 0.029)) - (3.25 * (ISS - 0.02))
            if impact <= 0:
                sum = 0
                session['sum'] = sum
                return redirect(url_for('report'))
                # return render_template('report.html', sum=sum)
                # return render_template('calculator.html', sum=sum)
            else:
                sum = round((1.08 * (impact + exploiability)), 3)
                session['sum'] = sum
                return redirect(url_for('report'))
                # return render_template('report.html', sum=sum)
                # return render_template('calculator.html', sum=sum)
        else: 
            return render_template('calculator.html')
           
@app.route('/av', methods=['GET', 'POST'])
def av():
    static = avlist[0]
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    if request.method=='POST':
        if request.form.get("y"):
            static = avlist[5]
            question = avlist[1]
            return render_template('avYes.html', question=question, ques=ques, quest=quest, questio=questio, static=static, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("n"):
            static = avlist[6]
            question = avlist[2]
            return render_template('avNo.html', question=question, ques=ques, quest=quest, questio=questio, static=static, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("u"):
            static = avlist[7]
            question = avlist[3]
            session['question'] = avlist[3]
            session['static'] = avlist[7]
            return redirect(url_for('report'))
            # return render_template('avNo.html', question=question, ques=ques, quest=quest, questio=questio, static=static, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questio=questio, static=static, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)

@app.route('/avyes', methods=['GET', 'POST'])
def avyes():
    static = avlist[5]
    sttic = avlist [0]
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[1]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    if request.method=='POST':
        if request.form.get("y"):
            static = avlist[5]
            sttic = avlist [9]
            question = avlist[3]
            session['question'] = avlist[3]
            session['static'] = avlist[5]
            session['sttic'] = avlist[9]
            return redirect(url_for('report'))
        elif request.form.get("n"):
            static = avlist[5]
            sttic = avlist [10]
            question = avlist[4]
            return render_template('avYesNo.html', question=question, ques=ques, quest=quest, questio=questio, static=static, sttic=sttic, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("u"):
            static = avlist[5]
            sttic = avlist [11]
            question = avlist[3]
            session['question'] = avlist[3]
            session['static'] = avlist[5]
            session['sttic'] = avlist[11]
            return redirect(url_for('report'))
        else:
            return render_template('rubric.html', ques=ques, sttic=sttic)

@app.route('/avyesno', methods=['GET', 'POST'])
def avyesno():
    static = avlist[5]
    sttic = avlist [0]
    stc = avlist [0]
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[1]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    if request.method=='POST':
        if request.form.get("y"):
            static = avlist[5]
            sttic = avlist [10]
            stc = avlist [19]
            question = avlist[23]
            return render_template('avYesNoYes.html', question=question, ques=ques, quest=quest, questio=questio, static=static, sttic=sttic, stc=stc, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("n"):
            static = avlist[5]
            sttic = avlist [10]
            stc = avlist [20]
            question = avlist[24]
            session['question'] = avlist[24]
            session['static'] = avlist[5]
            session['sttic'] = avlist[10]
            session['stc'] = avlist[20]
            return redirect(url_for('report'))
            # return render_template('avYesNo.html', question=question, ques=ques, quest=quest, questio=questio, static=static, sttic=sttic, stc=stc, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("u"):
            static = avlist[5]
            sttic = avlist [10]
            stc = avlist [21]
            question = avlist[24]
            session['question'] = avlist[24]
            session['static'] = avlist[5]
            session['sttic'] = avlist[10]
            session['stc'] = avlist[21]
            return redirect(url_for('report'))
            # return render_template('avYesNo.html', question=question, ques=ques, quest=quest, questio=questio, static=static, sttic=sttic, stc=stc, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        else:
            return render_template('rubric.html', ques=ques, sttic=sttic, stc=stc)

@app.route('/avyesnoyes', methods=['GET', 'POST'])
def avyesnoyse():
    static = avlist[5]
    sttic = avlist [0]
    stc = avlist [0]
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[1]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    if request.method=='POST':
        if request.form.get("y"):
            static = avlist[5]
            sttic = avlist [10]
            stc = avlist [19]
            sc = avlist [25]
            question = avlist[18]
            session['question'] = avlist[18]
            session['static'] = avlist[5]
            session['sttic'] = avlist[10]
            session['stc'] = avlist[19]
            session['sc'] = avlist[25]
            return redirect(url_for('report'))
            # return render_template('avYesNoYes.html', question=question, ques=ques, quest=quest, questio=questio, static=static, sttic=sttic, stc=stc, sc=sc, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("n"):
            static = avlist[5]
            sttic = avlist [10]
            stc = avlist [19]
            sc = avlist [26]
            question = avlist[24]
            session['question'] = avlist[24]
            session['static'] = avlist[5]
            session['sttic'] = avlist[10]
            session['stc'] = avlist[19]
            session['sc'] = avlist[26]
            return redirect(url_for('report'))
            # return render_template('avYesNoYes.html', question=question, ques=ques, quest=quest, questio=questio, static=static, sttic=sttic, stc=stc, sc=sc, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("u"):
            static = avlist[5]
            sttic = avlist [10]
            stc = avlist [19]
            sc = avlist [27]
            question = avlist[24]
            session['question'] = avlist[24]
            session['static'] = avlist[5]
            session['sttic'] = avlist[10]
            session['stc'] = avlist[19]
            session['sc'] = avlist[27]
            return redirect(url_for('report'))
            # return render_template('avYesNoYes.html', question=question, ques=ques, quest=quest, questio=questio, static=static, sttic=sttic, stc=stc, sc=sc, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        else:
            return render_template('rubric.html', ques=ques, sttic=sttic, stc=stc)

@app.route('/avno', methods=['GET', 'POST'])
def avno():
    static = avlist[5]
    stic = avlist [0]
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[1]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    if request.method=='POST':
        if request.form.get("y"):
            static = avlist[6]
            stic = avlist [13]
            question = avlist[17]
            session['question'] = avlist[17]
            session['static'] = avlist[6]
            session['stic'] = avlist[13]
            return redirect(url_for('report'))
            # return render_template('avNo.html', question=question, ques=ques, quest=quest, questio=questio, static=static, stic=stic, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("n"):
            static = avlist[6]
            stic = avlist [14]
            question = avlist[18]
            session['question'] = avlist[18]
            session['static'] = avlist[6]
            session['stic'] = avlist[14]
            return redirect(url_for('report'))
            # return render_template('avNo.html', question=question, ques=ques, quest=quest, questio=questio, static=static, stic=stic, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("u"):
            static = avlist[6]
            stic = avlist [15]
            question = avlist[18]
            session['question'] = avlist[18]
            session['static'] = avlist[6]
            session['stic'] = avlist[15]
            return redirect(url_for('report'))
            # return render_template('avNo.html', question=question, ques=ques, quest=quest, questio=questio, static=static, stic=stic, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        else:
            return render_template('rubric.html', ques=ques, stic=stic)

@app.route('/ac', methods=['GET', 'POST'])
def ac():
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    acst = aclist[0]
    if request.method=='POST':
        if request.form.get("y"):
            acst = aclist[3]
            ques = aclist[1]
            session['ques'] = aclist[1]
            session['acst'] = aclist[3]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questio=questio, acst=acst, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("n"):
            acst = aclist[4]
            ques = aclist[2]
            session['ques'] = aclist[2]
            session['acst'] = aclist[4]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questio=questio, acst=acst, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("u"):
            acst = aclist[5]
            ques = aclist[1]
            session['ques'] = aclist[1]
            session['acst'] = aclist[5]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questio=questio, acst=acst, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questio=questio, acst=acst, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
            
@app.route('/pr', methods=['GET', 'POST'])
def pr():
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    if request.method=='POST':
        if request.form.get("y"):
            prstatic = prlist[6]
            quest = prlist[1]
            return render_template('prYes.html', question=question, ques=ques, quest=quest, questio=questio, prstatic=prstatic, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("n"):
            prstatic = prlist[7]
            quest = prlist[3]
            session['quest'] = prlist[3]
            session['prstatic'] = prlist[7]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questio=questio, prstatic=prstatic, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("u"):
            prstatic = prlist[8]
            quest = prlist[3]
            session['quest'] = prlist[3]
            session['prstatic'] = prlist[8]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questio=questio, prstatic=prstatic, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questio=questio, prstatic=prstatic, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)

@app.route('/pryes', methods=['GET', 'POST'])
def pryes():
    ques = aclist[0]
    quest = prlist[1]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    prstatic = prlist[6]
    if request.method=='POST':
        if request.form.get("y"):
            prsttic = prlist[9]
            quest = prlist[2]
            return render_template('prYesYes.html', question=question, ques=ques, quest=quest, questio=questio, prsttic=prsttic, prstatic=prstatic, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("n"):
            prsttic = prlist[10]
            quest = prlist[3]
            session['quest'] = prlist[3]
            session['prstatic'] = prlist[7]
            session['prsttic'] = prlist[10]
            return redirect(url_for('report'))
            # return render_template('prYes.html', question=question, ques=ques, quest=quest, questio=questio, prsttic=prsttic, prstatic=prstatic, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        elif request.form.get("u"):
            prsttic = prlist[11]
            quest = prlist[3]
            session['quest'] = prlist[3]
            session['prstatic'] = prlist[7]
            session['prsttic'] = prlist[11]
            return redirect(url_for('report'))
            # return render_template('prYes.html', question=question, ques=ques, quest=quest, questio=questio, prsttic=prsttic, prstatic=prstatic, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questio=questio, prsttic=prsttic, prstatic=prstatic, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, questi=questi)

@app.route('/pryesyes', methods=['GET', 'POST'])
def pryesyes():
    ques = aclist[0]
    quest = prlist[2]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    prstatic = prlist[6]
    prsttic = prlist[9]
    if request.method=='POST':
        if request.form.get("y"):
            prsttic = prlist[9]
            prsttc = prlist[12]
            quest = prlist[5]
            session['quest'] = prlist[5]
            session['prstatic'] = prlist[7]
            session['prsttic'] = prlist[9]
            session['prsttc'] = prlist[12]
            return redirect(url_for('report'))
            # return render_template('prYesYes.html', question=question, ques=ques, quest=quest, questio=questio, prsttc=prsttc, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, prsttic=prsttic, prstatic=prstatic, questi=questi)
        elif request.form.get("n"):
            prsttic = prlist[9]
            prsttc = prlist[13]
            quest = prlist[4]
            session['quest'] = prlist[4]
            session['prstatic'] = prlist[7]
            session['prsttic'] = prlist[9]
            session['prsttc'] = prlist[13]
            return redirect(url_for('report'))
            # return render_template('prYesYes.html', question=question, ques=ques, quest=quest, questio=questio, prsttc=prsttc, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, prsttic=prsttic, prstatic=prstatic, questi=questi)
        elif request.form.get("u"):
            prsttic = prlist[9]
            prsttc = prlist[14]
            quest = prlist[3]
            session['quest'] = prlist[3]
            session['prstatic'] = prlist[7]
            session['prsttic'] = prlist[9]
            session['prsttc'] = prlist[14]
            return redirect(url_for('report'))
            # return render_template('prYesYes.html', question=question, ques=ques, quest=quest, questio=questio, prsttc=prsttc, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, prsttic=prsttic, prstatic=prstatic, questi=questi)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questio=questio, prsttc=prsttc, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, prsttic=prsttic, prstatic=prstatic, questi=questi)

@app.route('/ui', methods=['GET', 'POST'])
def ui():
    ques = aclist[0]
    quest = prlist[0]
    questio = slist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    uist = uilist[0]
    if request.method=='POST':
        if request.form.get("y"):
            uist = uilist[3]
            questi = uilist[1]
            session['questi'] = uilist[1]
            session['uist'] = uilist[3]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, uist=uist)
        elif request.form.get("n"):
            uist = uilist[4]
            questi = uilist[2]
            session['questi'] = uilist[2]
            session['uist'] = uilist[4]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, uist=uist)
        elif request.form.get("u"):
            uist = uilist[5]
            questi = uilist[2]
            session['questi'] = uilist[2]
            session['uist'] = uilist[5]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, uist=uist)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, uist=uist)

@app.route('/s', methods=['GET', 'POST'])
def s():
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    sst = slist[0]
    if request.method=='POST':
        if request.form.get("y"):
            sst = slist[3]
            questio = slist[1]
            session['questio'] = slist[1]
            session['sst'] = slist[3]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, sst=sst)
        elif request.form.get("n"):
            sst = slist[4]
            questio = slist[2]
            session['questio'] = slist[2]
            session['sst'] = slist[4]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, sst=sst)
        elif request.form.get("u"):
            sst = slist[5]
            questio = slist[1]
            session['questio'] = slist[1]
            session['sst'] = slist[5]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, sst=sst)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, sst=sst)

@app.route('/c', methods=['GET', 'POST'])
def c():
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    if request.method=='POST':
        if request.form.get("y"):
            cstatic = clist[4]
            cquestion = clist[7]
            return render_template('cyes.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, cstatic=cstatic)
        elif request.form.get("n"):
            cstatic = clist[5]
            cquestion = clist[2]
            session['cquestion'] = clist[2]
            session['cstatic'] = clist[5]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, cstatic=cstatic)
        elif request.form.get("u"):
            cstatic = clist[6]
            cquestion = clist[1]
            session['cquestion'] = clist[1]
            session['cstatic'] = clist[6]
            return redirect(url_for('report'))
            #return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, cstatic=cstatic)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, cstatic=cstatic)

@app.route('/cyes', methods=['GET', 'POST'])
def cyes():
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    if request.method=='POST':
        if request.form.get("y"):
            cstatic = clist[4]
            cstatic2 = clist[8]
            cquestion = clist[1]
            session['cquestion'] = clist[1]
            session['cstatic'] = clist[4]
            session['cstatic2'] = clist[8]
            return redirect(url_for('report'))
            # return render_template('cyes.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, cstatic=cstatic, cstatic2=cstatic2)
        elif request.form.get("n"):
            cstatic = clist[4]
            cstatic2 = clist[9]
            cquestion = clist[2]
            session['cquestion'] = clist[2]
            session['cstatic'] = clist[4]
            session['cstatic2'] = clist[9]
            return redirect(url_for('report'))
            # return render_template('cyes.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, cstatic=cstatic, cstatic2=cstatic2)
        elif request.form.get("u"):
            cstatic = clist[4]
            cstatic2 = clist[10]
            cquestion = clist[1]
            session['cquestion'] = clist[1]
            session['cstatic'] = clist[4]
            session['cstatic2'] = clist[10]
            return redirect(url_for('report'))
            # return render_template('cyes.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, cstatic=cstatic, cstatic2=cstatic2)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, cstatic=cstatic, cstatic2=cstatic2)

@app.route('/i', methods=['GET', 'POST'])
def i():
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    if request.method=='POST':
        if request.form.get("y"):
            istatic = ilist[4]
            iquestion = ilist[7]
            return render_template('iyes.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, istatic=istatic)
        elif request.form.get("n"):
            istatic = ilist[5]
            iquestion = ilist[2]
            session['iquestion'] = ilist[2]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, istatic=istatic)
        elif request.form.get("u"):
            istatic = ilist[6]
            iquestion = ilist[1]
            session['iquestion'] = ilist[1]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, istatic=istatic)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, istatic=istatic)

@app.route('/iyes', methods=['GET', 'POST'])
def iyes():
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    if request.method=='POST':
        if request.form.get("y"):
            istatic = ilist[4]
            istatic2 = ilist[8]
            iquestion = ilist[1]
            session['iquestion'] = ilist[1]
            return redirect(url_for('report'))
            # return render_template('iyes.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, istatic=istatic, istatic2=istatic2)
        elif request.form.get("n"):
            istatic = ilist[4]
            istatic2 = ilist[9]
            iquestion = ilist[2]
            session['iquestion'] = ilist[2]
            return redirect(url_for('report'))
            # return render_template('iyes.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, istatic=istatic, istatic2=istatic2)
        elif request.form.get("u"):
            istatic = ilist[4]
            istatic2 = ilist[10]
            iquestion = ilist[1]
            session['iquestion'] = ilist[1]
            return redirect(url_for('report'))
            # return render_template('iyes.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, istatic=istatic, istatic2=istatic2)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, istatic=istatic, istatic2=istatic2)

@app.route('/a', methods=['GET', 'POST'])
def a():
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    if request.method=='POST':
        if request.form.get("y"):
            astatic = alist[4]
            aquestion = alist[7]
            return render_template('ayes.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, astatic=astatic)
        elif request.form.get("n"):
            astatic = alist[5]
            aquestion = alist[2]
            session['aquestion'] = alist[2]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, astatic=astatic)
        elif request.form.get("u"):
            astatic = alist[6]
            aquestion = alist[1]
            session['aquestion'] = alist[1]
            return redirect(url_for('report'))
            # return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, astatic=astatic)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, astatic=astatic)

@app.route('/ayes', methods=['GET', 'POST'])
def ayes():
    ques = aclist[0]
    quest = prlist[0]
    questi = uilist[0]
    questio = slist[0]
    question = avlist[0]
    cquestion = clist[0]
    iquestion = ilist[0]
    aquestion = alist[0]
    if request.method=='POST':
        if request.form.get("y"):
            astatic = alist[4]
            astatic2 = alist[8]
            aquestion = alist[1]
            session['aquestion'] = alist[1]
            return redirect(url_for('report'))
            # return render_template('ayes.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, astatic=astatic, astatic2=astatic2)
        elif request.form.get("n"):
            astatic = alist[4]
            astatic2 = alist[9]
            aquestion = alist[2]
            session['aquestion'] = alist[2]
            return redirect(url_for('report'))
            # return render_template('ayes.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, astatic=astatic, astatic2=astatic2)
        elif request.form.get("u"):
            astatic = alist[4]
            astatic2 = alist[10]
            aquestion = alist[1]
            session['aquestion'] = alist[1]
            return redirect(url_for('report'))
            # return render_template('ayes.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, astatic=astatic, astatic2=astatic2)
        else:
            return render_template('rubric.html', question=question, ques=ques, quest=quest, questi=questi, questio=questio, cquestion=cquestion, iquestion=iquestion, aquestion=aquestion, astatic=astatic, astatic2=astatic2)

if __name__ == "__main__":  
    # db.creat_all()
    app.run(debug=True)
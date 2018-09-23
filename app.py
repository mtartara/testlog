from flask import Flask, render_template, json, request
import random
import string
import json
import datetime
import  time

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/LogString',methods=['POST','GET'])
def LogString():
    nrow = int(request.form['nrow'])
    dest = request.form['dest']
    id_session = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    for i in range(nrow):
        data = {}
        data['ID_Sessione'] = id_session
        data['Timestamp'] = str(datetime.datetime.now())
        data['Username'] = ''.join(random.choice(string.ascii_lowercase) for _ in range(10)) + '@' +''.join(random.choice(string.ascii_lowercase) for _ in range(5)) + '.com'
        data['Sorgente'] = '.'.join([str(random.randint(0, 255)) for x in range(4)])
        data['Servizio'] = random.choice(["HTTPS", "HTTP", "FTP", "SFTP"])
        data['Tipo_Evento'] = None
        data['Profilo_Utenza'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
        data['OCPLOGDEST'] = dest
        print json.dumps(data)


    return "<span>Loggged! Rows id: %s</span>" % id_session

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)

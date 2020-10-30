from flask import Flask
from flask import render_template
from flask import request
import subprocess as sp

app = Flask(__name__)

@app.route("/")
def root() :
    return render_template('getip.html')

@app.route('/iperf')
def iperf_page():
    return render_template('iperf.html')

@app.route('/runiperf', methods=['POST', 'GET'])
def run_iperf():
    cm = 'iperf3 -c %s -p 5001 -t 60' % request.form['ueip']
    sp.Popen(cm, shell=True, stdout=sp.PIPE)
    return render_template('timer.html') 


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')

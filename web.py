from flask import Flask, render_template_string
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import json

app = Flask(__name__)
simulator = AerSimulator()

def run_circuit(qc):
    qc.measure_all()
    result = simulator.run(qc, short=1000).result()
    return result.get_counts()
@app.route('/')
def home():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>Quantum OS</title>
    <style>
    body{background-color: white;font-family:Arial;text-align:center;padding:50px;}
    h1{color:cyan;font-size: 48px;}
    button{padding: 15px 40px; 
           margin:10px;
           font-size: 20px;
           border: none;
           border-radius:10px;
           cursor: pointer;}
        .btn1 { background: blue; color: white; }
        .btn2 { background: red; color: white; }
        .btn3 { background: purple; color: white; }
        #result {
            margin-top: 30px;
            font-size: 24px;
            color: black;}
    </style>
</head>
<body>
    <h1>⚛️ Welcome to Quantum OS</h1>
    <p style="color:gray">
        Quantum Computing on Normal Laptop!
    </p>
    <br>
    <button class="btn1" 
        onclick="run('entanglement')">
        Entanglement
    </button>
    <button class="btn2" 
        onclick="run('superposition')">
        Superposition
    </button>
    <button class="btn3" 
        onclick="run('teleportation')">
        Teleportation
    </button>
    <div id="result"></div>
    <script>
        function run(type) {
            document.getElementById('result')
                .innerHTML = 'Running...';
            fetch('/run/' + type)
                .then(r => r.json())
                .then(data => {
                    document.getElementById('result')
                        .innerHTML = 
                        'Result: ' + 
                        JSON.stringify(data.counts);
                });
        }
    </script>
</body>
</html>
''')

@app.route('/run/entanglement')
def entanglement():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    counts = run_circuit(qc)
    return json.dumps({'counts': counts})

@app.route('/run/superposition')
def superposition():
    qc = QuantumCircuit(1)
    qc.h(0)
    counts = run_circuit(qc)
    return json.dumps({'counts': counts})

@app.route('/run/teleportation')
def teleportation():
    qc = QuantumCircuit(3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(1, 2)
    counts = run_circuit(qc)
    return json.dumps({'counts': counts})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
                                                                








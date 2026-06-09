from flask import Flask, render_template_string
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import json

app = Flask(__name__)
simulator = AerSimulator()

def run_circuit(qc):
    qc.measure_all()
    result = simulator.run(qc, shots=1000).result()
    return result.get_counts()

@app.route('/')
def home():
    return render_template_string('''
<!DOCTYPE html>
<html>
<head>
    <title>Quantum OS</title>
    <style>
        * { margin:0; padding:0; box-sizing:border-box; }
        body {
            background: #000;
            color: white;
            font-family: Arial;
            min-height: 100vh;
        }
        .header {
            background: linear-gradient(135deg, #0a0a2e, #1a1a4e);
            padding: 40px;
            text-align: center;
            border-bottom: 2px solid #00ffff;
        }
        .title {
            font-size: 48px;
            font-weight: bold;
            color: #00ffff;
            text-shadow: 0 0 20px #00ffff;
        }
        .subtitle {
            color: #888;
            margin-top: 10px;
            font-size: 18px;
        }
        .container {
            max-width: 900px;
            margin: 40px auto;
            padding: 20px;
        }
        .cards {
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            @media (max-width: 768px) 
                {
            .cards {
                    grid-template-columns: 1fr;
                   }
            .title {
                    font-size: 32px;
                   }
            .card {
                   padding: 20px;
                  }
                }
            gap: 20px;
            margin-top: 30px;
        }
        .card {
            background: #0a0a2e;
            border-radius: 15px;
            padding: 30px 20px;
            text-align: center;
            border: 1px solid #333;
            cursor: pointer;
            transition: all 0.3s;
        }
        .card:hover {
            transform: translateY(-5px);
            border-color: #00ffff;
            box-shadow: 0 0 20px rgba(0,255,255,0.3);
        }
        .card-icon {
            font-size: 48px;
            margin-bottom: 15px;
        }
        .card-title {
            font-size: 20px;
            font-weight: bold;
            margin-bottom: 10px;
            color: #00ffff;
        }
        .card-desc {
            color: #888;
            font-size: 14px;
        }
        .btn {
            margin-top: 20px;
            padding: 12px 30px;
            border: none;
            border-radius: 25px;
            font-size: 16px;
            cursor: pointer;
            font-weight: bold;
            transition: all 0.3s;
        }
        .btn1 { background: #0066ff; color: white; }
        .btn2 { background: #ff3333; color: white; }
        .btn3 { background: #9933ff; color: white; }
        .btn:hover { opacity: 0.8; transform: scale(1.05); }
        .result-box {
            margin-top: 30px;
            background: #0a0a2e;
            border: 1px solid #00ffff;
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            display: none;
        }
        .result-title {
            color: #00ffff;
            font-size: 20px;
            margin-bottom: 15px;
        }
        .result-data {
            color: #fff;
            font-size: 18px;
        }
        .loading {
            color: #888;
            font-size: 18px;
        }
        .footer {
            text-align: center;
            padding: 30px;
            color: #444;
            border-top: 1px solid #222;
            margin-top: 50px;
        }
    </style>
</head>
<body>
    <div class="header">
        <div class="title">⚛️ Quantum OS</div>
        <div class="subtitle">
            Quantum Computing on Normal Laptop & Phone
        </div>
    </div>

    <div class="container">
        <div class="cards">
            <div class="card">
                <div class="card-icon">🔗</div>
                <div class="card-title">Entanglement</div>
                <div class="card-desc">
                    2 qubits instantly connected
                </div>
                <button class="btn btn1"
                    onclick="run('entanglement')">
                    Run
                </button>
            </div>

            <div class="card">
                <div class="card-icon">⚡</div>
                <div class="card-title">Superposition</div>
                <div class="card-desc">
                    0 and 1 at the same time
                </div>
                <button class="btn btn2"
                    onclick="run('superposition')">
                    Run
                </button>
            </div>

            <div class="card">
                <div class="card-icon">🌀</div>
                <div class="card-title">Teleportation</div>
                <div class="card-desc">
                    Quantum state transfer
                </div>
                <button class="btn btn3"
                    onclick="run('teleportation')">
                    Run
                </button>
            </div>

             <div class="card">
                <div class="card-icon">〰️</div>
                <div class="card-title">Interference</div>
                <div class="card-desc">
                    Quantum waves combining
                </div>
                <button class="btn btn1"
                    onclick="run('interference')">
                    Run
                </button>
            </div>

            <div class="card">
                <div class="card-icon">🔍</div>
                <div class="card-title">Grover's Search</div>
                <div class="card-desc">
                    Quantum search algorithm
                </div>
                <button class="btn btn2"
                    onclick="run('grover')">
                    Run
                </button>
            </div>

            <div class="card">
                <div class="card-icon">📊</div>
                <div class="card-title">Fourier Transform</div>
                <div class="card-desc">
                    Quantum signal processing
                </div>
                <button class="btn btn3"
                    onclick="run('fourier')">
                    Run
                </button>
            </div>                                          
        </div>

        <div class="result-box" id="result-box">
            <div class="result-title" id="result-title">
                Result
            </div>
            <div class="result-data" id="result-data">
            </div>
        </div>
    </div>

    <div class="footer">
        Built with ❤️ using Python + Qiskit |
        Quantum Computing for Everyone
    </div>

   <script>
    function run(type) {
        var box = document.getElementById('result-box');
        var data = document.getElementById('result-data');
        var title = document.getElementById('result-title');
        box.style.display = 'block';
        data.innerHTML = '⏳ Running quantum simulation...';
        title.innerHTML = type.toUpperCase();
        fetch('/run/' + type)
            .then(r => r.json())
            .then(res => {
                let counts = res.counts;
                let sorted = Object.entries(counts)
                    .sort((a,b) => b[1]-a[1]);
                let max = sorted[0][1];
                let html = '✅ Results:<br><br>';
                for(let [state, count] of sorted) {
                    let pct = Math.round(count/max*100);
                    html += `
                    <div style="margin:10px 20px;
                    display:flex;align-items:center;gap:10px">
                       <span style="color:#fff;
                       font-size:14px;width:30px;
                       text-align:right">${state}</span>
                       <div style="background:#00ffff;
                       height:20px;width:${pct}%;
                       border-radius:5px;min-width:5px"></div>
                       <span style="color:#888;
                       font-size:14px">${count}</span>
                </div>`;
                }
                data.innerHTML = html;
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

@app.route('/run/interference')
def interference():
    qc = QuantumCircuit(1)
    qc.h(0)
    qc.h(0)
    counts = run_circuit(qc)
    return json.dumps({'counts': counts})

@app.route('/run/grover')
def grover():
    qc = QuantumCircuit(2)
    qc.h([0,1])
    qc.cz(0,1)
    qc.h([0,1])
    counts = run_circuit(qc)
    return json.dumps({'counts': counts})

@app.route('/run/fourier')
def fourier():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cp(3.14159/2, 0, 1)
    qc.h(1)
    counts = run_circuit(qc)
    return json.dumps({'counts': counts})
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
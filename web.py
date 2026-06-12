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
           background: #020818;
            color: white;
            font-family: Arial;
            min-height: 100vh;
        }
        .header {
            background: linear-gradient(135deg, #050d1f, #1a1a4e);
            padding: 40px;
            text-align: center;
            border-bottom: 2px solid #4d9fff;
        }
        .title {
            font-size: 48px;
            font-weight: bold;
            color: #4d9fff;
            text-shadow: 0 0 20px #4d9fff;
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
            border: 1px solid #1a3a6e;
            cursor: pointer;
            transition: all 0.3s;
        }
        .card:hover {
            transform: translateY(-5px);
            border-color: #4d9fff;
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
            color: #4d9fff;
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
            border: 1px solid #4d9fff;
            border-radius: 15px;
            padding: 25px;
            text-align: center;
            display: none;
        }
        .result-title {
            color: #4d9fff;
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
    .qubit {
    width: 60px;
    height: 60px;
    border-radius: 50%;
    border: 3px solid #4d9fff;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    font-size: 20px;
    margin: 10px;
    transition: all 0.5s;
}
.qubit.zero { background: #003333; color: #4d9fff; }
.qubit.one { background: #330033; color: #ff00ff; }
.qubit.super { 
    background: linear-gradient(#003333, #330033);
    animation: spin 1s infinite;
}
@keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
}
.step-box {
    background: #0a0a2e;
    border: 1px solid #4d9fff;
    border-radius: 10px;
    padding: 15px;
    margin: 10px 0;
    text-align: left;
}
.step-title {
    color: #4d9fff;
    font-size: 16px;
    margin-bottom: 8px;
}
.step-desc {
    color: #aaa;
    font-size: 14px;
    line-height: 1.6;
}
.highlight {
    color: #4d9fff;
    font-weight: bold;
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
        <div style="max-width:900px;margin:40px auto;
padding:20px;background:#0a0a2e;
border-radius:15px;border:1px solid #1a3a6e">
    <h2 style="color:#4d9fff;text-align:center;
    margin-bottom:20px">⚛️ About Quantum OS</h2>

    <h3 style="color:#4d9fff;margin:20px 0 10px;text-align:left">
    👨‍🔬 Builder
    </h3>
    <p style="color:#aaa;line-height:1.8;text-align:left">
    <b style="color:white">S. Praveen</b><br>
    M.Sc Physics — (MK University) <br>
    Melur, Madurai.<br>
    sapraveen81900@gmail.com <br>                            

    <h3 style="color:#4d9fff;margin:20px 0 10px">
    💡 Why I Built This
    </h3>
    <p style="color:#aaa;line-height:1.8">
    Quantum Computers are extremely expensive — 
    only the world's biggest companies like IBM, 
    Google, and Microsoft can afford them. 
    Small startups and small companies cannot 
    access quantum computing power.<br><br>
    So I decided to build Quantum Models based 
    on quantum computing basics that can run 
    on normal computers — making quantum 
    computing accessible to everyone!
    </p>

    <h3 style="color:#4d9fff;margin:20px 0 10px">
    🎯 Vision
    </h3>
    <p style="color:#aaa;line-height:1.8">
    To make Quantum Computing affordable and 
    accessible — not just for tech giants, 
    but for every small startup, student, 
    and researcher in the world.<br><br>
    To build a world-scale quantum technology 
    company that employs thousands of 
    Physics graduates from India and creates 
    products used by everyone on Earth.
    </p>

    <h3 style="color:#4d9fff;margin:20px 0 10px">
    🚀 Roadmap
    </h3>
    <p style="color:#aaa;line-height:1.8">
    V1 → Basic Quantum Simulations ✅<br>
    V2 → Advanced Algorithms + Better UI ⏳<br>
    V3 → Mobile App 📱<br>
    V4 → AI + Quantum Combined 🤖<br>
    V5 → World Scale 🌍
    </p>

    <div style="text-align:center;margin-top:25px">
        <a href="https://github.com/pravakutty/Quantum-OS"
        style="color:#4d9fff;text-decoration:none;
        border:1px solid #4d9fff;padding:10px 25px;
        border-radius:25px">
        ⭐ GitHub
        </a>
    </div>
</div>                          
        Built with ❤️ using Python + Qiskit |
        Quantum Computing for Everyone
    </div>

   <script>
    function run(type) {
    var box = document.getElementById('result-box');
    var data = document.getElementById('result-data');
    var title = document.getElementById('result-title');
    box.style.display = 'block';
    title.innerHTML = type.toUpperCase();
    
    // Step by step explanation
    var steps = {
        'entanglement': [
            {title: '⚛️ Step 1: 2 Qubits Create பண்ணோம்',
             desc: 'இரண்டு qubits உருவாக்கினோம். இப்போ இரண்டும் |0⟩ state-ல இருக்கு.',
             visual: '<div class="qubit zero">0</div><div class="qubit zero">0</div>'},
            {title: '🔀 Step 2: Hadamard Gate Apply பண்ணோம்',
             desc: 'First qubit-ஐ superposition-ல போட்டோம். இப்போ 0 and 1 same time!',
             visual: '<div class="qubit super">?</div><div class="qubit zero">0</div>'},
            {title: '🔗 Step 3: CNOT Gate — Entanglement!',
             desc: 'இரண்டு qubits-ஐ entangle பண்ணோம். ஒண்ணு மாறினா இன்னொண்ணும் மாறும்!',
             visual: '<div class="qubit super">?</div>🔗<div class="qubit super">?</div>'},
            {title: '📊 Step 4: Measurement',
             desc: 'Measure பண்ணும்போது 00 or 11 மட்டும் வரும் — 01 or 10 வராது! இதுதான் Entanglement!',
             visual: '<div class="qubit zero">0</div>🔗<div class="qubit zero">0</div>'}
        ],
        'superposition': [
            {title: '⚛️ Step 1: 1 Qubit Create பண்ணோம்',
             desc: 'ஒரு qubit உருவாக்கினோம். இப்போ |0⟩ state-ல இருக்கு.',
             visual: '<div class="qubit zero">0</div>'},
            {title: '🌀 Step 2: Hadamard Gate Apply பண்ணோம்',
             desc: 'Qubit இப்போ 0 AND 1 same time! இதுதான் Superposition — coin spinning மாதிரி!',
             visual: '<div class="qubit super">?</div>'},
            {title: '📊 Step 3: Measurement பண்ணோம்',
             desc: 'Measure பண்ணும்போது மட்டும் 0 or 1 decide ஆகுது. Coin land ஆனா மாதிரி!',
             visual: '<div class="qubit one">1</div>'},
            {title: '✅ Real World Use',
             desc: 'Quantum computers same time-ல multiple calculations பண்ணுது — இதனால Classical computer-ஐ விட exponentially fast!',
             visual: '⚡ Quantum Speed!'}
        ],
        'teleportation': [
            {title: '⚛️ Step 1: 3 Qubits Ready',
             desc: 'Alice-கிட்ட 2 qubits, Bob-கிட்ட 1 qubit இருக்கு.',
             visual: '<div class="qubit zero">A1</div><div class="qubit zero">A2</div>🌐<div class="qubit zero">B</div>'},
            {title: '🔗 Step 2: Entanglement Create பண்ணோம்',
             desc: 'Alice-ஓட qubit-ஐ Bob-ஓட qubit-உடன் entangle பண்ணினோம்!',
             visual: '<div class="qubit super">A1</div>🔗<div class="qubit super">B</div>'},
            {title: '📡 Step 3: Information Teleport!',
             desc: 'Alice measure பண்ணும்போது — Bob-ஓட qubit instant-ஆ correct state-ல போகுது! Physics-ஐ travel பண்ணாம!',
             visual: '✨ Teleported!'},
            {title: '✅ Real World Use',
             desc: 'Quantum internet-ல unhackable communication-க்கு use ஆகுது!',
             visual: '🔐 Quantum Security!'}
        ],
        'interference': [
            {title: '⚛️ Step 1: Qubit Superposition-ல',
             desc: 'Qubit 0 and 1 same time-ல இருக்கு.',
             visual: '<div class="qubit super">?</div>'},
            {title: '🌊 Step 2: Hadamard Again Apply பண்ணோம்',
             desc: 'Wave-மாதிரி paths interfere ஆகுது. Wrong answers cancel ஆகுது, Right answer amplify ஆகுது!',
             visual: '〰️ Wave Interference'},
            {title: '✅ Result',
             desc: '|0⟩ மட்டும் வருது — 100%! Interference wrong paths-ஐ eliminate பண்ணுது.',
             visual: '<div class="qubit zero">0</div> = 1000/1000'}
        ],
        'grover': [
            {title: '🔍 Step 1: Search Problem',
             desc: '4 items-ல ஒண்ணை find பண்ணணும். Classical = 4 steps. Quantum = 2 steps!',
             visual: '📦📦📦📦'},
            {title: '⚛️ Step 2: Superposition',
             desc: 'எல்லா possibilities-ம் same time-ல check பண்ணுது!',
             visual: '<div class="qubit super">?</div><div class="qubit super">?</div>'},
            {title: '🎯 Step 3: Oracle + Amplification',
             desc: 'Correct answer-ஐ amplify பண்ணுது, wrong answers-ஐ reduce பண்ணுது!',
             visual: '📦📦📦✅'},
            {title: '✅ Real World Use',
             desc: 'Database search, password cracking prevention, optimization problems-க்கு use ஆகுது!',
             visual: '🚀 Quadratic Speedup!'}
        ],
        'fourier': [
            {title: '📊 Step 1: Signal Input',
             desc: 'Quantum signal input கொடுக்கிறோம்.',
             visual: '〰️〰️〰️'},
            {title: '⚛️ Step 2: Quantum Transform',
             desc: 'Classical Fourier Transform-ஐ விட exponentially fast-ஆ calculate பண்ணுது!',
             visual: '<div class="qubit super">?</div><div class="qubit super">?</div>'},
            {title: '✅ Real World Use',
             desc: 'Cryptography, signal processing, chemistry simulations-க்கு use ஆகுது!',
             visual: '🔐 Cryptography Power!'}
        ]
    };

    var experimentSteps = steps[type];
    var currentStep = 0;
    
    function showStep(i) {
        if(i >= experimentSteps.length) {
            // Run actual quantum simulation
            data.innerHTML += '<br><div class="step-box"><div class="step-title">⚛️ Running Real Quantum Simulation...</div></div>';
            fetch('/run/' + type)
                .then(r => r.json())
                .then(res => {
                    let counts = res.counts;
                    let sorted = Object.entries(counts)
                        .sort((a,b) => b[1]-a[1]);
                    let max = sorted[0][1];
                    let html = '<div class="step-box"><div class="step-title">📊 Quantum Results:</div>';
                    for(let [state, count] of sorted) {
                        let pct = Math.round(count/max*100);
                        html += `
                        <div style="margin:8px 0;
                        display:flex;align-items:center;gap:10px">
                            <span style="color:#fff;
                            width:40px">${state}</span>
                            <div style="background:#4d9fff;
                            height:20px;width:${pct}%;
                            border-radius:5px;
                            min-width:5px"></div>
                            <span style="color:#888">
                            ${count}</span>
                        </div>`;
                    }
                    html += '</div>';
                    data.innerHTML += html;
                });
            return;
        }
        
        var step = experimentSteps[i];
        var stepHtml = `
        <div class="step-box" id="step-${i}">
            <div class="step-title">${step.title}</div>
            <div class="step-desc">${step.desc}</div>
            <div style="text-align:center;
            font-size:30px;margin:10px 0">
                ${step.visual}
            </div>
        </div>`;
        
        if(i === 0) data.innerHTML = stepHtml;
        else data.innerHTML += stepHtml;
        
        setTimeout(() => showStep(i+1), 1500);
    }
    
    showStep(0);
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
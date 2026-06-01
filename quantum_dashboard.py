from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

simulator = AerSimulator()

def run_circuit(qc, shots=1000):
    qc.measure_all()
    result = simulator.run(qc, shots=shots).result()
    return result.get_counts()

# 1. Entanglement
qc1 = QuantumCircuit(2)
qc1.h(0)
qc1.cx(0, 1)
counts1 = run_circuit(qc1)

# 2. Superposition
qc2 = QuantumCircuit(1)
qc2.h(0)
counts2 = run_circuit(qc2)

# 3. Teleportation
qc3 = QuantumCircuit(3)
qc3.h(0)
qc3.cx(0, 1)
qc3.cx(1, 2)
counts3 = run_circuit(qc3)

# Dashboard
fig, axes = plt.subplots(1, 3, figsize=(15, 5))
fig.suptitle('Quantum Computing Dashboard', 
             fontsize=16, fontweight='bold')

axes[0].bar(counts1.keys(), counts1.values(), color='blue')
axes[0].set_title('Entanglement')
axes[0].set_xlabel('States')
axes[0].set_ylabel('Count')

axes[1].bar(counts2.keys(), counts2.values(), color='red')
axes[1].set_title('Superposition')
axes[1].set_xlabel('States')
axes[1].set_ylabel('Count')

axes[2].bar(counts3.keys(), counts3.values(), color='purple')
axes[2].set_title('Teleportation')
axes[2].set_xlabel('States')
axes[2].set_ylabel('Count')

plt.tight_layout()
plt.show()
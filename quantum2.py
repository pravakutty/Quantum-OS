from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

# Superposition circuit
qc = QuantumCircuit(1)
qc.h(0)
qc.measure_all()

# Simulate
simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()
counts = result.get_counts()

# Graph
plt.figure(figsize=(8, 6))
plt.bar(counts.keys(), counts.values(), color=['blue', 'red'])
plt.xlabel('Qubit State')
plt.ylabel('Count')
plt.title('Quantum Superposition - 0 and 1 Same Time!')
plt.show()
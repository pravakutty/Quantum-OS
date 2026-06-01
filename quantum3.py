# quantum3.py - Quantum Teleportation
from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt

qc = QuantumCircuit(3, 3)

# Qubit prepare
qc.h(0)
qc.cx(0, 1)
qc.cx(1, 2)
qc.measure([0,1,2], [0,1,2])

simulator = AerSimulator()
result = simulator.run(qc, shots=1000).result()
counts = result.get_counts()

plt.bar(counts.keys(), counts.values(), color='purple')
plt.title('Quantum Teleportation!')
plt.xlabel('States')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
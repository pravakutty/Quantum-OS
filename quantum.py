from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator

# 2 Qubits create பண்ணு
qc = QuantumCircuit(2)

# Superposition
qc.h(0)

# Entanglement
qc.cx(0, 1)

# Measure
qc.measure_all()

# Simulate
simulator = AerSimulator()
result = simulator.run(qc).result()
counts = result.get_counts()

print("Quantum Result:", counts)
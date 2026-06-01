from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
import matplotlib.pyplot as plt
import tkinter as tk

simulator = AerSimulator()

def run_circuit(qc):
    qc.measure_all()
    result = simulator.run(qc, shots=1000).result()
    return result.get_counts()

def show_entanglement():
    qc = QuantumCircuit(2)
    qc.h(0)
    qc.cx(0, 1)
    counts = run_circuit(qc)
    plt.figure(figsize=(6,4))
    plt.bar(list(counts.keys()), list(counts.values()), color='blue')
    plt.title('Quantum Entanglement')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.show()

def show_superposition():
    qc = QuantumCircuit(2)
    qc.h(0)
    counts = run_circuit(qc)
    plt.figure(figsize=(6,4))
    plt.bar(list(counts.keys()), list(counts.values()), color='red')
    plt.title('Quantum Superposition')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.show()

def show_teleportation():
    qc = QuantumCircuit(3)
    qc.h(0)
    qc.cx(0, 1)
    qc.cx(1, 2)
    qc.h(0)
    counts = run_circuit(qc)
    plt.figure(figsize=(6,4))
    plt.bar(list(counts.keys()), list(counts.values()), color='purple')
    plt.title('Quantum Teleportation')
    plt.xlabel('State')
    plt.ylabel('Count')
    plt.show()

#UI Window
window = tk.Tk()
window.title("Quantum OS")
window.geometry("400x300")
window.configure(bg='black')

#Title
title = tk.Label(window, text="Welcome to Quantum OS", font=("Arial", 24, "bold"), fg="white", bg="black")
title.pack(pady=20)


#buttons
btn1 = tk.Button(window, text="Entanglement", font=("Arial", 14), bg="blue", fg="white", width=20, command=show_entanglement)
btn1.pack(pady=10)

btn2 = tk.Button(window, text="Superposition", font=("Arial", 14), bg="red", fg="white", width=20, command=show_superposition)
btn2.pack(pady=10)

btn3 = tk.Button(window, text="Teleportation", font=("Arial", 14), bg="purple", fg="white", width=20, command=show_teleportation)
btn3.pack(pady=10)

window.mainloop()
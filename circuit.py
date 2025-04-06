from typing import List
from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
from numpy import pi
from qiskit.circuit.library import C3XGate
#from Algo import *


class QAlgo:
    def __init__(s):
        pass
    
    def Regi(s):
        global qreg_q, creg_c
        qreg_q = QuantumRegister(5, 'q')
        creg_c = ClassicalRegister(2, 'c')
        return qreg_q, creg_c

    def Reset(s):
        global circuit 
        circuit = QuantumCircuit(qreg_q, creg_c)    
        circuit.reset(qreg_q[0])
        circuit.reset(qreg_q[1])
        circuit.reset(qreg_q[2])
        circuit.reset(qreg_q[3])
        circuit.reset(qreg_q[4])
        circuit.x(qreg_q[2])
    
    def XG(s, L : list ):
        if L[0] == 1: #cardinal node is green
            circuit.x(qreg_q[0])
        if (L[0] + L[1] == 2): #Alert Node, if all states are high then
            circuit.x(qreg_q[4])
            
    def CG(s, L : "list"):
        if L[0] !=0 and L[1] !=0:
            circuit.u(2 * pi, 2 * pi, 2 * pi, qreg_q[1])
            circuit.u(pi, 2 * pi, pi, qreg_q[3])
        elif L[0][0] !=0:
            circuit.u(2 * pi, 2 * pi, 2 * pi, qreg_q[1])
        elif L[0][1] !=0:
            circuit.u(pi, 2 * pi, pi, qreg_q[3])
        else:
            pass
        
    
    def C3xg(s):
        circuit.append(C3XGate(), [qreg_q[0], qreg_q[1], qreg_q[3], qreg_q[2]])
        return circuit
        
    def Measure(s): 
        circuit.measure([2, 0], [1, 1])
        simulator = Aer.get_backend('qasm_simulator')
        result = execute(circuit , backend = simulator).result()
        global bit_result
        bit_result=dict(result.get_counts(circuit))
        print(bit_result)
        q = round((list(bit_result.values())[0])/1024)
        print(q)
        
def CKT(M : "List"):
    Q = QAlgo()
    Q.Regi()
    Q.Reset()
    Q.XG(M)
    Q.CG(M)
    Q.C3xg()
    Q.Measure()
    for i in range(1):
        if list(bit_result)[0] == '00':
            print("Red light")
        elif list(bit_result)[0] == '01':
            print("yellow light")
        elif list(bit_result)[0] == '10':
            print("Green light")
        elif list(bit_result)[0] == '11':
            print("Green light")
        else:
            pass
        
    print("End")

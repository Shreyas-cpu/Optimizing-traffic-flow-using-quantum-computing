// Quantum Gate Types and their configurations
const QUANTUM_GATES = {
    RESET: { symbol: 'R', color: '#e74c3c' },
    X: { symbol: 'X', color: '#3498db' },
    U: { symbol: 'U', color: '#2ecc71' },
    C3X: { symbol: 'C3X', color: '#9b59b6' }
};

// Traffic Light States
const TRAFFIC_STATES = {
    RED: '00',
    RED_YELLOW: '01',
    YELLOW: '10',
    GREEN: '11'
};

class QuantumCircuitVisualizer {
    constructor() {
        this.gatesContainer = document.getElementById('gates-animation');
        this.currentStep = 0;
        this.isAnimating = false;
    }

    clearGates() {
        this.gatesContainer.innerHTML = '';
    }

    createGate(type, qubitIndex, position) {
        const gate = document.createElement('div');
        gate.className = 'quantum-gate';
        gate.style.left = `${position}px`;
        gate.style.top = `${20 + qubitIndex * 30}px`;
        gate.style.backgroundColor = QUANTUM_GATES[type].color;
        gate.textContent = QUANTUM_GATES[type].symbol;
        return gate;
    }

    createControlLine(startQubit, endQubit, position) {
        const line = document.createElement('div');
        line.className = 'connection-line';
        const top = Math.min(startQubit, endQubit) * 30 + 20;
        const height = Math.abs(endQubit - startQubit) * 30;
        line.style.left = `${position + 20}px`;
        line.style.top = `${top}px`;
        line.style.height = `${height}px`;
        return line;
    }

    async animateCircuit() {
        if (this.isAnimating) return;
        this.isAnimating = true;
        this.clearGates();

        const updateStatus = (message) => {
            document.getElementById('status-text').textContent = message;
        };

        // Initialize qubits
        updateStatus('Initializing quantum circuit...');
        for (let i = 0; i < 5; i++) {
            await this.addGateWithDelay('RESET', i, 100);
        }
        await new Promise(resolve => setTimeout(resolve, 500));

        // Traffic state encoding
        updateStatus('Encoding traffic state...');
        await this.addGateWithDelay('X', 2, 200); // Base traffic state
        
        // Vehicle density gates
        updateStatus('Processing vehicle density...');
        const vehicleDensity = Math.random();
        if (vehicleDensity > 0.5) {
            await this.addGateWithDelay('X', 0, 300);
            updateStatus('High vehicle density detected...');
        }

        // Pedestrian density gates
        updateStatus('Processing pedestrian data...');
        const pedestrianDensity = Math.random();
        if (pedestrianDensity > 0.5) {
            await this.addGateWithDelay('X', 4, 300);
            updateStatus('High pedestrian activity detected...');
        }

        // Quantum superposition
        updateStatus('Applying quantum superposition...');
        await this.addGateWithDelay('U', 1, 400);
        await this.addGateWithDelay('U', 3, 400);

        // Final optimization
        updateStatus('Optimizing traffic signal timing...');
        const c3xGate = this.createGate('C3X', 2, 500);
        const controlLine1 = this.createControlLine(0, 2, 500);
        const controlLine2 = this.createControlLine(1, 2, 500);
        const controlLine3 = this.createControlLine(3, 2, 500);
        
        this.gatesContainer.appendChild(c3xGate);
        this.gatesContainer.appendChild(controlLine1);
        this.gatesContainer.appendChild(controlLine2);
        this.gatesContainer.appendChild(controlLine3);

        await new Promise(resolve => setTimeout(resolve, 1000));
        updateStatus('Quantum optimization complete');
        this.isAnimating = false;
    }

    createGate(type, qubitIndex, position) {
        const gate = document.createElement('div');
        gate.className = 'quantum-gate';
        gate.style.left = `${position}px`;
        gate.style.top = `${20 + qubitIndex * 30}px`;
        gate.style.backgroundColor = QUANTUM_GATES[type].color;
        gate.textContent = QUANTUM_GATES[type].symbol;
        
        // Add tooltip with gate description
        const descriptions = {
            'RESET': 'Initializes qubit to |0⟩ state',
            'X': 'NOT gate - Flips qubit state',
            'U': 'Rotation gate - Creates superposition',
            'C3X': 'Toffoli gate - 3-control NOT operation'
        };
        
        gate.title = descriptions[type];
        return gate;
    }

    async addGateWithDelay(type, qubitIndex, position) {
        const gate = this.createGate(type, qubitIndex, position);
        this.gatesContainer.appendChild(gate);
        await new Promise(resolve => setTimeout(resolve, 200));
    }
}

class TrafficSimulation {
    constructor() {
        this.circuitVisualizer = new QuantumCircuitVisualizer();
        this.isRunning = false;
        this.setupEventListeners();
    }

    setupEventListeners() {
        // Video upload handlers
        document.querySelectorAll('.video-preview').forEach(preview => {
            preview.addEventListener('click', () => {
                const input = preview.parentElement.querySelector('.video-input');
                input.click();
            });
        });

        document.querySelectorAll('.video-input').forEach(input => {
            input.addEventListener('change', (e) => {
                const file = e.target.files[0];
                if (file) {
                    const preview = input.parentElement.querySelector('.video-preview');
                    preview.innerHTML = `<div class="upload-icon">✓</div><p>${file.name}</p>`;
                }
            });
        });

        // Simulation control handlers
        document.getElementById('start-sim').addEventListener('click', () => this.startSimulation());
        document.getElementById('stop-sim').addEventListener('click', () => this.stopSimulation());
    }

    validateInputs() {
        const xCoord = document.getElementById('x-coord').value;
        const yCoord = document.getElementById('y-coord').value;
        const nodes = document.getElementById('nodes').value.trim();
        
        if (!xCoord || !yCoord) {
            alert('Please enter both X and Y coordinates');
            return false;
        }

        if (!nodes) {
            alert('Please enter connected nodes');
            return false;
        }

        const videos = document.querySelectorAll('.video-input');
        let allVideosUploaded = true;
        videos.forEach(video => {
            if (!video.files || video.files.length === 0) {
                allVideosUploaded = false;
            }
        });

        if (!allVideosUploaded) {
            alert('Please upload all required videos');
            return false;
        }

        return true;
    }

    updateTrafficLights(state) {
        const directions = ['north', 'south', 'east', 'west'];
        directions.forEach(direction => {
            const lights = document.querySelector(`.traffic-light.${direction} .light-container`).children;
            // Reset all lights
            Array.from(lights).forEach(light => light.classList.remove('active'));
            
            // Set active light based on state
            switch(state) {
                case TRAFFIC_STATES.RED:
                    lights[0].classList.add('active'); // Red
                    break;
                case TRAFFIC_STATES.RED_YELLOW:
                    lights[0].classList.add('active'); // Red
                    lights[1].classList.add('active'); // Yellow
                    break;
                case TRAFFIC_STATES.YELLOW:
                    lights[1].classList.add('active'); // Yellow
                    break;
                case TRAFFIC_STATES.GREEN:
                    lights[2].classList.add('active'); // Green
                    break;
            }
        });
    }

    async startSimulation() {
        if (!this.validateInputs()) return;
        
        this.isRunning = true;
        document.getElementById('start-sim').disabled = true;
        document.getElementById('stop-sim').disabled = false;
        document.getElementById('status-text').textContent = 'Simulation running...';

        while (this.isRunning) {
            // Animate quantum circuit
            await this.circuitVisualizer.animateCircuit();

            // Randomly change traffic light states for demonstration
            const states = Object.values(TRAFFIC_STATES);
            const randomState = states[Math.floor(Math.random() * states.length)];
            this.updateTrafficLights(randomState);

            await new Promise(resolve => setTimeout(resolve, 3000));
        }
    }

    stopSimulation() {
        this.isRunning = false;
        document.getElementById('start-sim').disabled = false;
        document.getElementById('stop-sim').disabled = true;
        document.getElementById('status-text').textContent = 'Simulation stopped';
    }
}

// Initialize the simulation when the page loads
document.addEventListener('DOMContentLoaded', () => {
    new TrafficSimulation();
});

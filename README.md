# QuantumPlators - Quantum Traffic Management System

A next-generation traffic management system that combines quantum computing with computer vision to optimize traffic flow at intersections.

## Features

- Real-time traffic detection for:
  * Pedestrians
  * Two-wheelers
  * Cars
- Quantum circuit optimization using Qiskit
- Interactive web interface
- Multi-node intersection management

## Project Structure

```
QuantumPlators/
├── Algo.py              # Traffic state algorithm
├── circuit.py           # Quantum circuit implementation
├── FramesML.py          # Video processing and ML detection
├── Main.py              # Main program entry point
├── gui.py              # Desktop GUI implementation
├── index.html          # Web interface
├── styles.css          # Web interface styling
├── script.js           # Web interface functionality
└── sample_videos/      # Traffic sample video generator
    ├── generate_videos.html
    └── README.md
```

## Requirements

- Python 3.8+
- Qiskit
- OpenCV
- NumPy
- PIL (Python Imaging Library)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/QuantumPlators/QuantumPlators.git
cd QuantumPlators
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Desktop Application

Run the main program:
```bash
python Main.py
```

### Web Interface

1. Open `index.html` in a web browser
2. Upload traffic videos
3. Enter intersection coordinates
4. Start the simulation

### Sample Videos

1. Navigate to `sample_videos/`
2. Open `generate_videos.html` in a browser
3. Generate sample videos for testing

## How It Works

1. **Traffic Detection**
   - Uses computer vision to detect and count vehicles and pedestrians
   - Processes video feeds in real-time
   - Calculates traffic density for each direction

2. **Quantum Processing**
   - Encodes traffic states into quantum bits
   - Uses quantum gates for optimization
   - Implements error correction
   - Returns optimized traffic signal timing

3. **Signal Management**
   - Coordinates multiple intersection nodes
   - Optimizes traffic flow across the network
   - Handles special cases and emergency vehicles

## Quantum Circuit

The system uses a 5-qubit quantum circuit:
- q[0]: Vehicle density
- q[1]: Timing control
- q[2]: State management
- q[3]: Phase control
- q[4]: Pedestrian density

Gates used:
- Reset gates for initialization
- X gates for state flipping
- U gates for rotation
- C3X (Toffoli) gate for optimization

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Qiskit team for quantum computing framework
- OpenCV community for computer vision tools
- Contributors and testers

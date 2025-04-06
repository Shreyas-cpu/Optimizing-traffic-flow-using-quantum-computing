try:
    import tkinter as tk
    from tkinter import ttk, filedialog, messagebox
    import os
    from PIL import Image, ImageTk
    import cv2
    import numpy as np
    from qiskit import QuantumRegister, ClassicalRegister, QuantumCircuit, Aer, execute
    from Algo import *
    from circuit import *
    from FramesML import *
except ImportError as e:
    print(f"Error: Missing required package - {str(e)}")
    print("Please install required packages using:")
    print("pip install pillow opencv-python numpy qiskit")
    exit(1)

class TrafficLightDisplay(ttk.Frame):
    def __init__(self, parent, direction):
        super().__init__(parent)
        self.direction = direction
        
        # Create canvas for traffic light
        self.canvas = tk.Canvas(self, width=60, height=150, bg='gray')
        self.canvas.pack(padx=5, pady=5)
        
        # Create traffic light circles
        self.red = self.canvas.create_oval(20, 20, 40, 40, fill='darkred')
        self.yellow = self.canvas.create_oval(20, 60, 40, 80, fill='darkgolden')
        self.green = self.canvas.create_oval(20, 100, 40, 120, fill='darkgreen')
        
        # Direction label
        ttk.Label(self, text=direction).pack()
    
    def update_state(self, state):
        # Reset all lights
        self.canvas.itemconfig(self.red, fill='darkred')
        self.canvas.itemconfig(self.yellow, fill='darkgolden')
        self.canvas.itemconfig(self.green, fill='darkgreen')
        
        # Set active light based on state
        if state == "00":  # Red
            self.canvas.itemconfig(self.red, fill='red')
        elif state == "01":  # Red-Yellow
            self.canvas.itemconfig(self.red, fill='red')
            self.canvas.itemconfig(self.yellow, fill='yellow')
        elif state == "10":  # Yellow
            self.canvas.itemconfig(self.yellow, fill='yellow')
        elif state == "11":  # Green
            self.canvas.itemconfig(self.green, fill='lime')

class VideoFrame(ttk.Frame):
    def __init__(self, parent, title):
        super().__init__(parent)
        self.title = title
        
        ttk.Label(self, text=title).pack()
        
        # Video display canvas
        self.canvas = tk.Canvas(self, width=320, height=240)
        self.canvas.pack(padx=5, pady=5)
        
        # File selection button
        ttk.Button(self, text="Select Video", command=self.select_video).pack()
        
        self.video_path = None
        
    def select_video(self):
        self.video_path = filedialog.askopenfilename(
            title=f"Select {self.title} Video",
            filetypes=[("Video files", "*.mp4 *.avi")]
        )
        if self.video_path:
            # Update display with first frame
            cap = cv2.VideoCapture(self.video_path)
            ret, frame = cap.read()
            if ret:
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame = cv2.resize(frame, (320, 240))
                photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
                self.canvas.create_image(0, 0, image=photo, anchor=tk.NW)
                self.canvas.image = photo
            cap.release()

class NodeInfoPanel(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        
        ttk.Label(self, text="Node Information").pack()
        
        # Coordinates
        coord_frame = ttk.Frame(self)
        coord_frame.pack(fill=tk.X, padx=5, pady=5)
        ttk.Label(coord_frame, text="X:").pack(side=tk.LEFT)
        self.x_coord = ttk.Entry(coord_frame, width=10)
        self.x_coord.pack(side=tk.LEFT, padx=5)
        ttk.Label(coord_frame, text="Y:").pack(side=tk.LEFT)
        self.y_coord = ttk.Entry(coord_frame, width=10)
        self.y_coord.pack(side=tk.LEFT, padx=5)
        
        # Connected nodes
        ttk.Label(self, text="Connected Nodes:").pack()
        self.nodes_text = tk.Text(self, height=4, width=30)
        self.nodes_text.pack(padx=5, pady=5)

class MainGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Quantum Traffic Management System")
        self.geometry("1200x800")
        
        # Instructions label
        instructions = """
        Instructions:
        1. Select video files for pedestrians, two-wheelers, and cars
        2. Enter node coordinates (X,Y)
        3. Enter connected node names (one per line)
        4. Click 'Start Simulation' to run the quantum traffic system
        """
        ttk.Label(self, text=instructions, justify=tk.LEFT).pack(pady=10)
        
        # Create main container
        main_container = ttk.Frame(self)
        main_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Video inputs frame
        video_frame = ttk.Frame(main_container)
        video_frame.pack(fill=tk.X, pady=10)
        
        # Create video input sections
        self.pedestrian_video = VideoFrame(video_frame, "Pedestrian Detection")
        self.pedestrian_video.pack(side=tk.LEFT, padx=5)
        
        self.two_wheeler_video = VideoFrame(video_frame, "Two Wheeler Detection")
        self.two_wheeler_video.pack(side=tk.LEFT, padx=5)
        
        self.car_video = VideoFrame(video_frame, "Car Detection")
        self.car_video.pack(side=tk.LEFT, padx=5)
        
        # Traffic lights frame
        traffic_frame = ttk.Frame(main_container)
        traffic_frame.pack(pady=20)
        
        # Create traffic lights
        self.lights = {}
        for direction in ['East', 'West', 'North', 'South']:
            self.lights[direction] = TrafficLightDisplay(traffic_frame, direction)
            self.lights[direction].pack(side=tk.LEFT, padx=20)
        
        # Node information
        self.node_info = NodeInfoPanel(main_container)
        self.node_info.pack(pady=20)
        
        # Control buttons
        control_frame = ttk.Frame(main_container)
        control_frame.pack(pady=20)
        
        ttk.Button(control_frame, text="Start Simulation", 
                   command=self.start_simulation).pack(side=tk.LEFT, padx=5)
        ttk.Button(control_frame, text="Stop Simulation", 
                   command=self.stop_simulation).pack(side=tk.LEFT, padx=5)
        
        self.running = False
    
    def validate_inputs(self):
        """Validate all required inputs before starting simulation"""
        if not all([self.pedestrian_video.video_path, 
                   self.two_wheeler_video.video_path, 
                   self.car_video.video_path]):
            tk.messagebox.showerror("Error", "Please select all video files")
            return False
            
        try:
            x = float(self.node_info.x_coord.get())
            y = float(self.node_info.y_coord.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Please enter valid coordinates")
            return False
            
        connected_nodes = self.node_info.nodes_text.get("1.0", tk.END).strip()
        if not connected_nodes:
            tk.messagebox.showerror("Error", "Please enter connected nodes")
            return False
            
        return True

    def process_frame(self, frame, detector_type):
        """Process a single frame with the appropriate detector"""
        if detector_type == "pedestrian":
            # Convert frame to grayscale for pedestrian detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cascade_path = os.path.join(os.getcwd(), 'pedestrians.xml')
            full_body = cv2.CascadeClassifier(cascade_path)
            bodies = full_body.detectMultiScale(gray, 1.2, 3)
            return len(bodies)
        elif detector_type == "two_wheeler":
            # Process for two-wheeler detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cascade_path = os.path.join(os.getcwd(), 'two_wheeler.xml')
            two_wheeler = cv2.CascadeClassifier(cascade_path)
            vehicles = two_wheeler.detectMultiScale(gray, 1.01, 1)
            return len(vehicles)
        elif detector_type == "car":
            # Process for car detection
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            cascade_path = os.path.join(os.getcwd(), 'cars.xml')
            car_cascade = cv2.CascadeClassifier(cascade_path)
            cars = car_cascade.detectMultiScale(gray, 1.1, 2)
            return len(cars)
        return 0

    def start_simulation(self):
        if not self.running:
            if not self.validate_inputs():
                return
                
            self.running = True
            try:
                # Initialize video captures
                ped_cap = cv2.VideoCapture(self.pedestrian_video.video_path)
                two_cap = cv2.VideoCapture(self.two_wheeler_video.video_path)
                car_cap = cv2.VideoCapture(self.car_video.video_path)
                
                # Process first frame of each video
                ret_ped, frame_ped = ped_cap.read()
                ret_two, frame_two = two_cap.read()
                ret_car, frame_car = car_cap.read()
                
                if all([ret_ped, ret_two, ret_car]):
                    # Count detections
                    ped_count = self.process_frame(frame_ped, "pedestrian")
                    two_count = self.process_frame(frame_two, "two_wheeler")
                    car_count = self.process_frame(frame_car, "car")
                    
                    # Create input list for algorithm
                    x = float(self.node_info.x_coord.get())
                    y = float(self.node_info.y_coord.get())
                    connected_nodes = self.node_info.nodes_text.get("1.0", tk.END).strip().split('\n')
                    
                    # Format data for ALGO
                    L = [
                        [[ped_count, two_count], [ped_count, two_count], 
                         [ped_count, two_count], [ped_count, car_count]], 
                        [x, y], 
                        connected_nodes
                    ]
                    
                    # Run quantum algorithm
                    M = ALGO(L)
                    W = CKT(M)
                    
                    # Update traffic lights based on quantum circuit result
                    directions = ['East', 'West', 'North', 'South']
                    for i, direction in enumerate(directions):
                        if i < len(W):
                            self.lights[direction].update_state(W[i])
                    
                    # Show detection counts
                    status_msg = f"Detected: {ped_count} pedestrians, {two_count} two-wheelers, {car_count} cars"
                    tk.messagebox.showinfo("Detection Results", status_msg)
                
                # Clean up
                ped_cap.release()
                two_cap.release()
                car_cap.release()
                
            except Exception as e:
                tk.messagebox.showerror("Error", f"An error occurred: {str(e)}")
                self.running = False
    
    def stop_simulation(self):
        self.running = False

if __name__ == "__main__":
    app = MainGUI()
    app.mainloop()

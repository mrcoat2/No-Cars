import socket
import pickle
import time

FPS = 60
FRAME_TIME = 1 / FPS

address = "localhost"
port = 4090

class Car:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        self.color = (255, 53, 52)
        self.width = width
        self.height = height
        self.speed = [0, 0] # [x_speed, y_speed]
        self.direction = 0 # Lets choose pi or radians at some point

        self.destination = None

this_car = Car(200, 200, 20, 30)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Connect to the server's address and port
    print("Connecting to server...")
    s.connect((address, port))
    send_data = [this_car.x, this_car.y, this_car.width, this_car.height]
    serialized_data = pickle.dumps(send_data)

    s.sendall(serialized_data)
    while True: # Main loop
        start = time.perf_counter()

        # Your loop code here
        this_car.y += 1 # Move the car down for testing

        data = s.recv(1024)
        print(f"Received data from server: {data}")
        if data == "audit":
            this_car_data = [this_car.x, this_car.y, this_car.speed]
            serialized_car_data = pickle.dumps(this_car_data)
            s.sendall(serialized_car_data)

        elapsed = time.perf_counter() - start
        sleep_time = FRAME_TIME - elapsed

        if sleep_time > 0:
            time.sleep(sleep_time)

class VacuumEnvironment:
    def __init__(self):
        # '0' for Clean, '1' for Dirty
        self.location_condition = {'A': '1', 'B': '1'}
        self.vacuum_location = 'A'  # Start at Room A

    def run_agent(self):
        print(f"Initial State: {self.location_condition} | Vacuum starting in Room {self.vacuum_location}\n")
        
        # Total rooms to clean
        for _ in range(2):
            current_room = self.vacuum_location
            status = self.location_condition[current_room]
            
            if status == '1': # If Dirty
                print(f"Room {current_room} is Dirty. Cleaning...")
                self.location_condition[current_room] = '0'
                print(f"Room {current_room} is now Clean.")
            else:
                print(f"Room {current_room} is already Clean.")
                
            # Move to the other room
            if current_room == 'A':
                print("Moving Right to Room B...")
                self.vacuum_location = 'B'
            else:
                print("Moving Left to Room A...")
                self.vacuum_location = 'A'
            print("-" * 30)
            
        print(f"Final Environment State: {self.location_condition}")

# Run simulation
env = VacuumEnvironment()
env.run_agent()

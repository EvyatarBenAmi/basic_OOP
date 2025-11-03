class Agent:
    def __init__(self, code_name: str, clearance_level: int):
        self.code_name = code_name
        self._clearance_level = clearance_level

    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}")

    def getter(self):
        print(self._clearance_level)

    def setter(self, new_level: int):
        self.mew_level = new_level
        if 1 < new_level < 10: 
            self._clearance_level = new_level 
        print(self._clearance_level)

class Mission:
    def __init__(self, mission_name: str, target_location: str, assigned_agent: Agent):
        self.mission_name = mission_name
        self.target_location = target_location
        self.assigned_agent = assigned_agent

    def brief(self):
        print(f"Mission: {self.mission_name}, Target: {self.target_location}, Agent: {self.assigned_agent.code_name}")


class FieldAgent(Agent):
    def __init__(self, code_name, clearance_level, region: str):
        super().__init__(code_name, clearance_level)
        self.region = region
    
    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}. Region: {self.region}")
      

class CyberAgent(Agent):
    def __init__(self, code_name, clearance_level, specialty):
        super().__init__(code_name, clearance_level)
        self.specialty = specialty
    
    def report(self):
        print(f"Agent {self.code_name} reporting. Clearance Level: {self._clearance_level}. specialty: {self.specialty}")


def func_create_report():
    pass
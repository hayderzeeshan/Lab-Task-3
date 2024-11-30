class ModelBasedAgent:
    def __init__(self, desired_temp):
        self. desired_temp = desired_temp
        self. current_temp = None
        self. previous_temps = []

    def percept(self, temp):
        self. current_temp = temp
        self. previous_temps. append(temp)

    def act(self):
        if self. current_temp > self. desired_temp:
            return "Turn off the heater"
        else:
            return "Turn on heater"

    def get_memory(self):
        return self. previous_temps

agent = ModelBasedAgent(32)

rooms = {
"Living Room": 28,
"Bedroom": 18,
"Kitchen": 32
}
for room, temp in rooms.items():
    agent.percept(temp)
    print(f"{room}: {temp} ==> {agent.act()}")

print("Agent temperatures", agent.get_memory())
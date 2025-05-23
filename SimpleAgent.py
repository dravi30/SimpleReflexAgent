import matplotlib.pyplot as plt
import matplotlib.patches as patches
import time

# 2x2 environment
environment = {
    "Room1": "Clean",
    "Room2": "Dirty",
    "Room3": "Clean",
    "Room4": "Dirty"
}

room_positions = {
    "Room1": (0, 1),  # Top-left
    "Room2": (1, 1),  # Top-right
    "Room3": (0, 0),  # Bottom-left
    "Room4": (1, 0)   # Bottom-right
}

rooms = list(environment.keys())  
agent_index = 0  


def reflex_agent(state):
    if state == "Dirty":
        return "Clean"
    else:
        return "Move"
        
        
def draw_environment(env, agent_pos, step):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 2) 
    ax.set_ylim(0, 2) 
    ax.set_xticks([])
    ax.set_yticks([]) 
    ax.set_title(f"Step {step} — Agent in {rooms[agent_pos]}")

    for room, pos in room_positions.items():  
        x, y = pos
        color = 'red' if env[room] == "Dirty" else 'green'  
        rect = patches.Rectangle((x, y), 1, 1, facecolor=color, edgecolor='black') 
        ax.add_patch(rect)
        ax.text(x + 0.5, y + 0.5, room, ha='center', va='center', color='white', fontsize=10)

    
    agent_x, agent_y = room_positions[rooms[agent_pos]]
    agent_patch = patches.Circle((agent_x + 0.5, agent_y + 0.5), 0.1, color='blue')
    ax.add_patch(agent_patch)

    plt.pause(1) 
    plt.close() 
     
     
plt.ion()  
steps = 8  


for step in range(steps):
    current_room = rooms[agent_index] 
    state = environment[current_room] 
    action = reflex_agent(state) 

    draw_environment(environment, agent_index, step + 1) 

    if action == "Clean":
        environment[current_room] = "Clean"
    else:
        agent_index = (agent_index + 1) % len(rooms) 


plt.ioff() 
print("Simulation complete!") 
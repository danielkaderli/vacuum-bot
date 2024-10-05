import random

class Environment:
  #make environment
  def __init__(self, size):
    #initialize self
    self.size = size
    self.locations = ['dirty' for i in range(size)]
    self.agent_pos = random.randint(0, size-1)
    
  def clean(self):
    #clean environment
    self.locations[self.agent_pos] = 'clean'
    print('cleaned')

  def add_dirt(self, position):
    #add dirt to environment
    if position < self.size:
      self.locations[position] = 'dirty'

  def move_agent(self, direction, speed):
    spaces = random.randint(0, speed)
    if direction == 'left' and self.agent_pos > 0 + spaces:
      self.agent_pos -= spaces
    elif direction == 'right' and self.agent_pos < self.size - spaces - 1:
      self.agent_pos += spaces
  
  def get_state(self, position):
    #get state of environment
    return self.locations[position]

class Agent:
  #make agent
  def __init__(self, environment, speed):
    self.environment = environment
    self.speed = speed
    self.performance = 0.5
    self.prev_state = 'none'

  def calculatePerf(self):
    # for x in range(self.environment.size):
    #   if self.environment.get_state(x) == 'dirty':
    #     self.performance -= 1

    if self.prev_state == 'clean' and self.sense() == 'clean':
      self.performance *= 0.99
    if self.sense() == 'dirty':
      self.performance *= 1.01
    return self.performance
  
  def sense(self):
    return self.environment.get_state(self.environment.agent_pos)

  def act(self):
    if self.sense() == 'dirty':
      self.clean()
    else:
      self.move()

  def clean(self):
    self.environment.clean()
    # self.performance += 1

  def move(self):
    direction = random.choice(['left', 'right'])
    self.prev_state = self.sense()
    self.environment.move_agent(direction, self.speed)
    # self.performance -= 1

def simulate(num_steps, env_size, speed):
  env = Environment(env_size)
  vacuum = Agent(env, speed)

  for i in range(num_steps):
    print('step ', i)
    print('performance: ', vacuum.calculatePerf())
    vacuum.act()
    for i, cell in enumerate(env.locations):
      state = "\033[33m#\033[0m" if cell == 'dirty' else " "
      # agent_marker = "\033[35m*\033[0m" if i == env.agent_pos else ""
      if(i == env.agent_pos):
        print(f"\033[35m[\033[0m{state}\033[35m]\033[0m", end="")
      else:
        print(f"[{state}]", end="")
        

    

  return vacuum.performance
  

# Run the simulation
performance = simulate(100, env_size=100, speed=4)
print(f"Agent performance after 100 steps: {performance}")


  
  

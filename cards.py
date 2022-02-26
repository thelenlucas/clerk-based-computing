#This class imitates a standard file card, for ease of use in the analogy.
#It can hold one number
#These number
#For simplicities sake these values are all floats
class card(object):
    def __init__(self, v):
        self.value = v

    def read(self):
        return self.value

    def write(self, v):
        self.value = v


#This next object is a file cabnet, one that can hold a theoretically infinite number
#of cards. It has a current index that is persistant, and can pass up the value of the current
#card, or pass down a value to be written to it
#In a physical computer, this is noted to be a fixed size without adjustments
class cabinet(object):
    def __init__(self, length):
        self.cards = []

        for i in range(length):
            self.cards.append(card(0))

        #this is the "head" of the machine that points to the current memory adress
        self.head = 0

    def pull(self):
        return self.cards[self.head].read()

    def push(self, value):
        self.cards[self.head].write(value)

    def setHead(self, newHead):
        self.head = newHead

        #wrap this around if it's too large, TODO: remove this and add actual error throwing
        if self.head >= len(self.cards):
          self.head = 0
          #print("corrected")

    #This loads data into the cabinet, useful "out of charecter" to put programs
    #on to a bank or to initialize certain data for testing
    def load(self, data):
      self.cards = []
      for i in data:
        self.cards.append(card(i))


#Up next is our clerk. He's rather stupid unfortunatly, so he can only do what we
#tell him to do, to the letter, but he is able to do things quite quickly(hopefully)
#He can do just a couple of base things, and he has no memory, so we give him a pad
#The pad can store a few numbers(for now), three numbers that we use to execute our
#instructuions, as well as more for normal operations, such as a program counter
#and the current memory adress
class clerk(object):
  def __init__(self, memory_size=10):
    #Materialize a cabinet for our unfortunate soul to work on for eternity
    self.memory = cabinet(memory_size)

    #Bring up another. This one is for holding the memory for our program
    self.program = cabinet(0)
    #We'll load data on to it later

    #The modifiable aspects of the pad
    self.free_registers = [0, 0, 0]
    #The automatic aspects of the pad
    #Register zero is the program head, register one the memory head
    self.reserved_registers = [0, 0]

  #There are several functions that we need to start building anything useful
  #These are really simple, things like add, subtract, store value, read value
  #We generally take them for granted, it's a computer engineer's job to build them
  #so we get to ignore the exact how's of the arcitecture!
  def execute(self, opCode, modifier):
    #The simplest instructions will be to read and write data from the current
    #card into a register. We're going to assume the register's don't need to have
    #seperate modifiers applied to them
    if opCode == 0: #Pulls current memory value to {modifier} free register
      self.free_registers[modifier] = self.memory.pull()
    elif opCode == 1: #Pushes value in register {modifier} to current memory index
      self.memory.push(self.free_registers[modifier])
    #The next instructions are slightly more complicated. They add and subtract
    #The first two register values together and then move that value to the third
    #register
    elif opCode == 2:
      self.free_registers[2] = self.free_registers[0] + self.free_registers[1]
    elif opCode == 3:
      self.free_registers[2] = self.free_registers[0] - self.free_registers[1]

    #Instruction 4 shifts the memory head to the value in {modifier}
    elif opCode == 4:
      self.memory.setHead(self.free_registers[modifier])

    #Instruction 5 modifies the program head - it sets it to a specific value,
    #much like the previous instruction. In essense this acts like a goto statement
    elif opCode == 5:
      self.program.setHead(self.free_registers[modifier])

    #Instruction 6 shifts the memorty head to {modifier}
    elif opCode == 6:
      self.memory.setHead(modifier)

    #Instruction 7 shifts the program head to {modifier}
    elif opCode == 7:
      self.reserved_registers[0] = modifier

    #8 pushes {modifier} directly to memory
    elif opCode == 8:
      self.memory.push(modifier)


  #We're going to define a convention that states the first value of the memory
  #is four our output, and can be accessed freely
  def output(self):
    return self.memory.cards[0].read()
    
  #Now the magic happens. The machine gets the opCode and modifier from the current
  #program memory, incriments the program memory by one, then executes the
  #instruction
  def incriment(self):
    self.reserved_registers[0] = self.program.head
    
    opCode = self.program.pull()[0]
    modifier = self.program.pull()[1]

    self.reserved_registers[0] += 1

    self.execute(opCode, modifier)
    self.program.setHead(self.reserved_registers[0])
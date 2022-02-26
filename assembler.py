"""
An assembler is a program that converts low-level code to machine code
We don't want to code in ones and zeros, so we code in slightly less painful 
symbolic code thats more readable, if only a little bit. This is basically a
compiler, though a very simple one
"""

"""
PUL(0): Pulls current memory value to {modifier} free register
PUS(1): Pushes value in register {modifier} to current memory index
ADD(2): Adds register zero to register one and stores in register two
SUB(3): Subtracts register one from register zero and stores in register two
SMI(4): Shifts the memory head to the value in {modifier}
SPI(5): Shifts the program head to the value in {modifier}
SHM(6): Shift the memory head to {modifier}
SHP(7): Shift the program haed to {modifier}
PSS(8): Pushes {modifier} to memory. Constant
"""

def assemble(fileName):
  with open(fileName, "r") as file:
    program = file.readlines()

  #Dictionary that helps us know which instructions match which numerical code
  instructions = {
    "PUL": 0,
    "PUS": 1,
    "ADD": 2,
    "SUB": 3,
    "SMI": 4,
    "SPI": 5,
    "SHM": 6,
    "SHP": 7,
    "PSS": 8
  }
  
  parsed = []
  for i in range(len(program)):
    parsed.append([])

    curr = ""
    
    for j in program[i]:
      if j == " " or j == "\n":
        parsed[i].append(curr)
        curr = ""
      else:
        curr += j

  compiled = []
  #Now its time to convert this into bytecode
  for i in parsed:
    compiled.append([instructions[i[0]], int(i[1])])

  return compiled


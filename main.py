"""
This virtual machine is based on the one described in the "File Clerk" machine described by
Richard Feynman in his 1980 series of lectures on computing at CalTech, transcribed in "Feynman Lectures on Computation".
Some liberties have been taken where the programmer has deemed it to be useful for varous reasons, being that this is not a 1:1
recreation of the described machine, but instead a useful model for udnerstanding how a modern digital computer works at its most
basic level

Coded by: Lucas Thelen
"""

#Imports our custom library
import cards, time

"""
For the programmer:
0: Pulls current memory value to {modifier} free register
1: Pushes value in register {modifier} to current memory index
2: Adds register zero to register one and stores in register two
3: Subtracts register one from register zero and stores in register two
4: Shifts the memory head to the value in {modifier}
5: Shifts the program head to the value in {modifier}
6: Shift the memory head to {modifier}
7: Shift the program haed to {modifier} TODO: Fix this, its broken currently
"""

cpu = cards.clerk()

memory = [0, 1, 0, 0]

#Simple fibbonaci sequence
code = [
  [6, 1],
  [0, 0],
  [6, 2],
  [0, 1],
  [2, 0],
  [6, 2],
  [1, 0],
  [6, 1],
  [1, 2],
  [6, 0],
  [1, 0],
  [7, 0]
  
]

cpu.memory.load(memory)
cpu.program.load(code)


while True:
  cpu.incriment()
  curr = []
  for i in cpu.memory.cards:
    #print(i.read())
    pass
  print(cpu.output())
  time.sleep(0.1)
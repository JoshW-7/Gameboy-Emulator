import time
import os

from CPU import CPU
from GPU import GPU
from Memory import Memory

RUNNING = True
STEP = False

# Create the memory, to be accessed by several components
Memory = Memory("TETRIS.gb")

# Central Processing Unit (CPU)
CPU = CPU(Memory)
CPU.DEBUG = True

# Graphical Processing Unit (GPU)
GPU = GPU(Memory)

try:
    os.remove("log.txt")
except:
    pass

file = open("log.txt", "w")

BREAKPOINTS = []
BREAK = False


while RUNNING:

    cycles_before = CPU.cycles
    CPU.fetch()

    #print(hex(CPU.PC))
    if CPU.PC in BREAKPOINTS:
        BREAK = True
        print("Breakpoint at " + "0x" + hex(CPU.PC)[2:].zfill(4).upper())

    if BREAK:
        file.write("0x" + hex(CPU.PC)[2:].zfill(4).upper() + " : ")
        file.write(CPU.debug_string + "	")
        for i in range(0,CPU.instruction_length-1):
            file.write(hex(CPU.args[i])[2:].zfill(2).upper() + " ")
        file.write(CPU.print_registers())
        file.write("\n")
        input()

    CPU.decode()

    CPU.execute()
    cycles_after = CPU.cycles
    cycles_passed = cycles_after - cycles_before
    GPU.update(cycles_passed)











































#

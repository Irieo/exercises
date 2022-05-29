import sys

# inputs
Lx, Ly, x, y = [int(i) for i in input().split()]

# game loop
while True:
    remaining_turns = int(input())  # The remaining amount of turns Thor can move.

    step = ''
    
    if y < Ly: step += 'S'
    elif y > Ly: step += 'N'
    if x < Lx: step += 'E'
    elif x > Lx: step += 'W'

    if 'S' in step: y+=1
    if 'N' in step: y-=1
    if 'E' in step: x+=1
    if 'W' in step: x-=1

    print(step)
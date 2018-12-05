#!/usr/bin/env python
import sys
import string

def reactive_units():
    forward = set([f'{char}{char.upper()}' for char in list(string.ascii_lowercase)])
    backward = set([f'{char}{char.lower()}' for char in list(string.ascii_uppercase)])
    return  forward.union(backward)

def react(molecule):
    for reaction in reactive_units():
        molecule = molecule.replace(reaction, '')        
    return molecule

molecule = str(sys.stdin.read())
molecule_length = len(molecule)
molecule_diff = 1

while molecule_diff > 0:
    molecule = react(molecule)
    molecule_diff = molecule_length - len(molecule)
    molecule_length = len(molecule)

print(molecule_length)
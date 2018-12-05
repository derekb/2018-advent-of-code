#!/usr/bin/env python
import sys
import string

def reactive_units():
    forward = set([f'{char}{char.upper()}' for char in list(string.ascii_lowercase)])
    backward = set([f'{char}{char.lower()}' for char in list(string.ascii_uppercase)])
    return  forward.union(backward)

def react(molecule, reactive_units):
    for reaction in reactive_units:
        molecule = molecule.replace(reaction, '')        
    return molecule

def full_reaction(molecule, reactive_units):
    molecule_length = len(molecule)
    molecule_diff = 1

    while molecule_diff > 0:
        molecule = react(molecule, reactive_units)
        molecule_diff = molecule_length - len(molecule)
        molecule_length = len(molecule)
    return molecule_length

def strip_units(molecule, reaction):
    for unit in reaction:
        molecule = molecule.replace(unit, '')        
    return molecule

molecule = str(sys.stdin.read())

results = [(reaction, full_reaction(strip_units(molecule, reaction), reactive_units())) for reaction in reactive_units()]
results.sort(key=lambda tup: tup[1])

troublesome_unit = (min(results, key=lambda result: result[1]))
print(troublesome_unit)
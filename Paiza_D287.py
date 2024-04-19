# coding: utf-8

input_line = input()

parts = input_line.split()

A = int(parts[0])
B = int(parts[1])

cheapest = min(A,round(B*0.7))

print(cheapest)
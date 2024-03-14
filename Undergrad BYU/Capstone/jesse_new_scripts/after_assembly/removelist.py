#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from Bio import SeqIO

arguments = sys.argv
if len(arguments) < 3:
	sys.exit("./removelist.py listtodelete output")


fasta_file = arguments[1]  # Input fasta file
number_file = arguments[2] # Input interesting numbers file, one per line
result_file = arguments[3] # Output fasta file

remove = set()
with open(number_file) as f:
    for line in f:
        line = line.strip()
        if line != "":
            remove.add(line)
fasta_sequences = SeqIO.parse(open(fasta_file),'fasta')
end = False
with open(result_file, "w") as f:
    for seq in fasta_sequences:
        if seq.id not in remove:
            SeqIO.write([seq], f, "fasta")

 
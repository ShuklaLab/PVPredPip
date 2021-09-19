## This script identifies SARS-COV-2 spike glycoprotein sequences which has a "X" character in their amino acid sequence.

file1=open("./172_uniprot_seq_ids.fasta").readlines()

for i in file1:
	if i[0]==">":
		id=i.strip()
	if i[0]!=">" and "X" in i.strip():
		print id


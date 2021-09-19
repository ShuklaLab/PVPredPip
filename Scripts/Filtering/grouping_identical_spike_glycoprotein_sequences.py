## This script groups the identical spike glycoprotein fasta sequences.

file1=open("./164_uniprot_seq_ids_names.txt").readlines()
file2=open("./164_uniprot_seq_ids.fasta").readlines()

for i in file1:
	fn=i.split()[0].split(">")[1].split("|")[0]+"-"+i.split()[0].split(">")[1].split("|")[1]+"-"+i.split()[0].split(">")[1].split("|")[2]
#		print fn

	file3=open("./"+fn+".fa", 'w')
	c=[]

	for j in range(0, len(file2)):
		if i.strip()==file2[j].strip() and str(j) not in c:
			file3.write(file2[j])
			file3.write(file2[j+1])
			seq=file2[j+1].strip()
			c.append(str(j))
			c.append(str(j+1))
			for k in range(0, len(file2)):
				if seq==file2[k].strip() and str(k) not in c:
					file3.write(file2[k-1])
					file3.write(file2[k])
					c.append(str(k))
					c.append(str(k-1))




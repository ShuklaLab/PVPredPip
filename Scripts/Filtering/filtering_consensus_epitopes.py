## This python script filters out all the Singleton results of IEDB clustering tool.
## This python script selects consensus results (peptides) of IEDB cluster tool which included constituent epitopes from two epitope predicton methods.
## The two epitope predicton methods can be B-cell epitope prediction methods (ABCPred and BcePred; see example input and output files 1) or T-cell epitope prediction methods (TepiTool MHC-I and MHC-II; see example input and output files 2).
## This script was also used to selected final consensus results (peptides) of B-Cell and T-Cell epitopes; see example input and output files 3.

file1=open("./filtering_consensus_epitopes_example_input_file_3.txt").readlines()
file2=open("./filtering_consensus_epitopes_example_output_file_3.txt", "w")

flag1=0
pred=[]
clust_numb=[]

for i in range(0,len(file1)):
	if file1[i].split("\t")[1]=="Consensus":
		flag1=flag1+1

	if flag1==1:
		pred.append(file1[i].split("\t")[5].split()[0])

	if flag1==2 or file1[i].split("\t")[1]=="Singleton":
		if "-" in pred:
			pred.remove("-")
		pred=list(set(pred))
		if len(pred)>1:
			clust_numb.append(file1[i-1].split("\t")[0])		
		flag1=1
		pred=[]

file2.write(file1[0])

for j in clust_numb:
	for k in file1:
		if j.strip() == k.split("\t")[0].strip():
			file2.write(k.strip()+"\n")


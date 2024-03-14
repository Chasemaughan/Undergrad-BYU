#!/usr/bin/env python

import sys
import os

arguments = sys.argv


tablefile = arguments[1]
delim= arguments[2]
place= arguments[3]
taxonP= arguments[4]
covmult= arguments[5]
covmult=float(covmult)
lname, crap1 = tablefile.split(".")
outfile1 =open(lname + "_" +  taxonP + "_del_list.txt", "w")
outfile2 =open(lname + "_" +  taxonP +  "_sistaxa_list.txt", "w")
#outfile3 =open(lname + "_" +  taxonP + "_BOTH_del_sistaxa_list.txt", "w")
outfile4 =open(lname + "_" +  taxonP + "_pairfeq_list.txt", "w")
outfile5 =open(lname + "_" +  taxonP + "_taxafeq_list.txt", "w")
outfile6 =open(lname + "_" +  taxonP + "_Locifeq_list.txt", "w")
outfile7 =open(lname + "_" +  taxonP + "_kmerdepthsaved_list.txt", "w")
outfile8 =open(lname + "_" +  taxonP + "_kmerdepthdelete_list.txt", "w")


hit=[]
taxa=set([])
cov_save=set([])
cov_del=set([])
rm_save=set([])
sistaxa=set([])
locidic={}
taxadic={}
pairdic={}
with open(tablefile, "r") as table2:
	makein2=table2.readlines()
	for i in makein2:
		query, target, id, length, mismatch, gaps, qs, qend, ts, tend, evalue, bit=i.split()
		crap="_R"
		if crap in query or crap in target:
			pass
		else:
			if query.split(delim,-1)[0] == target.split(delim,-1)[0]:
				if query.split(delim,-1)[int(place)] != target.split(delim,-1)[int(place)]:
					taxa.add(query)
					taxa.add(target)
#					print taxonP +" do not match\t" + query.split(delim,-1)[0] + "\t" + query +" : "+ query.split(delim,-1)[int(place)] +"\t" +target + ":" + target.split(delim,-1)[int(place)]
					if query.split(delim,-1)[0] in locidic:
						locidic[query.split(delim,-1)[0]] += 1
					else:
						locidic[query.split(delim,-1)[0]] = 1
					
					a,b = query.split(delim,1)
					c,d = target.split(delim,1)
					
					if b.split("_comp")[0] in taxadic:
						taxadic[b.split("_comp")[0]] += 1
					else:
						taxadic[b.split("_comp")[0]] = 1	
					
					if d.split("_comp")[0] in taxadic:
						taxadic[d.split("_comp")[0]] += 1
					else:
						taxadic[d.split("_comp")[0]] = 1	
					
					if b.split("_comp")[0] + "\t" + d.split("_comp")[0] in pairdic:
						pairdic[b.split("_comp")[0] + "\t" + d.split("_comp")[0]] += 1
					else:
						pairdic[b.split("_comp")[0] + "\t" + d.split("_comp")[0]] = 1	
					qcov=float(query.split(delim,-1)[-1])
					tcov=float(target.split(delim,-1)[-1])
					print(str(qcov)+"|"+str(tcov))
					
					if qcov >= covmult*tcov:
						cov_save.add(query)
						cov_del.add(target)
					if covmult*qcov <= tcov:
						cov_save.add(target)
						cov_del.add(query)
					if qcov  < covmult*tcov and covmult*qcov > tcov:
				#	else:
						cov_del.add(query)
						cov_del.add(target)					
						print("yep")
						print(taxonP +" do not match\t" + query.split(delim,-1)[0] + "\t" + query +" : "+ query.split(delim,-1)[int(place)] +"\t" +target + ":" + target.split(delim,-1)[int(place)])

					#(query.split(delim,-1)[-1]+"|"+target.split(delim,-1)[-1])
						

				if query.split(delim,-1)[1] == target.split(delim,-1)[1]:
					sistaxa.add(query)
					sistaxa.add(target)

	
	
#print "Same taxa and loci that match 99% id i.e. possible terminal duplication" + query.split(delim,-1)[0] + "\t" + query + target				
for x in taxa:
	outfile1.write(x +"\n")
for x in sistaxa:
	outfile2.write(x +"\n")
for key in pairdic:
	outfile4.write(key + "\t" + str(pairdic[key]) + "\n")
for key in taxadic:
	outfile5.write(key+ "\t" + str(taxadic[key])+ "\n")	
for key in locidic:
	outfile6.write(key+ "\t" + str(locidic[key])+ "\n")	


#for x in sistaxa:
#	outfile3.write(x +"\n")
#for x in taxa:
#	outfile3.write(x +"\n")


for x in cov_save:
	if x in cov_del:
		rm_save.add(x)
for x in rm_save:
	cov_save.remove(x)


for x in cov_save:
	outfile7.write(x +"\n")
for x in cov_del:
	outfile8.write(x +"\n")


print("Number of sequnces that are probable contaimination 99% match with a sequence from a diffrent " + taxonP + "\t" +  str(len(taxa)))
print("Number of sequnces saved with "+str(covmult)+" times more avg kmer coverge \t" +  str(len(cov_save)))
print("Number of sequnces to deleted based on the kmer multiplier \t" +  str(len(cov_del)))
print("Number of sequnces from the same taxa for the same loci that with 99% id\t" + str(len(sistaxa)))

table2.close()
outfile1.close()
outfile2.close()
#outfile3.close()

outfile4.close()
outfile5.close()
outfile6.close()
outfile7.close()
outfile8.close()


sys.exit()
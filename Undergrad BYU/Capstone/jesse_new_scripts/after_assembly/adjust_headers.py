import sys

infilename = sys.argv[1]
outfilename = infilename.split(".")[0] + "_headers.fa"

with open(infilename) as infile:
    with open(outfilename, "w") as outfile:
        for line in infile:
            if line[0] == ">":
                taxon = "_".join(line.split("_")[1:5])
                outfile.write(">" + taxon + "\n")
            else:
                outfile.write(line)
            

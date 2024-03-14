#!/bin/bash


#SBATCH --job-name=LOCI_ASS
#SBATCH -o %A_%a.LOCI_ASS.out
#SBATCH -e %A_%a.LOCI_ASS.err
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=jessebreinholt@gmail.com
#SBATCH --mem-per-cpu=3000mb
#SBATCH -t 24:00:00
#SBATCH -n 1
#SBATCH -c 16
#SBATCH --qos=rgenomics
#SBATCH --array=1-5

#-b to line12 for burst
module load gcc/5.2.0 spades python ncbi_blast usearch

INFILE1=$(head -n $SLURM_ARRAY_TASK_ID butmiss | tail -n1|cut -f1)
INFILE2=$(head -n $SLURM_ARRAY_TASK_ID butmiss | tail -n1|cut -f2)
taxa=$(head -n $SLURM_ARRAY_TASK_ID butmiss | tail -n1|cut -f3)

#INFILE1=$(head -n $SLURM_ARRAY_TASK_ID REASSLIST | tail -n1|cut -f1)
#INFILE2=$(head -n $SLURM_ARRAY_TASK_ID REASSLIST | tail -n1|cut -f2)
#taxa=$(head -n $SLURM_ARRAY_TASK_ID REASSLIST | tail -n1|cut -f3)

#python SPADES_ASS.py -ing Stenopsyche_tienmushanensis_v1_genome.fasta -inp genes26.fa -threads 8 -tname $taxa -flanksize 0 -1 $INFILE1 -2 $INFILE2 -rname Campy_jejuni

time python ASS_F.py -ing Stenopsyche_tienmushanensis_v1_genome.fasta -inp SINGLEREF_TRI_REF2.fa -inpf ALL_TRI_REF2.fa -threads 16 -tname $taxa -flanksize 0 -1 /orange/rgenomics/Sequencing_Data/BYU_138901/ANALYSIS/Plate1-2/$INFILE1 -2 /orange/rgenomics/Sequencing_Data/BYU_138901/ANALYSIS/Plate1-2/$INFILE2 -rname Stenopsyche_tienmushanensis

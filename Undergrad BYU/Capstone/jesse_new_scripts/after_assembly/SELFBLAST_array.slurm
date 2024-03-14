#!/bin/bash
#SBATCH --job-name=SBLAST
#SBATCH -o %A_%a.SBLAST
#SBATCH --mail-type=FAIL
#SBATCH --mail-user=jessebreinholt@gmail.com
#SBATCH --mem-per-cpu=8000mb
#SBATCH -t 09:00:00
#SBATCH -n 1
#SBATCH -c 8
#SBATCH --array=1-372

INFILE=$(head -n $SLURM_ARRAY_TASK_ID INLIST | tail -n1)
module load usearch



usearch -ublast $INFILE -db $INFILE -evalue 0.01 -id 0.98 -self -query_cov 0.95 -strand both -threads 8 -blast6out $INFILE.blast

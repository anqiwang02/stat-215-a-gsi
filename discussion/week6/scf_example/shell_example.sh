#!/bin/bash
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --nodes=1

# pls change the below line so I don't get emails about your jobs lol
#SBATCH --mail-user=ozerov@berkeley.edu
#SBATCH --mail-type=ALL

python parallel_scf.py > parallel_scf.out

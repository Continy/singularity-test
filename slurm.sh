#!/bin/bash

# SLURM Resource Parameters

#SBATCH -n 6                       # Number of cores
#SBATCH -N 1                        # Number of nodes always 1
#SBATCH -t 0-00:10 # D-HH:MM        # Time using the nodes
#SBATCH -p dgx1-gpu                 # Partition you submit to
#SBATCH --gres=gpu:1               # GPUs
#SBATCH --mem=16G                   # Memory you need
#SBATCH --job-name=HelloSlurm       # Job name
#SBATCH -o job_%j.out
#SBATCH -e job_%j.err
#SBATCH --mail-type=ALL             # Type of notification BEGIN/FAIL/END/ALL
#SBATCH --mail-user=satanama.ring@gmail.com
# Executable
EXE=/bin/bash

singularity shell --bind /project/learningvo/tartanair_v1_5/abandonedfactory/Data:/zihao/datasets:ro,/data2/datasets/yuhengq/zihao/singularity-test:/zihao/singularity-test /data2/datasets/yuhengq/zihao/flowformer.sif
bash /zihao/singularity-test/run_script.sh
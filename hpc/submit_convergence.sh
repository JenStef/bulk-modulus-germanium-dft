#!/bin/bash

#SBATCH -A mtgn473_spring2026_vstevano
#SBATCH -p student
#SBATCH --nodes=1 # number of nodes
#SBATCH --ntasks-per-node=4 # number of tasks per node
####SBATCH --ntasks=12 # redundant; total number of tasks: ntasks = nodes * ntasks-per-node
#SBATCH --time=00:10:00 # time in HH:MM:SS
#SBATCH -o ./jobs/%j/output.%j # standard print output labeled with SLURM job id %j
#SBATCH -e ./jobs/%j/error.%j  # standard print error  labeled with SLURM job id %j

# module loads here



# Define the options: v is a flag, f: requires an argument
while getopts ":f:" opt; do
  case $opt in
    f)
      FILE_PATH="$OPTARG"
      echo "File path specified: $FILE_PATH"
      ;;
  esac
done


OUTPUT_FILE_NAME=$(basename -s .in $FILE_PATH).out
echo "$OUTPUT_FILE_NAME"

echo "Job has started!"
srun -n 4 ./pw.x < $FILE_PATH > ./output/$OUTPUT_FILE_NAME
echo "Job has ended!"

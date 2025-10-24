
#!/bin/bash
#SBATCH --job-name=your_job_name  # Job name
#SBATCH --partition=geocean       # Standard output and error log
#SBATCH --mem=4gb                 # Memory per node in GB (see also --mem-per-cpu)

case_dir=$(ls | awk "NR == $SLURM_ARRAY_TASK_ID")
yourLauncher.sh --case-dir $case_dir > $case_dir/wrapper_out.log 2> $case_dir/wrapper_error.log

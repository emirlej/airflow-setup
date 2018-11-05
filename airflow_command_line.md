# Useful airflow command line arguments

### It might be more convenient to use these commands

```bash
airflow clear <dag-id> # Clear all runs for a dag
airflow backfill -s <start-date> -e <end-date> -m <dag-id> # Trigger and backfill without the need to pause the dag
airflow test <dag-id> <task-id> <execution-date> # Testing 
```
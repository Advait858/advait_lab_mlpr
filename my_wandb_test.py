import wandb

# 1. Login to wandb (only once per session)
wandb.login(key="002b9beb1304272a9f38f51e52d99718ff0db18a")

# 2. Initialize your run
wandb.init(project="distance_classification_project")

# 3. Example usage: log a metric
#accuracy_value = 0.90
#wandb.log({"accuracy": accuracy_value})

print("Done logging to W&B!")

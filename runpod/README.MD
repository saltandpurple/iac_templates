# Runpod Utility scripts
Since (of this writing) there is no official Terraform Provider for Runpod infrastructure, I am creating a few scripts to at least partially 
automate things I do all the time on runpod. Execution is extremely straightforward:

```
# Do this in a venv, obviously
pip install -r requirements.txt
export RUNPOD_API_KEY=YOUR_API_KEY
python3 create_runpod.py # or one of the other scripts
```

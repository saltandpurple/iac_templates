# Runpod Utility scripts
Since (of this writing) there is no official Terraform Provider for Runpod infrastructure, I am creating a few scripts to at least partially 
automate things I do all the time on runpod. Execution is extremely straightforward:

```
# Do this in a venv, obviously
pip install -r requirements.txt
export RUNPOD_API_KEY=YOUR_API_KEY

python3 create_runpod.py # or one of the other scripts
```
You can set the pod name via the env POD_NAME. Otherwise it's "default_pod".
Make sure to configure the pod properly in the script (disk size, GPU, image etc).

Something I found useful (require the [Runpod CLI tool](https://github.com/runpod/runpodctl)):
```
runpodctl send some-file # on the sending machine
runpodctl receive some-other-file <SOME_CODE_YOU_GET_FROM_THE_FIRST_COMMAND> # run on the receiving machine, obviously
```
These commands do not require an API Key but make use of one-time keys. It's pretty neat for quickly transferring some model or whatever between a pod and your machine.


# SSH connection script (automatically get ID and ssh into it)
# Runpod Utility scripts
Since (of this writing) there is no official Terraform Provider for Runpod infrastructure, I am creating a few scripts to at least partially 
automate things I do all the time on runpod. Execution is extremely straightforward:

## Pod creation & deletion
Since I frequently needed to automate this to at least some extent, I wrote small scripts doing this:
Expects that the RUNPOD_API_KEY env is set and the `requests`-package has been installed.
```
python3 create_runpod.py
```
You can set the pod name via the env POD_NAME. Otherwise it's "default_pod".
Make sure to configure the pod properly in the script (disk size, GPU, image etc).

```
python3 delete_runpod.py <POD_ID> # pod_id is optional, uses the POD_NAME otherwise.
```

## File transfer
Something I found useful (require the [Runpod CLI tool](https://github.com/runpod/runpodctl)):
```
runpodctl send some-file # on the sending machine
runpodctl receive some-other-file <ONE_TIME_CODE> # run on the receiving machine, obviously
```
These commands do not require an API Key but make use of one-time keys. It's pretty neat for quickly transferring some model or whatever between a pod and your machine.


## SSH connection 
Since it's fiddly to look-up a Runpod's IP manually to SSH into it (and it changes on every pod pause/restart, naturally), a small script to automate this as well.

```
python3 connect_runpod.py <POD_NAME> # pod name is a mandatory param here
```
Defaults to expecting your SSH-key in `~/.ssh/id_ed25519_runpod`, adjust as needed. Also uses `sshpass` to provide the default-password (always "runpod") for the SSH connection (actual auth is done via Key, naturally).
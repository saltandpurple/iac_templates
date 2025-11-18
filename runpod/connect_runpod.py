#!/usr/bin/env python3
import os
import sys
import requests

def connect_runpod():
    api_key = os.getenv('RUNPOD_API_KEY')
    if not api_key:
        raise ValueError("RUNPOD_API_KEY environment variable is required")

    if len(sys.argv) < 2:
        sys.exit("Usage: connect_runpod.py <pod_name>")

    pod_name = sys.argv[1]
    headers = {"Authorization": f"Bearer {api_key}"}

    try:
        print(f"Searching for pod {pod_name}...")
        pods_url = "https://rest.runpod.io/v1/pods"
        resp = requests.get(pods_url, headers=headers)
        resp.raise_for_status()
        pods = resp.json()

        pod = next((p for p in pods if p.get('name') == pod_name), None)
        if not pod:
            sys.exit(f"Error: Pod {pod_name} not found.")

        ip = pod.get('publicIp')
        port = pod.get('portMappings', {}).get('22')
        if not ip or not port:
            sys.exit(f"Error: Pod {pod_name} missing publicIp or SSH port mapping.")

        print(f"Found pod: {pod['id']} at {ip}:{port}")
        print(f"Connecting: ssh root@{ip} -p {port}")
        os.execvp("sshpass", ["sshpass", "-p", "runpod", "ssh", f"root@{ip}", "-p", str(port), "-i", os.path.expanduser("~/.ssh/id_ed25519_runpod")])

    except requests.exceptions.RequestException as e:
        error = f"API request failed: {e}"
        if e.response is not None:
            error += f" | Response: {e.response.text}"
        sys.exit(error)

if __name__ == "__main__":
    connect_runpod()

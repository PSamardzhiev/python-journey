import proxmoxer
import requests
import time

# Disable warnings about insecure HTTP requests
requests.packages.urllib3.disable_warnings()

# Proxmox host details and credentials
proxmox_host = '192.168.1.2'  # replace with your IP address

# Function to get VM list from user input
def vms_to_start():
    vms = input("Enter VM list to start (example: 100, 101, 102 etc):")
    return vms

vms_list = vms_to_start()

print(f"The script will try to start virtual machines with VMIDs: {vms_list}")
print("Press CTRL + C to abort")
time.sleep(3)

# Function to obtain credentials from a file
def obtain_credentials(cred_path):
    with open(cred_path, 'r') as crd:
        username = crd.readline().strip()
        password = crd.readline().strip()
    return username, password

username, password = obtain_credentials(cred_path='pass.txt')

# Create a Proxmox API session
proxmox = proxmoxer.ProxmoxAPI(
    proxmox_host,
    user=username,
    password=password,
    verify_ssl=False
)

# Start the VMs from the VM list
for vmid in vms_list.split(","):
    vmid = int(vmid.strip())    
    try:
        node_name = 'pve'  # Replace with the actual name of your node

        # Check VM status
        status = proxmox.nodes(node_name).qemu(vmid).status.current.get()
        if status['status'] == 'running':
            print(f"VM with VMID {vmid} is already running.")
        else:
            result = proxmox.nodes(node_name).qemu(vmid).status.start.post()
            print(f"Started VM with VMID {vmid}: {result}")
        time.sleep(3)
    except Exception as e:
        print(f"Failed to start VM {vmid}: {e}")

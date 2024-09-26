import subprocess
import json

def read_flavor(filename):
    with open(filename, 'r') as file:
        return file.read().strip()

def write_to_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

hypervisor_name = 'compute01.kle.com'
node = 'compute01'
openstack_command = f"openstack hypervisor show {hypervisor_name} -f json"
node1=' '
try:
    result = subprocess.run(openstack_command, shell=True, capture_output=True, text=True)

    if result.returncode == 0:
        output = result.stdout
        hypervisor_info = json.loads(output)

        vcpu_total = hypervisor_info.get('vcpus', 0)
        vcpu_used=hypervisor_info.get('vcpus_used',0)
        vcpu_available=vcpu_total-vcpu_used
        ram_total = hypervisor_info.get('free_ram_mb', 0)
        disk_total = hypervisor_info.get('free_disk_gb', 0)

        print(f"vCPU Total: {vcpu_available}")
        print(f"RAM Total: {ram_total} MB")
        print(f"Disk Space Total: {disk_total} GB")

        flavor = read_flavor('flavor.txt')

        if flavor == "m1.tiny":
            vcpus = 1
            ram = 512
            disk_space = 1
        elif flavor == "m1.med":
            vcpus = 2
            ram = 2048
            disk_space = 40
        elif flavor == "m1.large":
            vcpus = 2
            ram = 2048
            disk_space = 20
        else:
            print("Flavor not recognized.")

        if vcpu_available > vcpus and ram_total > ram and disk_total > disk_space:
            write_to_file('name1.txt', node)
        else:
            write_to_file('name1.txt', node1)
            print("Resources not sufficient for the selected flavor.")
    else:
        print("Failed to retrieve hypervisor information")

except Exception as e:
    print(f"An error occurred: {str(e)}")
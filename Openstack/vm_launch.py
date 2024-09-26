import subprocess

# Read flavor name from the file
with open("flavor.txt", "r") as flavor_file:
    flavor = flavor_file.readline().strip()

image = input("Enter the image (e.g., cirros): ")

# Use the openstack command to get the network ID
network_id_command = "openstack network show -c id -f value private"
network_id = subprocess.check_output(network_id_command, shell=True, text=True).strip()

security_group = input("Enter the security group: ")
server_name = input("Enter the server name: ")

# Read compute node name from the file
with open("node.txt", "r") as file:
    compute_node = file.readline().strip()

# Construct the command with user input and compute node name
command = f"openstack server create --flavor {flavor} --image {image} --nic net-id={network_id} --security-group {security_group} --availability-zone nova:{compute_node} {server_name}"

# Run the command
subprocess.run(command, shell=True)
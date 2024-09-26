
import paramiko
import time
import csv
import subprocess  

def collect_system_data(ip, username, password, duration=500):
    with open('data1.csv', 'w', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        csv_writer.writerow(["time", "cpu", "memory", "bandwidth", "rtt", "throughput", "latency"])

        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ssh.connect(ip, username=username, password=password)

            iperf_server_command = "iperf -s"
            ssh.exec_command(iperf_server_command)

            for i in range(duration):
                rtt_process = subprocess.Popen(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                rtt_result = rtt_process.communicate()[0].decode('utf-8')
                rtt_lines = rtt_result.split('\n')
                rtt_time = "N/A"
                for line in rtt_lines:
                    if "time=" in line:
                        rtt_time = line.split('time=')[1].split()[0]

                latency_process = subprocess.Popen(["ping", "-c", "1", ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                latency_result = latency_process.communicate()[0].decode('utf-8')
                latency_lines = latency_result.split('\n')
                latency_value = "N/A"
                for line in latency_lines:
                    if "time=" in line:
                        latency_value = line.split('time=')[1].split()[0]

                iperf_client_command = f"iperf -c {ip} -t 1"  
                throughput_process = subprocess.Popen(iperf_client_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                throughput_result = throughput_process.communicate()[0].decode('utf-8')
                throughput_lines = throughput_result.split('\n')
                throughput_value = "N/A"
                for line in throughput_lines:
                    if "bits/sec" in line:
                        throughput_value = line.split()[-2]

                stdin, stdout, stderr = ssh.exec_command("top -b -n 1 | awk '/^%Cpu/{print $2, $4, $6}' && free -m | awk 'NR==2{printf \"%s\", $3}' && ifstat -t 1 1 | awk '{print $1}'")

                result = stdout.read().decode('utf-8').split()

                timestamp = i + 1

                if len(result) >= 4:
                    csv_writer.writerow([timestamp, result[0], result[1], result[3], rtt_time, throughput_value, latency_value])
                else:
                    print(f"Unexpected output format on iteration {i + 1}. Skipping.")

                time.sleep(1)

        except Exception as e:
            print(f"An error occurred: {str(e)}")

        finally:
            ssh.close()

# Replace 'your_username', 'your_password', and 'script_name.py' with your actual credentials and script name
collect_system_data("192.168.40.23", "ubuntu", "1234", duration=500)
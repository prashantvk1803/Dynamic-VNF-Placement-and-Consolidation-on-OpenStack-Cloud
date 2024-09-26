# Dynamic VNF Placement and Consolidation in Openstack Cloud using Machine Learning


## Introduction
Network Function Virtualization (NFV) revolutionizes the traditional networking landscape by replacing dedicated network hardware with software-driven alternatives. This approach allows network functions, which were once dependent on specific hardware, to be implemented as software, running on standard servers. Virtualized Network Functions (VNFs), such as firewalls, load balancers, and intrusion detection systems, exemplify this transition. By enabling these functions through software, NFV offers greater flexibility, scalability, and cost efficiency compared to traditional hardware-based solutions.

In parallel, Software-Defined Networking (SDN) enhances network management by centralizing control and providing a comprehensive, unified view of the entire network. SDN decouples the network control plane from the data plane, enabling administrators to manage network services through a centralized interface. This centralized approach simplifies network management, improves agility, and facilitates more efficient resource allocation.

Moreover, the consolidation of Virtual Machines (VMs) plays a crucial role in cloud computing environments. VM consolidation involves reallocating virtual machines across physical hosts to optimize resource utilization and improve overall efficiency. By strategically consolidating VMs, cloud service providers can reduce energy consumption, lower operational costs, and enhance the performance of their infrastructure. This process ensures that physical resources are used more effectively, ultimately leading to a more sustainable and cost-effective cloud computing ecosystem.

## Motivation
**Need of Network Function Virtualisation**

NFV streamlines network operations by reducing the dependency of software on    hardware, reducing costs,  and accelerating service deployment.
NFV enhances network flexibility, allowing dynamic resource allocation and efficient network management.

**Why efficient VNF placement and consolidation is important?**

Efficient VM placement and consolidation optimize resource utilization, reducing costs associated with hardware procurement, maintenance, and energy consumption.
This strategy enhances system performance by balancing workloads across physical hosts, ensuring consistent service delivery and scalability while aligning with sustainability goals.


## Problem Statement
To develop an efficient strategy for placing VNFs within an NFV network on Openstack cloud platform by analyzing resource utilization and implementing VNF consolidation to maximize resource efficiency.

## System Model
![systemmodel](https://github.com/user-attachments/assets/13f08648-f341-48ad-9243-c788ec35f28a)

Our proposed model has following modules:
1. Resource monitoring module
2. Filter host module
3. LSTM prediction module
4. Placement module
5. Consolidation module


## Flow Chart

### Placement Module
![placementfinal drawio (1)](https://github.com/user-attachments/assets/212f3493-a660-4ca2-9335-666ced76015a)

### Consolidation Module
![migrate drawio (1)](https://github.com/user-attachments/assets/66022e72-ee05-4ed3-bdc7-9d6e88d005b7)


## Dataset Description

The table provides descriptions and units for various parameters used to record real-time metrics in the dataset. The dataset consists of 8,640 rows and 8 columns, with data recorded over 2 days at intervals of 20 seconds per data point.

#### Parameters and Descriptions

- **Date**: Specific date when the event occurred. Unit: day (d)
- **Time**: Specific moment when metrics are recorded. Unit: seconds (s)
- **CPU Utilization**: Percentage of CPU resources being used. Unit: percentage (%)
- **Memory Utilization**: Percentage of memory being used. Unit: percentage (%)
- **Latency**: Delay in data transmission. Unit: milliseconds (ms)
- **RTT (Round-Trip Time)**: Time taken for a signal to travel from source to destination and back. Unit: milliseconds (ms)
- **Bandwidth**: Maximum rate of data transfer across a network path. Unit: megabits per second (Mbps)
- **Throughput**: Actual rate of successful data transfer over a communication channel. Unit: megabits per second (Mbps)

These metrics were collected using various system commands such as `top` for CPU usage, `free` for memory usage, `ping` for latency and RTT, `ifstat` for network bandwidth, and `iperf` for throughput. The dataset provides a detailed record of system performance metrics essential for analysis and optimization of network and computing resources.


## Mathematical Model for VM Consolidation

In optimizing the VM consolidation module, an Integer Linear Programming (ILP) model plays a pivotal role. The ILP model aims to minimize Virtual Network Function (VNF) migrations across servers and reduce the number of active servers, thereby improving resource utilization efficiency while maintaining system performance.

#### Parameters Used in ILP

- **`migrate_vnf_{vnf, server}`**: Binary variable indicating if a VNF is migrated to a server.
- **`server_active_{server}`**: Binary variable indicating if a server is active.
- **`VNF_Specs_{vnf}`**: Specifications of a Virtual Network Function.
- **`Server_Specs_{server}`**: Specifications of a server.
- **`Server_Load_{server}`**: Resource utilization value of the server at a given time instance.
- **`Upper_threshold`**: Upper threshold for server resource utilization.
- **`Lower_threshold`**: Lower threshold for server resource utilization.

#### Thresholds Used in the Model

Two thresholds are utilized to classify resource utilization:
- **`upper_threshold`**: Mean resource utilization value plus standard deviation.
- **`lower_threshold`**: Mean resource utilization value minus standard deviation.

#### Decision Variables

- **Migration of VNF**: `migrate_vnf_{vnf, server}` ∈ {0, 1}
- **Server Active Status**: `server_active_{server}` ∈ {0, 1}

#### Constraints

- **VNF Placement**: Each VNF must be placed on exactly one server.
- **Resource Capacity**: Ensures server resource capacities are not exceeded.
- **Resource Utilization**: Limits server resource utilization based on predefined thresholds.

#### Objective

The objective is to minimize the number of active servers, total downtime, and the number of migrations to reduce overall power consumption.

#### Optimization Goal

Minimize:
$$
\sum_{\text{server}} (server\_active\_{\text{server}} + \sum_{\text{vnf}} migrate\_vnf\_{\text{vnf, server}})
$$


This ILP model provides a structured approach to efficiently consolidate Virtual Machines across a cloud infrastructure, optimizing resource usage and operational costs.
## Results
### Lightly Loaded Scenario
![lightly](https://github.com/user-attachments/assets/8ef22a08-57e9-44af-a8d5-dd31916e9b70)

### Moderately Loaded Scenario
![moderately](https://github.com/user-attachments/assets/2877fe2f-1b1e-4a38-b6f4-315cf19c8dd4)

### Highly Loaded Scenario
![highly](https://github.com/user-attachments/assets/b3505d7c-9c03-42f4-ad02-f5038a44d068)


## Conclusion
In our proposed work, we have optimised VNF placement within NFV and SDN through the effective implementation of key features and services. By developing a robust load prediction model using machine learning and a layered architecture with control and data planes, we achieved optimal resource utilisation, reduced energy consumption, and enhanced system performance. We also employed a consolidation strategy using LSTM networks and ILP to further optimise VNF placement. This ILP-LSTM-driven strategy significantly improved power consumption and reduced the number of active servers, enhancing energy efficiency and lowering operational costs. However, this optimisation has led to an average 12.5% SLA violation rate due to increased CPU utilisation and longer response times, highlighting the need for a more balanced approach. While our current implementation has made significant strides in optimising VNF placement, the high CPU utilisation and delayed response times indicate the need for a more balanced optimisation strategy.



# Team Members

| **Name**            | **USN**       | 
|---------------------|---------------|
| Ananya Deshpande    | 01FE21BCS059  |
| Pragati D Bhat      | 01FE21BCS070  |
| Prashant K          | 01FE21BCS073  |
| Supreet Palankar    | 01FE21BCS068  |

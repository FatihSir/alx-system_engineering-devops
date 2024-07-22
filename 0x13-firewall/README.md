# 0x13. Firewall
![Firewall](1.jpeg)


#### Firewall Introduction

A firewall is a crucial security system that monitors and controls incoming and outgoing network traffic based on predetermined security rules. It acts as a barrier between a trusted internal network and untrusted external networks, such as the internet. Firewalls can be hardware-based, software-based, or a combination of both.

### Types of Firewalls

1. **Packet-Filtering Firewalls**: These firewalls inspect packets transferred between computers. They accept or reject packets based on user-defined rules. This type of firewall is effective but can be susceptible to certain attacks.

2. **Stateful Inspection Firewalls**: More advanced than packet-filtering firewalls, these track the state of active connections and make decisions based on the context of the traffic.

3. **Proxy Firewalls**: These firewalls act as an intermediary between the client and the server, filtering all messages at the application layer.

4. **Next-Generation Firewalls (NGFW)**: These provide advanced features like in-line deep packet inspection, intrusion prevention systems (IPS), and more.

### Common Firewall Configurations

- **Default Deny**: Blocks all traffic by default and only allows traffic that is explicitly permitted.
- **Default Allow**: Allows all traffic by default and only blocks traffic that is explicitly denied.

### Benefits of Using a Firewall

- **Enhanced Security**: Firewalls prevent unauthorized access and can protect against various types of cyber attacks.
- **Traffic Monitoring**: They provide detailed logs of traffic which can be used for monitoring and auditing purposes.
- **Access Control**: Firewalls can enforce policies regarding who can access resources within the network.
- **Improved Privacy**: By blocking malicious traffic, firewalls help maintain the privacy and integrity of data.

### Conclusion

Implementing a firewall is an essential step in safeguarding your network. It helps to establish a secure environment for your applications and data by controlling the flow of traffic and preventing unauthorized access. Whether you are managing a small personal network or a large enterprise system, a properly configured firewall is a cornerstone of effective cybersecurity.

#### 0. Block all incoming traffic but

Let’s install the ufw firewall and setup a few rules on web-01.

##### Requirements:

- The requirements below must be applied to `web-01` (feel free to do it on `lb-01` and `web-02`, but it won’t be checked)
Configure `ufw` so that it blocks all incoming traffic, except the following TCP ports:
    - `22` (SSH)
    - `443` (HTTPS SSL)
    - `80` (HTTP)
- Share the `ufw` commands that you used in your answer file
##### Repo:

- GitHub repository: `alx-system_engineering-devops`
- Directory: `0x13-firewall`
- File: `0-block_all_incoming_traffic_but`

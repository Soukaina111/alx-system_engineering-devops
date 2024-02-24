![Distributed](https://i.imgur.com/wSsNvGp.png)

Description

This is a distributed web infrastructure that atttempts to reduce the traffic to the primary server by distributing the load of the traffic using load balancer and two servers.

Specifics About This Infrastructure
 how it works.
This load balancer is configured with the Round Robin distribution algorithm. This algorithm works by using each server  according to their weights. As a dynamic algorithm, Round Robin allows server weights to be adjusted.

The setup enabled by the load-balancer.

The HAProxy load-balancer is enabling an Active-Passive setup rather than an Active-Active setup. In an Active-Active setup, all th servrs ar active to prevent any point failure from one server or another. On the other hand, in an Active-Passive setup,only the active server will be availabl and the other one will be the mirror of it, in case the frt one failed to serve , the failover willturn on the passive one , so that the user won't notice any failure on the process.

How a database Primary-Replica (Master-Slave) cluster works.
A Primary-Replica setup configures one server to act as the Primary server and the other server to act as a Replica of the Primary server. However, the Primary server is capable of performing read/write requests whilst the Replica server is only capable of performing read requests. Data is synchronized between the Primary and Replica servers whenever the Primary server executes a write operation.

The difference between the Primary node and the Replica node in regard to the application.

The Primary node is responsible for all the write operations  while the Replica node is capable of processing read operations, which decreases the read traffic to the Primary node.

Issues With This Infrastructure
There are multiple SPOF (Single Point Of Failure).
For example, if the Primary MySQL database server is down, the entire site would be unable to make changes to the site (including adding or removing users). The server containing the load balancer and the application server connecting to the primary database server are also SPOFs.
Security issues.

The data transmitted over the network isn't encrypted using an SSL certificate so hackers can spy on the network. There is no way of blocking unauthorized IPs since there's no firewall installed on any server.
No monitoring.
We have no way of knowing the status of each server since they're not being monitored.


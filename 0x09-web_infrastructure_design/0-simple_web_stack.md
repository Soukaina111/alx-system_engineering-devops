![LAMP](https://i.imgur.com/p2uyTqY.png)
Description

The current fils represents a simple web infrastructure that hosts a website with the domain name foobar.com. this infrastructure is the basic one without any  firewalls or SSL certificates for protecting the server's network. All the  components of the LAMP stack hasto share the resources provided by the server APACHE.

Specifics About This Infrastructure

What is a server .
A server is a physical hardware or software that provides services (resources) to clients.

The role of the domain name.

The domain name is important because it's the human readable equivalent to IP adresses, it's the edge beetween the machine language and the human one .

The type of DNS record www is in www.foobar.com.

www.foobar.com uses an A record. This can be checked by running dig www.foobar.com.

The role of the web server.
The web server's role is to provide the static content of a web pages requested via HTTP protocol.

The role of the application server.
the role of aaplication server is to provide the dynamic part of the requested content and to install, operate and host applications and associated services for end users, IT services and organizations and facilitates the hosting and delivery of high-end consumer or business applications

The role of the database.
Database is the collection of the datasets of all the resources, and is important to maintain a collection of organized information that can easily be accessed, managed and updated

What the server uses to communicate with the client (computer of the user requesting the website).
Communication is ensured using the TCP/IP protocol suite.

Issues With This Infrastructure

SPOF (Single Point Of Failure):
There is many failure points in this infrastructur, for instance if the  database server is down, the entire site would be down, or if the server is no more functional, no responses would be available.

Downtime when maintenance needed.
When we need to run some maintenance checks on any component, they have to be put down or the server has to be turned off. Since there's only one server, the website would be experiencing a downtime, and we won't be able to set the active-passive or active-passive approach to deal with this issue

Cannot scale if there's too much incoming traffic.
Because we only have one server, and no load balancer .

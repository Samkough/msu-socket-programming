# MSU Socket Programming
This repository was inspired by my CSIT340 - Computer Networks course. We were assigned projects to create programs that deal with sockets and networks.

## Requirements
* Python 3.5+ (haven't tried with anything lower than 3.5)

## Projects
### Project 01
* Built a basic TCP and UDP client/server

### Project 03
* Same thing as Project 01 except now, with a new purpose:
     * Users will input some math expression, such as “2 + 3”, “2 *3    ”, “2    + 3 * 4/5”, etc., in the client. The client will send the math expression to the server.
     * The server will evaluate the result of the received math expression, and send back the final result back to the requesting client. The result should be sent back as a string. For example, if the server receives “2 + 3”, it will send back “5”. If the server receives “2 *3    ”, it will send back “6”.
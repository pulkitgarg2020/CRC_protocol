# CRC_protocol

This program is to implement the message sending and receiving mechanism in Cyclic Redundancy Check (CRC) protocol.

There are two methods in this program which are as follows:

### Sender
Given a message M(x) (a bit string) and the reference polynomial G(x)
(another bit string), the method computes the CRC remainder and determine P(x) - the bit string that will be transmitted.
As an example, if M(x) = 1101011 and G(x) = 1101, the method should return P(x) =
1101011010

### Receiver
Given a bit string with CRC remainder appended, this method would divide the bit string by G(x) and determine if the message is error-free or not. 

The program can be simply run with the following command:
```
py crc.py
```
After a successful execution of the program, you will get prompts which are self explanatory. 


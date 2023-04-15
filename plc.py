import socket

plc = "10.0.1.88"
port = 10002

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((plc,port))

relay = []
def relay_control(value):
    global relay
    rly = value
    relay = [0x40,0x30,0x30,0x31,0x0D]

    if(rly==0):
        relay[3] = 0x30
    elif (rly==1):
        relay[3] = 0x31
    elif (rly==2):
        relay[3] = 0x32
    elif (rly==3):
        relay[3] = 0x34
    elif (rly==4):
        relay[3] = 0x38

    elif (rly==12 or rly==21):
        relay[3] = 0x33
    elif (rly==13 or rly==31):
        relay[3] = 0x35
    elif (rly==14 or rly==41):
        relay[3] = 0x39
    elif (rly==23 or rly==32):
        relay[3] = 0x36
    elif (rly==24 or rly==42):
        relay[3] = 0x36
    elif (rly==34 or rly==43):
        relay[3] = 0x43

    elif (rly==123 or rly==132 or rly==213 or rly==231 or rly==321 or rly==312):
        relay[3] = 0x37

    elif (rly==234 or rly==243 or rly==324 or rly==342 or rly==432 or rly==423):
        relay[3] = 0x45

    elif (rly==134 or rly==143 or rly==413 or rly==431 or rly==341 or rly==314):
        relay[3] = 0x44

    elif (rly==124 or rly==142 or rly==412 or rly==421 or rly==241 or rly==214):
        relay[3] = 0x42

    elif (rly==1234):
        relay[3] = 0x46
    return relay

relay_control(4)
s.send(bytes(relay))
data = s.recv(1024)
s.close()
print(repr(data))
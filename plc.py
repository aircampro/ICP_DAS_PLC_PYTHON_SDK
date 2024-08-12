# ref:- https://github.com/aman983/ICP_DAS_PLC_PYTHON_SDK/tree/main
#
# example to read ICP DAS PLC over TCP/IP
#
import socket
class ICP_DAS_PLC():    
    def __init__(self,IP,PORT):
        self.IP = IP
        self.PORT = PORT
        self.Command = []
        self.type = ""
        self.dev_con = 0
    def __del__(self):
        if self.dev_con == 1:
            self.dev.close()        
    def Connect(self):
        try:
            self.dev = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            self.dev_con = 1
            self.dev.settimeout(10)
            self.dev.connect((self.IP,self.PORT))
        except socket.error as e:
            print("exception : ",e)
            if self.dev_con == 1
                self.dev.close()
                self.dev_con = 0
    def Close(self):
        if self.dev_con == 1:
            self.dev.close()  
            self.dev_con == 0
    def Send_Command(self,cmd):
        self.dev.send(bytes(cmd))
    def Recive_Data(self):
        data = self.dev.recv(1024)
        self.input_buffer = repr(data)
        if (self.input_buffer[2:-3] == ">"):
            print("From PLC --> ",self.input_buffer[2:-3])
        elif (self.type == "Digital I/O"):
            print("From PLC --> ",self.input_buffer[3:-3])
            return {"Relay Status":self.input_buffer[3:5],"Digital Input status":self.input_buffer[5:-3]}
        elif (self.type == "Counter Value"):
            print("From PLC --> ",self.input_buffer[5:-3])
            return {"Device":self.input_buffer[3:5],"Digital Input status":self.input_buffer[5:-3]}        
        elif (self.type == "Counter Value"):
            print("From PLC --> ",self.input_buffer[5:-3])
            return {"Device":self.input_buffer[3:5],"Digital Input status":self.input_buffer[5:-3]}       
        #self.dev.close()
    def Relay_control(self,rly):
        self.Connect()
        self.command = [0x40,0x30,0x30,0x31,0x0D]

        if(rly==0):
            self.command[3] = 0x30
        elif (rly==1):
            self.command[3] = 0x31
        elif (rly==2):
            self.command[3] = 0x32
        elif (rly==3):
            self.command[3] = 0x34
        elif (rly==4):
            self.command[3] = 0x38

        elif (rly==12 or rly==21):
            self.command[3] = 0x33
        elif (rly==13 or rly==31):
            self.command[3] = 0x35
        elif (rly==14 or rly==41):
            self.command[3] = 0x39
        elif (rly==23 or rly==32):
            self.command[3] = 0x36
        elif (rly==24 or rly==42):
            self.command[3] = 0x36
        elif (rly==34 or rly==43):
            self.command[3] = 0x43

        elif (rly==123 or rly==132 or rly==213 or rly==231 or rly==321 or rly==312):
            self.command[3] = 0x37

        elif (rly==234 or rly==243 or rly==324 or rly==342 or rly==432 or rly==423):
            self.command[3] = 0x45

        elif (rly==134 or rly==143 or rly==413 or rly==431 or rly==341 or rly==314):
            self.command[3] = 0x44

        elif (rly==124 or rly==142 or rly==412 or rly==421 or rly==241 or rly==214):
            self.command[3] = 0x42

        elif (rly==1234):
            self.command[3] = 0x46
        self.Send_Command(self.command)
        self.type = "Digital I/O"
        self.Recive_Data()
        self.Close()
    def Digital_Input(self):
        self.Connect()
        self.command = [0x40,0x30,0x30,0x0D]
        self.Send_Command(self.command)
        self.ret = self.Recive_Data()
        self.Close()
        return self.ret
    def Counter_Value(self,pin):
        self.type = "Counter Value"
        self.Connect()
        if (pin == 1):
            self.command = [0x20,0x23,0x30,0x30,0x30,0x0D]
        elif (pin == 2):
            self.command = [0x20,0x23,0x30,0x30,0x31,0x0D]
        elif (pin == 3):
            self.command = [0x20,0x23,0x30,0x30,0x32,0x0D]
        elif (pin == 4):
            self.command = [0x20,0x23,0x30,0x30,0x33,0x0D]
        self.Send_Command(self.command)
        self.Close()
        return self.Recive_Data()
    def Reset_Counter(self,counter):
        self.Connect()
        if (counter == 1):
            self.command = [0x20,0x24,0x30,0x30,0x43,0x30,0x0D]
        elif (counter == 2):
            self.command = [0x20,0x24,0x30,0x30,0x43,0x31,0x0D]
        elif (counter == 3):
            self.command = [0x20,0x24,0x30,0x30,0x43,0x32,0x0D]
        elif (counter == 4):
            self.command = [0x20,0x24,0x30,0x30,0x43,0x33,0X0D]
        self.Send_Command(self.command)
        self.Close()
        return self.Recive_Data()
    def Status_Latch(self,pin):
        self.Connect()
        if (pin == 1):
            self.command = [0x20,0x24,0x30,0x30,0x4c,0x30,0X0D]
        elif (pin == 2):
            self.command = [0x20,0x24,0x30,0x30,0x4c,0x31,0X0D]
        elif (pin == 3):
            self.command = [0x20,0x24,0x30,0x30,0x4c,0x32,0X0D]
        elif (pin == 4):
            self.command = [0x20,0x24,0x30,0x30,0x4c,0x33,0X0D]
        self.Send_Command(self.command)
        self.Close()
        return self.Recive_Data()
    def Clear_Latch_Status(self):
        self.Connect()
        self.command = [0X20,0x24,0x30,0x30,0x43,0X0D]
        self.Send_Command(self.command)
        self.ret = self.Recive_Data()
        print(self.ret)
        self.Close()
        return self.ret

# this is the list of actions to do for the regression test
def main():
    #plc_name = PLC(IP Address , Port number)
    demo_room1 = ICP_DAS_PLC("10.0.1.88", 10002)                 # connect to the PLC with the given IP address on the port specified
    demo_room1.Relay_control(1234)                               # read relay ports of the PLC
    for z in range(0,5):                                         # relays 0-4
        demo_room1.Relay_control(z)    
    relays_list = [12,21,13,31,14,41,24,42,34,43,123,132,213,231,321,312,234,243,324,342,432,423,134,143,413,431,341,314,124,142,412,421,241,214]
    for r in relays_list:
        demo_room1.Relay_control(r)     
    demo_room1.Digital_Input()                                   # Get digital input of PLC
    for c in range(1,5):
        demo_room1.Counter_Value(c)                              # Get counter value of digital input 1-4 
        demo_room1.Reset_Counter(c)                              # Reset the counter 1-4 value
        demo_room1.Status_Latch(c)                               # Get latch status of pin 1-4
        demo_room1.Clear_Latch_Status()                          # C lears latch status 

if __name__ == '__main__':  
    main()

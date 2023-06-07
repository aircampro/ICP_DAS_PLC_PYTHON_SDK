# ICP DAS PLC Python SDK
This is a Repository to add support of python to ICP DAS PLC(Programable Logic Controller). 

# Sample Code Example
<ol>
  <li>
    Connecting to the PLC -->
    <code>Room = PLC(IP_Address,Port_number)</code> 
  </li>
  <li>
    Turns on Relay's 1,2,3 -->
  <code>Room.Relay_control(123)</code> 
  </li>
  
  <li>
    Get digital input from PLC -->
  <code>Room.Digital_imput()</code> 
  </li>
  
  
  <li>
    Get digital input 1 counter value form PLC -->
  <code>Room.Counter_Value(1)</code> 
  </li>
  
  
  <li>
    Resets the Counter 1 value to 0 -->
  <code>Room.Reset_Counter(1)</code> 
  </li>
  
  
  <li>
    Gets Latch status of pin 1 -->
  <code>Room.Status_Latch(1)</code> 
  </li>
  
  
  <li>
    Clears Latch status -->
  <code>Room.Clear_Latch_Status()</code> 
  </li>
  
</ol>

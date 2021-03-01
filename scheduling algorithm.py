
class inputs:
 def __init__(self,n):
  self.processName = [0] * n
  self.arrivalTime = [] * n
  self.testat = [0] * n
  self.burstTime = [] * n
  self.testbt = [0] * n
  self.completionTime = [0] * n
  self.turnAroundTime = [0] * n
  self.waitingTime = [0] * n
  self.priority = [] * n
 
 def getInput(self,option):
  for i in range(n):
   print("\n")
   txt = "Process {} : "
   print(txt.format(i+1))
   process = input(" input the process : ")
   self.processName[i] = process
   at = int(input(" input the arrival time : "))
   self.arrivalTime.append([at,i])
   self.testat[i] = at
   bt = int(input(" input the burst time : "))
   self.burstTime.append([bt,i])
   self.testbt[i] = bt
   if option == 3 or option == 4:                                                                     # 3 for priority_nonprem  4 fro priority_prem
    p = int(input(" input the priority of the process : "))  
    self.priority.append([p,i])                                         



class FCFS(inputs):

 def getCompletionTime(self):
  self.arrivalTime.sort()
  time = self.arrivalTime[0][0]
  for i in range(n):
   index = self.arrivalTime[i][1]
   if self.arrivalTime[i][0] > time: time = self.arrivalTime[i][0] + self.burstTime[index][0]
   else: time += self.burstTime[index][0]
   self.completionTime[index] = time
 
 
 def getTurnAroundTime(self):
  for i in range(n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]
 
 def printFcfs(self):
  print("\n")
  print(" Process  arrivalTime  burstTime  completionTime  turnAroundTime  waitingTime")
  for x in range(n):
   txt = "    {}          {}           {}            {}             {}              {} "
   print(txt.format(self.processName[x],self.testat[x],self.testbt[x],self.completionTime[x],self.turnAroundTime[x],self.waitingTime[x]))
  print("\n Average TurnAround Time : " + str(sum(self.turnAroundTime)/n))
  print(" Average Waiting Time : " + str(sum(self.waitingTime)/n))




class RR(inputs):

 def getCompletionTime(self,tq):
  self.arrivalTime.sort()
  time = self.arrivalTime[0][0]
  while time  != (self.arrivalTime[0][0] + sum(self.testbt)):
   for i in range(n):
    index = self.arrivalTime[i][1]
    if self.burstTime[index][0] <= tq and self.burstTime[index][0] > 0:
     time += self.burstTime[index][0]
     self.completionTime[index] = time
     self.burstTime[index][0] = 0 
    elif self.burstTime[index][0] > tq:
     self.burstTime[index][0] -= tq
     time += tq

   
 
 
 def getTurnAroundTime(self):
  for i in range(n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]
 
 def printRr(self):
  print("\n")
  print(" Process  arrivalTime  burstTime  completionTime  turnAroundTime  waitingTime")
  for x in range(n):
   txt = "    {}          {}           {}            {}             {}              {} "
   print(txt.format(self.processName[x],self.testat[x],self.testbt[x],self.completionTime[x],self.turnAroundTime[x],self.waitingTime[x]))
  print("\n Average TurnAround Time : " + str(sum(self.turnAroundTime)/n))
  print(" Average Waiting Time : " + str(sum(self.waitingTime)/n))






class priority_nonprem(inputs):

 
 def getCompletionTime(self):
  self.arrivalTime.sort() 
  self.priority.sort()
  time =  self.arrivalTime[0][0]
  while time != (self.arrivalTime[0][0] + sum(self.testbt)):
   for i in range(n):
    index = self.priority[i][1]
    if self.burstTime[index][0] != 0 and self.testat[index] <= time:
     time += self.burstTime[index][0]
     self.burstTime[index][0] = 0
     self.completionTime[index] = time
     break





 def getTurnAroundTime(self):
  for i in range(n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]
 
 def printPnp(self):
  print("\n")
  print(" Process  arrivalTime  burstTime  completionTime  turnAroundTime  waitingTime")
  for x in range(n):
   txt = "    {}          {}           {}            {}             {}              {} "
   print(txt.format(self.processName[x],self.testat[x],self.testbt[x],self.completionTime[x],self.turnAroundTime[x],self.waitingTime[x]))
  print("\n Average TurnAround Time : " + str(sum(self.turnAroundTime)/n))
  print(" Average Waiting Time : " + str(sum(self.waitingTime)/n))





class priority_prem(inputs):

 def getCompletionTime(self):
  self.arrivalTime.sort()
  self.priority.sort()
  time = self.arrivalTime[0][0]
  while time != (self.arrivalTime[0][0] + sum(self.testbt)):
   for i in range(n):
    index = self.priority[i][1]
    if self.burstTime[index][0] != 0 and self.testat[index] <= time:
     self.burstTime[index][0] -= 1
     time += 1
     if self.burstTime[index][0] == 0: self.completionTime[index] = time
     break
  


 def getTurnAroundTime(self):
  for i in range(n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]
 
 def printPp(self):
  print("\n")
  print(" Process  arrivalTime  burstTime  completionTime  turnAroundTime  waitingTime")
  for x in range(n):
   txt = "    {}          {}           {}            {}             {}              {} "
   print(txt.format(self.processName[x],self.testat[x],self.testbt[x],self.completionTime[x],self.turnAroundTime[x],self.waitingTime[x]))
  print("\n Average TurnAround Time : " + str(sum(self.turnAroundTime)/n))
  print(" Average Waiting Time : " + str(sum(self.waitingTime)/n))

 




class SJF(inputs):


 def getCompletionTime(self):
  self.arrivalTime.sort()
  self.burstTime.sort()
  time = self.arrivalTime[0][0]
  while time != self.arrivalTime[0][0] + sum(self.testbt):
   for i in range(n):
    index = self.burstTime[i][1]
    if self.burstTime[i][0] != 0 and self.testat[index] <= time:
     time += self.burstTime[i][0]
     self.burstTime[i][0] = 0
     self.completionTime[index] = time
     break



 def getTurnAroundTime(self):
  for i in range(n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]
 
 def printSjf(self):
  print("\n")
  print(" Process  arrivalTime  burstTime  completionTime  turnAroundTime  waitingTime")
  for x in range(n):
   txt = "    {}          {}           {}            {}             {}              {} "
   print(txt.format(self.processName[x],self.testat[x],self.testbt[x],self.completionTime[x],self.turnAroundTime[x],self.waitingTime[x]))
  print("\n Average TurnAround Time : " + str(sum(self.turnAroundTime)/n))
  print(" Average Waiting Time : " + str(sum(self.waitingTime)/n))




class SRTF(inputs):

 

 def getCompletionTime(self):
  self.arrivalTime.sort()
  self.burstTime.sort()
  time = self.arrivalTime[0][0]
  while time != (self.arrivalTime[0][0] + sum(self.testbt)):
   for i in range(n):
    index = self.burstTime[i][1]
    if self.burstTime[i][0] > 0  and self.testat[index] <= time:
     self.burstTime[i][0] -= 1
     time += 1
     self.burstTime.sort()
     if self.burstTime[i][0] == 0: self.completionTime[index] = time
     break




 def getTurnAroundTime(self):
  for i in range(n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]
 
 def printSrtf(self):
  print("\n")
  print(" Process  arrivalTime  burstTime  completionTime  turnAroundTime  waitingTime")
  for x in range(n):
   txt = "    {}          {}           {}            {}             {}              {} "
   print(txt.format(self.processName[x],self.testat[x],self.testbt[x],self.completionTime[x],self.turnAroundTime[x],self.waitingTime[x]))
  print("\n Average TurnAround Time : " + str(sum(self.turnAroundTime)/n))
  print(" Average Waiting Time : " + str(sum(self.waitingTime)/n))




# driver's code



while(1):



 print(" \nChoose the option for Algorithm to be followed  \n\n")
 
 print(" ***************** MENU *****************\n")
 print(" Option                         Algorithm")
 print("   1.                              FCFS  ")
 print("   2.                               RR   ")
 print("   3.                     Non Preemptive Priority ")
 print("   4.                        Preemptive Priority ")
 print("   5.                               SJF  ")
 print("   6.                              SRTF  ")
 print("   0.                              exit  ")


 option = int(input(" \noption : "))

 n = int(input(" \ninput the number of processes : "))
 input1 = inputs(n)

 if option == 0 :
  print("\n you exited the program! ")
  break


 if option == 1 :
  fcfs = FCFS(n)
  fcfs.getInput(option)
  fcfs.getCompletionTime()
  fcfs.getTurnAroundTime()
  fcfs.getWaitingTime()
  fcfs.printFcfs()

 if option == 2 :
  rr = RR(n)
  tq = int(input(" input the time quantum : "))
  rr.getInput(option)
  rr.getCompletionTime(tq)
  rr.getTurnAroundTime()
  rr.getWaitingTime()
  rr.printRr()

 if option == 3 :
  print(" \nNote : While entering priority assume lower the number higher the priority ")
  pnp = priority_nonprem(n)
  pnp.getInput(option)
  pnp.getCompletionTime()
  pnp.getTurnAroundTime()
  pnp.getWaitingTime()
  pnp.printPnp()

 if option == 4 :
  print(" \nNote : While entering priority assume lower the number higher the priority ")
  pp = priority_prem(n)
  pp.getInput(option)
  pp.getCompletionTime()
  pp.getTurnAroundTime()
  pp.getWaitingTime()
  pp.printPp()


 if option == 5 :
  sjf = SJF(n)
  sjf.getInput(option)
  sjf.getCompletionTime()
  sjf.getTurnAroundTime()
  sjf.getWaitingTime()
  sjf.printSjf()


 if option == 6 :
  srtf = SRTF(n)
  srtf.getInput(option)
  srtf.getCompletionTime()
  srtf.getTurnAroundTime()
  srtf.getWaitingTime()
  srtf.printSrtf()







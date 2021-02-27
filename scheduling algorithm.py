
class inputs:
 def __init__(self,n):
  self.processName = [0] * n
  self.arrivalTime = [] * n
  self.testat = [0] * n
  self.brustTime = [] * n
  self.testbt = [0] * n
  self.completionTime = [0] * n
  self.turnAroundTime = [0] * n
  self.waitingTime = [0] * n
  self.priority = [] * n
 
 def getInput(self,option):
  for i in range(n):
   print("\n")
   txt = "Process {} : "
   print(txt.format(i))
   process = input(" input the process : ")
   self.processName[i] = process
   at = int(input(" input the arrival time : "))
   self.arrivalTime.append([at,i])
   self.testat[i] = at
   bt = int(input(" input the brust time : "))
   self.brustTime.append([bt,i])
   self.testbt[i] = bt
   if option == 3:                                                                     # 3 for priority_prem
    p = int(input(" input the priority of the process : "))  
    self.priority.append([p,i])                                         



class FCFS(inputs):

 def getCompletionTime(self):
  self.arrivalTime.sort()
  time = self.arrivalTime[0][0]
  for i in range(n):
   index = self.arrivalTime[i][1]
   if self.arrivalTime[i][0] > time: time = self.arrivalTime[i][0] + self.brustTime[index][0]
   else: time += self.brustTime[index][0]
   self.completionTime[index] = time
 
 
 def getTurnAroundTime(self):
  for i in range(n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]
 
 def printFcfs(self):
  print("\n")
  print(" Process  arrivalTime  brustTime  completionTime  turnAroundTime  waitingTime")
  for x in range(n):
   txt = "    {}          {}           {}            {}             {}              {} "
   print(txt.format(self.processName[x],self.testat[x],self.testbt[x],self.completionTime[x],self.turnAroundTime[x],self.waitingTime[x]))




class RR(inputs):

 def getCompletionTime(self,tq):
  self.arrivalTime.sort()
  time = self.arrivalTime[0][0]
  while time  != (self.arrivalTime[0][0] + sum(self.testbt)):
   for i in range(n):
    index = self.arrivalTime[i][1]
    if self.brustTime[index][0] <= tq and self.brustTime[index][0] > 0:
     time += self.brustTime[index][0]
     self.completionTime[index] = time
     self.brustTime[index][0] = 0 
    elif self.brustTime[index][0] > tq:
     self.brustTime[index][0] -= tq
     time += tq

   
 
 
 def getTurnAroundTime(self):
  for i in range(n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]
 
 def printRr(self):
  print("\n")
  print(" Process  arrivalTime  brustTime  completionTime  turnAroundTime  waitingTime")
  for x in range(n):
   txt = "    {}          {}           {}            {}             {}              {} "
   print(txt.format(self.processName[x],self.testat[x],self.testbt[x],self.completionTime[x],self.turnAroundTime[x],self.waitingTime[x]))



class priority_prem(inputs):

 
 def getCompletionTime(self): 
  self.priority.sort()
  index = self.priority[0][1]
  time =  self.testat[index]
  for i in range(n):
   index = self.priority[i][1]
   if self.arrivalTime[index][0] > time: time = self.arrivalTime[index][0] + self.brustTime[index][0]
   else: time += self.brustTime[index][0]
   self.completionTime[index] = time





 def getTurnAroundTime(self):
  for i in range(n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]
 
 def printpP(self):
  print("\n")
  print(" Process  arrivalTime  brustTime  completionTime  turnAroundTime  waitingTime")
  for x in range(n):
   txt = "    {}          {}           {}            {}             {}              {} "
   print(txt.format(self.processName[x],self.testat[x],self.testbt[x],self.completionTime[x],self.turnAroundTime[x],self.waitingTime[x]))


# driver's code


n = int(input(" input the number of processes : "))

input1 = inputs(n)

pp = priority_prem(n)
pp.getInput(3)
pp.getCompletionTime()
pp.getTurnAroundTime()
pp.getWaitingTime()
pp.printpP()


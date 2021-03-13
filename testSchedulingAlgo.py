startTime = []
length = []



class inputs:
 def __init__(self,n):
  self.n = n
  self.processName = [0] * self.n
  self.arrivalTime = [] * self.n
  self.testat = [0] * self.n
  self.burstTime = [] * self.n
  self.testbt = [0] * self.n
  self.completionTime = [0] * self.n
  self.turnAroundTime = [0] * self.n
  self.waitingTime = [0] * self.n
  self.priority = [] * self.n

class FCFS(inputs):

 def getCompletionTime(self):
  self.arrivalTime.sort()
  time = self.arrivalTime[0][0]
  for i in range(self.n):
   index = self.arrivalTime[i][1]
   if self.arrivalTime[i][0] > time:
        time = self.arrivalTime[i][0] + self.testbt[index]
        startTime.append([index,self.arrivalTime[i][0]])
        length.append([index,self.testbt[index]])
   else:
        startTime.append([index,time])
        time += self.testbt[index]
        length.append([index,self.testbt[index]])
   self.completionTime[index] = time
 
 
 def getTurnAroundTime(self):
  for i in range(self.n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(self.n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.burstTime[i][0]

 
class RR(inputs):

 def getCompletionTime(self,tq):
  self.arrivalTime.sort()
  time = self.arrivalTime[0][0]
  queue =  []
  k = 0
  #print(queue)
  index = self.arrivalTime[0][1]
  #print("index : " + str(index))
  queue.append(index)
  while len(queue)!=0:
   #print("len : " + str(len(queue)))
   index = queue.pop(0)
   #print("index : " + str(index))
   if self.testbt[index] <= tq and self.testbt[index] > 0 and time >= self.testat[index]:
    time += self.testbt[index]
    #print("time : " + str(time))
    self.completionTime[index] = time
    #print("completionTime of " + str(index) + " is " + str(time))
    self.testbt[index] = 0 
   elif self.testbt[index] > tq and time >= self.testat[index]:
    self.testbt[index] -= tq
    time += tq
    #print(time)
   j = k + 1
   while j < self.n:
    z = self.arrivalTime[j][1]
    if self.testat[z] <= time and self.testbt[z] > 0 and z not in queue: queue.append(z)
    j += 1
   if self.testbt[index] > 0 and index not in queue: queue.append(index)
   k += 1
   #print(queue)


 def getTurnAroundTime(self):
  for i in range(self.n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(self.n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.burstTime[i][0]
 





class priority_nonprem(inputs):

 
 def getCompletionTime(self):
  self.arrivalTime.sort() 
  self.priority.sort()
  time =  self.arrivalTime[0][0]
  sums =  self.arrivalTime[0][0] + sum(self.testbt)
  while time != (sums):
   for i in range(self.n):
    index = self.priority[i][1]
    if self.testbt[index] != 0 and self.testat[index] <= time:
     time += self.testbt[index]
     self.testbt[index] = 0
     self.completionTime[index] = time
     break


 def getTurnAroundTime(self):
  for i in range(self.n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(self.n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.burstTime[i][0]






class priority_prem(inputs):

 def getCompletionTime(self):
  self.arrivalTime.sort()
  self.priority.sort()
  time = self.arrivalTime[0][0]
  sums =  self.arrivalTime[0][0] + sum(self.testbt)
  while time != (sums):
   for i in range(self.n):
    index = self.priority[i][1]
    if self.testbt[index] != 0 and self.testat[index] <= time:
     self.testbt[index] -= 1
     time += 1
     if self.testbt[index]  == 0: self.completionTime[index] = time
     break
  


 def getTurnAroundTime(self):
  for i in range(self.n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(self.n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.burstTime[i][0]
 
 




class SJF(inputs):


 def getCompletionTime(self):
  self.arrivalTime.sort()
  self.burstTime.sort()
  time = self.arrivalTime[0][0]
  while time != self.arrivalTime[0][0] + sum(self.testbt):
   for i in range(self.n):
    index = self.burstTime[i][1]
    if self.burstTime[i][0] != 0 and self.testat[index] <= time:
     time += self.burstTime[i][0]
     self.burstTime[i][0] = 0
     self.completionTime[index] = time
     break



 def getTurnAroundTime(self):
  for i in range(self.n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(self.n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]
 




class SRTF(inputs):

 

 def getCompletionTime(self):
  self.arrivalTime.sort()
  self.burstTime.sort()
  time = self.arrivalTime[0][0]
  while time != (self.arrivalTime[0][0] + sum(self.testbt)):
   for i in range(self.n):
    index = self.burstTime[i][1]
    if self.burstTime[i][0] > 0  and self.testat[index] <= time:
     self.burstTime[i][0] -= 1
     time += 1
     self.burstTime.sort()
     if self.burstTime[i][0] == 0: self.completionTime[index] = time
     break




 def getTurnAroundTime(self):
  for i in range(self.n):
    self.turnAroundTime[i] = self.completionTime[i] - self.testat[i]
 
 def getWaitingTime(self):
  for i in range(self.n):
    self.waitingTime[i] = self.turnAroundTime[i] - self.testbt[i]
 


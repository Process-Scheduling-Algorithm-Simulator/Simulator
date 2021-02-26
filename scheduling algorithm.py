
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
 
 def getInput(self):
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



class FCFS(inputs):

 def getCompletionTime(self):
  self.arrivalTime.sort()
  print(self.arrivalTime)
  time = 0
  for i in range(n):
   index = self.arrivalTime[i][1]
   print(index)
   time += self.brustTime[0][index]
   print(time)
   self.completionTime[index] = time
  print(self.completionTime) 
 
 
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













# driver's code


n = int(input(" input the number of processes : "))

input1 = inputs(n)

fcfs = FCFS(n)
fcfs.getInput()
fcfs.getCompletionTime()
fcfs.getTurnAroundTime()
fcfs.getWaitingTime()
fcfs.printFcfs()


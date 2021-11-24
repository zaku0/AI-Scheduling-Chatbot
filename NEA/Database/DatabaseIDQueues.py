import random
class ID_Queue():
  digits = [0,1,2,3,4,5,6,7,8,9]
  usedIDs = []
  def __init__(self):
    self.Queue = []
    self.Rear = -1
    self.queueSize = 10
    self.IDsize = 7
    for Count in range(self.queueSize-1):
      self.Add(self.IDsize,[])

  def IsEmpty(self):
    if self.Rear == -1:
      return True
    else:
      return False

  def Add(self,size,ID):
    if size < 1:
        join = lambda nums: int(''.join(str(i) for i in nums))
        myID = join(ID)
        checkUnique = self.CheckQueueID(myID)
        if checkUnique == 0:
            self.Queue.append(myID)
        return myID
    else:
        ID.append(random.choice(ID_Queue.digits))
        self.Add(size-1,ID)

  def getID(self):
      self.Add(self.IDsize,[])
      ID_Queue.usedIDs.append(self.Queue[0])
      return self.Queue.pop(0)

  def CheckQueueID(self,ID):
    if ID in self.Queue or ID in ID_Queue.usedIDs:
        return -1
    return 0

  def getQueue(self):
      return self.Queue

pattern_ID = ID_Queue()
response_ID = ID_Queue()
context_ID = ID_Queue()

class LiftSim(object):

    def __init__(self,queues, capacity):
        self.queues=queues
        self.capacity=capacity
        
    def theLift(self):
        queues=[list(i) for i in self.queues]
        target=[]
        path=[0]
        ground=0
        topFloor=len(queues)      
        direction=1           # 1 is going UP and -1 is going DOWN
        people=0
        capac=self.capacity
    
        while queues.count([])!=len(queues) or len(target)!=0:  #check if there's people queueing
            for i in range(ground, topFloor, direction):
                while i in target:
                    people-=1
                    if i!= path[-1]:         #check if there's multiple people going to the same floor
                        path.append(i)
                    target.remove(i)
                if queues[i]:
                    for j in queues[i][:]:
                        if (j>i and direction+1) or (not direction+1 and j<i): #check if lift is going in the direction of target
                            if people<capac:
                                queues[i].remove(j)    #people go into lift
                                target.append(j)       #target floors
                                people+=1
                                if i!=path[-1]:        
                                    path.append(i)      #stops at floor to pick up people
                            elif people>=capac:
                                if i!=path[-1]:
                                    path.append(i)
            direction *=-1
            ground,topFloor=topFloor+direction,ground+direction   #Lift changes direction
        if path[-1]!=0:
                return path+[0]
        else:
            return path

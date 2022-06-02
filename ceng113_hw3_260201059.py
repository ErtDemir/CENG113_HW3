def addAFriend(person,newFriend,friendships):
    friendships[person].append(newFriend)
    friendships[newFriend].append(person)
def removeAFriend(person,oldFriend,friendships):
    friendships[person].remove(oldFriend)
    friendships[oldFriend].remove(person)
def addAUser(person,friendships):
    friendships[person]=[]
def deleteAUser(person,friendships):
    del friendships[person]
    for (i,j) in friendships.items():
        if person in j:
            j.remove(person)

def offerAFriend(person,friendships):
    calculations = {}
    #Calculation Number of Mutual Friends
    counts = []
    totalCounts = []
    for key in friendships.keys():
        eliminatedUser = []
        otherUser = []
        eliminatedUser = friendships[key][:]
        eliminatedUser.append(key)
        for i in friendships.keys():
            if  i not in eliminatedUser:
                otherUser.append(i)
        #First Calculation Max Min
        for j in otherUser:
            for k in friendships[j]:
                count = 0
                for l in friendships[key]:
                    if l is k:
                        count +=1
                counts.append(count)
            #Second Calculation Max Min
                totalCount = count/(len(set(friendships[key]+friendships[j])))
                totalCounts.append(totalCount)
    counts.sort()
    totalCounts.sort()
    firstMin = counts[0]
    firstMax = counts[-1]
    secondMin = totalCounts[0]
    secondMax = totalCounts[-1]
    #x_scale calculation for person
    closeFriends = []
    mutualFriends = []
    scales = []
    for friends in friendships[person]:
        closeFriends.append(friends)
    for users in friendships.keys():
        if users != person and users not in closeFriends:
            mutualFriends.append(users)
            countmutualFriend = 0
            totalFriends = len(set(friendships[person]+friendships[users]))
            for usersFriends in friendships[users]:
                if usersFriends in friendships[person]:   
                    countmutualFriend += 1
            #Scale Calculation
            if firstMax != firstMin:    
                firstScale = ( countmutualFriend - firstMin ) / ( firstMax - firstMin )
                secondScale = (( countmutualFriend/totalFriends) - secondMin) / ( secondMax - secondMin)
                averageScale = (firstScale+secondScale) / 2 
                calculations[users] = averageScale
                scales.append(averageScale)
                lock = 1
            else:
                randomfriend = []
                for b in friendships.keys():
                    if b not in friendships[person]:
                        randomfriend.append(b)
                lock = 0
    if lock == 1:
        scales.sort()
        #Offer A Friend
        possibleNewFriend = None
        for cal in calculations.keys():
            if calculations[cal] == scales[-1] :
                possibleNewFriend = cal
    elif lock == 0:
        possibleNewFriend = randomfriend[0]
    #print(firstScale,"\n",secondScale,"\n",averageScale,"\n")
    return possibleNewFriend
    
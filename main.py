
global userdict
userdict= {}
'''this is the dictionary where we store all the users&artists that are from file'''

def seeusers(filename):
    '''@author: Changmin Lee'''
    '''it adds the past user records about their preferences to the userdict'''
    with open(filename, "r") as f:
        for line in f:
            [user, singers]=line.strip().split(':')
            singerlist=singers.strip().split(',')
            userdict[user]= singerlist
      
def getpreference():
    '''@author: Changmin Lee'''
    '''Asks for the preference of the person. '''
    singer=[]
    a='start'
    while a != "":
        a= input("Enter an artist that you like (Enter to finish:")
        singer.append(a.title().strip())
    singer.sort()
    return singer

def rmv(L1, L2):
      '''@author: Bhagawat Chapagain'''
      '''Return a new list that contains only the elements in
      L2 NOT in L1. '''
      L3 = []
      for i in L2:
        if i in L1 == False:
            L3 += [i]
      return L3
def getRecommendations(currentUser, preferences, userData):
    '''@author: Bhagawat Chapagain'''
    '''Determine which user (or users) have tastes most similar to yours. Choose and rank artists that the similar user likes. These are your recommendations.'''
    
    bestUser = findBestUser(currentUser, preferences, userData)
    recommendations = rmv(preferences, userData[bestUser])
  
    return recommendations
def findBestUser(currentUser, preferences, userData):
    '''@author: Bhagawat Chapagain'''
    '''Returns  user with conjugate music preferences to the current User'''
    def numMatches( L1, L2 ):
      '''@author: Bhagawat Chapagain'''
      '''return the number of elements that match between
        two sorted lists '''
      same = 0
      for i in L1:
        if i in L2:
          same += 1
      return same
    users = list(userData.keys())
    bestScore = -1
    bestMatch = None
    for user in users:
        score = numMatches(preferences, userData[user])
        if preferences not in userData[user]:
            if bestScore < score:
                bestScore = numMatches(preferences, userData[user])
                bestMatch = user
    return bestMatch
def mostPopularArtist(userdict):
  '''@author: Kevin Pulickal'''
  '''get most popular artist: returns tuple: (likes, [artist1, artist2, etc.]'''
    
  preferences  = []

  for usr in userdict:
      preferences  += userdict[usr]
  preferences  = sorted(preferences)

  rankings = {} 
  artist_0 = ""
  for artist in preferences:
      if artist != artist_0:
          artist_0 = artist
          rankings[artist] = 0
      rankings[artist] = rankings[artist] + 1


  popularityList = []
  likes = 0
  for artist in rankings:
      if rankings[artist] > likes:
          popularityList = [artist]
          likes = rankings[artist]
      elif rankings[artist] == likes:
          popularityList.append(artist)
  popularityList = sorted(set(popularityList))
  return (likes, popularityList)
        
      
def printMostPopularArtist():
    '''@author: Kevin Pulickal'''
    '''output most popular artist'''
    for artist in getMostPopularArtist()[1]:
        print(artist)


def howPopular():
    '''@author: Kevin Pulickal'''
    '''How popular is the most popular artists (subs)'''
    print(mostPopularArtist()[0])

def mostLikes(userdict):
    '''@author: Bhagawat Chapagain'''
    '''Gives the user with the most likes if they are not private (...$)'''
    j = 0
    for User in userdict:
        if User[-1] != '$':
            if len(userdict[User]) > j:
                j = len(userdict[user])
                i = user
    return i
def savepreference(filename):
    myfile= open(filename, "w")
    for name in userdict:
        pref=userdict[name]
        myfile.write(name.strip()+':')
        for i in range(len(pref)):
            myfile.write(pref[i])
            if i <len(pref)-1 and i>0:
                myfile.write(',')
        myfile.write('\n')
    myfile.close()
    

def main():
    seeusers("musicrecplus.text")
    name=input("Enter your name ( put a $ symbol after your name if you wish your preferences to remain private ):")
    if name not in userdict:
        pref= getpreference()
        userdict[name]=pref
    option=''
    while alpha != 'q':
        print('Enter a letter to choose an option:'+'\n'+'e - Enter preferences'+'\n'+'r - Get recommendations'+'\n'+'p - Show most popular artists'+
              '/n'+'h - How popular is the most popular'+'\n'+'m- Which user has the most likes'+'\n'+'q - Save and quit'+'\n')
        option=input()
        if option == 'e':
            pref= getpreference()
            userdict[name]=pref
        if option == 'r':
          getRecommendations(name,pref, userdict)
        if option == 'p': mostPopularArtist()
        if option == 'h':
          return 0
        if option == 'm':
          findBestUser(name, pref, userdict)
    savepreference(filename)     


main()


import matplotlib
from matplotlib import pyplot as plt

class Series:
    def __init__(self, omdb, imdbid):
        self.omdb = omdb
        self.imdbid = imdbid
        self.outerObject = getShowIMDBID(omdb, imdbid) # JSON object for whole show
        self.totalSeasons = int(self.outerObject.get("total_seasons", ""))
        self.episodeDict = self.fillEpisodeDict() # Holds episode information [season, ep, epTitle, totalEp, rating]
        self.x = [] # Holds total episode number
        self.y = [] # Holds episode rating 
        self.fillXandYLists(self.x, self.y) # Fills x and y lists

    def displayPlot(self, x, y, outerObject, episodeDict):
        title = outerObject.get("title", "") # Holds title of the series
        plt.ylim(1, 10) # Sets y range shown for displaying ratings 
        plt.plot(x,y, marker="o", markersize=2) # Plots graph and sets marker on each 'point'
        plt.title(title + ' Ratings')
        plt.ylabel('IMDB Ratings')
        plt.xlabel('Episodes')
        placeAnnotations(x, y, episodeDict) # Adds annotations for highest/lowest ranking episodes
        plt.show()

    # Fills x and y lists which hold data to be displayed 
    def fillXandYLists(self, x, y):
        # Iterates through all episodes
        for num in range(1, len(self.episodeDict) + 1):
            x.append(self.episodeDict[num][3])
            y.append(self.episodeDict[num][4])

    # Returns episode dict in form of {[season, episode, epTitle, totalEp], ...}
    def fillEpisodeDict(self):
        iterVal = 1
        tmpDict = {}
        # For each season in show
        for number in range(1, self.totalSeasons + 1):
            tmpSeason = self.omdb.get(imdbid=self.imdbid, season=str(number)) # Json info for season

            # For each episode in the season
            for num in range(1, (len(tmpSeason.get("episodes", "")) + 1)):
                tmpEpisode = self.omdb.get(imdbid=self.imdbid, season=str(number), episode=str(num)) # Json info for episode

                rating = tmpEpisode.get("imdb_rating", "") # Get rating

                # If rating isn't convertable, don't include episode
                if isFloat(rating):
                    rating = float(rating) # Convert rating to float
                else:
                    continue

                # Dict will contain values in order of [season, episode, title]
                epTitle = tmpEpisode.get("title", "") # Get episode title
                tmpDict[iterVal] = [number, num, epTitle, iterVal, rating] # Add episode to episodeDict dictionary
                iterVal += 1 # Iterate to next episode
        return tmpDict

    # Returns JSON object for whole show
    def getOuterObject(self):
        return self.outerObject
    
    # Returns number of seasons
    def getSeasonCount(self):
        return self.totalSeasons

   # Returns episodeDict holding all episode information 
    def getEpisodeDict(self):
        return self.episodeDict

    # Returns x[] list holding episode numbers 
    def getX(self):
        return self.x
    
    # Returns y[] list holding episode rankings
    def getY(self):
        return self.y


#--------------------------------------------------------------------------------

# Set up API Key with OMDB
def omdbSetup(omdb, apikey):
    omdb.set_default('apikey', str(apikey))

# Get show JSON object by IMDB id
def getShowIMDBID(omdb, id):
    # get show by IMDB id
    showObject = omdb.imdbid(str(id))
    return showObject # Returns json object

# Pre: Must be called after x values are defined using fillXandYLists()
# Returns the index of the lowest ranking show in a series
def lowestRatingIndex(x):
    bottomRating = x[0] # Initialize lowest rating value to first episode
    currentIndex = 0 # Tracks current index while iterating through list
    lowestIndex = 0 # Tracks index of lowest rating

    # Iterate through ratings in x list
    for rating in x:
        if rating < bottomRating:
            bottomRating = rating
            lowestIndex = currentIndex
        currentIndex += 1
    
    return lowestIndex

# Pre: Must be called after x values are defined using fillXandYLists()
# Returns the index of the highest ranking show in a series
def highestRatingIndex(x):
    highestRating = x[0] # Initialize highest rating value to first episode
    currentIndex = 0 # Tracks current index while iterating through list
    highestIndex = 0 # Tracks index of highest rating

    # Iterate through ratings in x list
    for rating in x:
        if rating > highestRating:
            highestRating = rating
            highestIndex = currentIndex
        currentIndex += 1
    
    return highestIndex

# Places annotations for episode information
def placeAnnotations(x, y, epDict):
    # Get index of episodes
    lowRankIndex = lowestRatingIndex(y)
    highRankIndex = highestRatingIndex(y)
    # Create annotation text
    lowAnnotation = ("S" + str(epDict[lowRankIndex + 1][0]) + "E" + str(epDict[lowRankIndex + 1][1]) + "\n" + epDict[lowRankIndex + 1][2])
    highAnnotation = ("S" + str(epDict[highRankIndex + 1][0]) + "E" + str(epDict[highRankIndex + 1][1]) + "\n" + epDict[highRankIndex + 1][2])
    # Place annotations
    plt.annotate(lowAnnotation, xy=(x[lowRankIndex], y[lowRankIndex]), xytext=(x[lowRankIndex], y[lowRankIndex] - 0.9), color="orange", size=14)
    plt.annotate(highAnnotation, xy=(x[highRankIndex], y[highRankIndex]), xytext=(x[highRankIndex], y[highRankIndex] + 0.1), color="orange", size=14)

# Checks if value can be converted into a float
def isFloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False
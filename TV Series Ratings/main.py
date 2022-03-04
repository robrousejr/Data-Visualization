import matplotlib
import omdb
from functions import *

omdbSetup(omdb, 'fe9dd617') # Setup API Key

showkey = input("Enter an IMDB Title Code: ")

# Create series object and display Plot
seriesObj = Series(omdb, showkey)

# Displays plot
seriesObj.displayPlot(seriesObj.getX(), seriesObj.getY(), seriesObj.getOuterObject(), seriesObj.getEpisodeDict())

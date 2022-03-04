# TEST FILE ONLY
from functions import *
import matplotlib
from matplotlib import pyplot as plt
import omdb

omdbSetup(omdb, 'fe9dd617') # Setup API Key

# Testing Friends 
Friends = Series(omdb, "tt0108778")
Friends.displayPlot(Friends.getX(), Friends.getY(), Friends.getOuterObject(), Friends.getEpisodeDict())



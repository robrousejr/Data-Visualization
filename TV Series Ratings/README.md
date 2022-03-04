# TV Show Data Visualization
Creation of a chart in which it will display all of the IMDB ratings for each episode of whatever show you would like. It will also display the result in a graph which will point out both the highest and lowest rated episode throughout the entire series.

### Tools Used

1. Matplotlib
2. OMDB

### How to Build Project

**Run these commands:**  
*python -m pip install -U pip  
python -m pip install -U matplotlib  
pip install omdb*  

### How to Use
In *main.py*, 
```
# Create series object and display Plot
seriesObj = Series(omdb, "tt0386676")
```

Edit the second parameter which reads in the IMDB ID of the series to the series you would like to see displayed. 
This can be found through [IMDB's website](www.imdb.com)

**IMPORTANT: THIS CAN ONLY BE USED FOR TV SERIES**

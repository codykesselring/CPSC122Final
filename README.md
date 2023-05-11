CPSC 122 Final <br>
Technical Report<br>
introduction:<br>
I chose my spotify data because I thought it would be interesting to visualize my spotify habits. <br>
The source data is within 4 json files with data from 02/2022 to 02/2023. I include tables of uncleaned and cleaned data including heatmaps, barcharts, and line graphs. <br>
I collected the data by parsing through the source files and searching for specific attributes including time of day and total ms played of a specific artist.<br>
Impacts include greater self awareness as I can see my entire music history of the last year, and at a larger scale, I think companies can use the information to their advantage.<br>
Stakeholders might be interested with this data on a larger scale to know what songs may be marketable for specific audiences.<br>

Data Analysis:<br>
I started by making a list of all my spotify artists with their total playtime in descending order and chartted it. It resulted in a messy chart with way to many elements and was also displayed in milliseconds which are hard to understand. I cleaned it by converting milliseconds to seconds, and within the charts, I only grab a handful of artists instead of the full list.<br>
There was no too much difficulty gathering the data itself, except for having to wait a month to get it... but having the data split amongs 4 files, and intereting the data itself was an issue at the beginning as I misinterpretted what exactly some of the attributes meant in the data.<br>
The data aggregation techniques I used were pivot tables, filtering, and drill-down as many of the charts use months instead of days, for example.<br>
I used many visualization techniques such as bar charts, heat tables, and line graphs to represent the data. The most useful of which were 1) the line graph showing the linear regression of total hours played of music in the last year, 2) comparing how selected artists trendlines were similar, and 3) the heatmap that tells me the average amount I listen to music at a certain time.<br>
I used the t-test statistical hypothesis to see if I listen to music more during a weekday versus a weekend, and found that I do not because my t-test of .11>.05<br>

Classification models were not appropriate for my data set<br>

Conclusion: <br>
My raw data can be seen in the repository under files StreamingHistory(0-3).json, in which I condenensed the information into one dict in each of the programs to easily filter through data and visualize specific attributes. Conclusions I made through visualization and tests were that my playtime has increased since leaving high school, my preferred genre can be seen through my top artists (rap), My mood affects what artists I listen to, and there is no significant difference between the average duration of songs played on weekdays and weekends.<br>
I think that stakeholders in this project could find it very useful to know how to market towards a specific audience knowing their music habits. This specifically could be useful for those who advertise on music platforms, giving companies a greater hold on the audience listening to an ad because they know who what type of person they're looking for.<br>

# Cannabis: Cash Crop or Crime Boom?

Analyzing how crime rates may have been affected by the Legalization of Cannabis

# Inspiration and Goals
This project was inspired by an article I read on Forbes:

https://www.forbes.com/sites/mikeadams/2018/03/28/california-officials-say-marijuana-legalization-causing-more-violent-crime/#357310d62c3b

In summary, the article alleges that criminals are crossing state borders to snatch up all the Cannabis they can and transport it back to their home state.  In particular the author mentions a rise in "home invasions, violent crimes and robberies" perpetrated by people coming in from other states. The goal of my project is to determine if these "Weed Pirates" are having any significant impact on crime rates in regions where Cannabis has been legalized.

# Process
To see the long term effects of legalization I began by finding crime data from cities that had fully legalized as test groups and data from cities that had medical programs as controls.  After digging through several cities I decided to use Seattle as my test and Portland as a control.

This focus of this project is weed piracy, so I decided to look at crime types I associated with piracy: Homicides, Thefts, Robberies, and Burglaries.

In order to make a fair comparison we need to verify that Portland and Seattle had similar crime rates and trends before legalization occured in 2012 (Washington) and late 2014 (Oregon), and see if there was any significant change after.  This was accomplished using a set of hypotheses for testing:

H(null): There is no significant change in violent crime rates coinciding with legalization of Cannabis

H(alt): There is significant change in violent crime rates coinciding with legalization of Cannabis

# Results
   ![alt text](https://github.com/WhimsicalNose03/Final-Project/blob/master/plots/homicide_rates.png)![alt text](https://github.com/WhimsicalNose03/Final-Project/blob/master/plots/theft_rates.png)
![alt text](https://github.com/WhimsicalNose03/Final-Project/blob/master/plots/burglary_rates.png)
![alt text](https://github.com/WhimsicalNose03/Final-Project/blob/master/plots/robbery_rates.png)

(note: crime rates for Portland in 2015 are imputed as average since 2010)

Cannabis became fully legal in Seattle in 2012, and in Portland in late 2014.  The above plots show illustrate a couple of key things:
* Murder rate in both cities appears to have spiked in the year of legalization; however, these increases are not statistically significant due to the low rate overall.
* There is a significant rise on Seattle Burglaries (p = 0.0488) and Thefts (p < .00001) shortly after legalization in 2012, but the same cannot be said of Burglary and Theft in Portland following their legalization event in 2015.   
* There is not enough evidence in the data to support the hypothesis that Weed Pirates are invading and inflating piracy-related crimes, as described in the article above.

# Challenges
The most challenging part of this project was sifting through crime datasets and finding a city that could serve as a viable control against Seattle.  In addition, each city had a slightly different method of data entry, so cleaning followed a similar but different process each set.  Furthermore, my data only covers *reported* crimes - if a crime gets unreported or miscategorized it will affect our analysis.

# Moving Forward
While I found some significant results, there are a few directions I could go to proceed:
   * Identify more control cities to compare against Seattle.
   * Identify different control and test cities more closely associated with the growing process.
   * Dig deeper into the data I have to determine if proximity to dispensaries has an effect on neighborhood crime rates.
   
# Technologies and Libraries Used
* Python
* Numpy
* Pandas
* MatPlotLib
* GitHub

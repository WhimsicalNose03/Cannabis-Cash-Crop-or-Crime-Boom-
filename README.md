# Cannabis: Cash Crop or Crime Boom?

Analyzing how crime rates may have been affected by the Legalization of Cannabis

# Inspiration and Goals
This project was inspired by an article I read on Forbes:

https://www.forbes.com/sites/mikeadams/2018/03/28/california-officials-say-marijuana-legalization-causing-more-violent-crime/#357310d62c3b

In summary, the article alleges that criminals are crossing state borders to snatch up all the Cannabis they can and transport it back to their home state.  In particular the author mentions a rise in "home invasions, violent crimes and robberies" perpetrated by people coming in from other states. The goal of my project is to test these claims of "Weed Pirates" by looking at crime data from Seattle and Portland.

# Process
To observe the immediate effects of legalization I began by finding crime data from cities that had fully legalized as test groups and data from cities that had medical programs as controls.  After digging through several cities I decided to use Seattle as my test and Portland as a control.

This focus of this project is weed piracy, so I decided to look at crime types I associated with piracy: Homicides, Thefts, Robberies, and Burglaries.

I used a One-Tail Z-Test with the following hypotheses to test the articles claims for each crime category:

Critical Value = 0.05, Bonferonni Corrected to 0.00625

H(null): There is no significant rise in violent crime rates coinciding with legalization of Cannabis

H(alt): There is significant rise in violent crime rates coinciding with legalization of Cannabis

# Results
   ![alt text](https://github.com/WhimsicalNose03/Cannabis-Cash-Crop-or-Crime-Boom-/blob/master/homicide_rates.png)![alt text](https://github.com/WhimsicalNose03/Cannabis-Cash-Crop-or-Crime-Boom-/blob/master/theft_rates.png)
![alt text](https://github.com/WhimsicalNose03/Cannabis-Cash-Crop-or-Crime-Boom-/blob/master/burglary_rates.png)
![alt text](https://github.com/WhimsicalNose03/Cannabis-Cash-Crop-or-Crime-Boom-/blob/master/robbery_rates.png)

(note: crime rates for Portland in 2015 are imputed averages from 2010 to 2014)

From our graphs above we actually only get significant results for Burglary in both Seattle (p = 0.00043) and Portland (p < 0.00001).  However, these rates are both going __down__ instead of spiking.  The rest of our observed changes are not statistically significant.

The data does not provide enough evidence to accept our alternate hypothesis.  Rather, the significant decrease in burglaries suggests the opposite of the articles claims.

# Challenges
The most challenging part of this project was sifting through crime datasets and finding a city that could serve as a viable control against Seattle.  In addition, each city had a slightly different method of data entry, so cleaning followed a similar but different process each set.  Furthermore, my data only covers __reported__ crimes - if a crime gets unreported or miscategorized it will affect our analysis.

# Moving Forward
While I found some significant results, there are a few other directions I'd like to explore:
   * Identify more control cities to compare against Seattle.
   * Apply the same process to cities that participate in a different part of the product cycle.
   * Dig deeper into the data I have to determine if proximity to dispensaries has an effect on neighborhood crime rates.
   * Apply clustering to crime data to see if perpetrators were high during arrest.  (Only viable for certain datasets.)
   
# Technologies and Libraries Used
* Python
* Numpy
* Pandas
* MatPlotLib
* GitHub

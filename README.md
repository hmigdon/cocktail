Houston Migdon  
Engineering Python  
Final Project Description  
Spring Semester 2020  

                                                                  Cocktail.py  


When I was brainstorming ideas for a final project, I wanted to create something that would provide value to people stuck in the   
homes all over the world but still want to experience the fun of trying a new cocktail! The way this program is structured is simple,   users are asked to select their base-alcohol preference (i.e. “Vodka”) and from there the program instructs them how to make a random   cocktail using that base. For example, if you select “Tequila”, you may learn how to make a Tequila Sunrise, or the world-famous Paloma!   I think now more than ever, we need to get out of our routines and try new things! Since many people cooped up at home are still   drinking alcohol, I think it is a great idea to encourage people to add new varieties to their standard cocktail choices!  
  
The way I built the program is in tree-like structure where first we get to know if the user drinks alcohol at all. If they do,   
the baseChoice() function is called where the user selects which base-alcohol they prefer. Each base alcohol choice corresponds to  
a different function that is then called (i.e. tequila()). The structure of each alcohol's function is largely similar, as each  
selects a random choice from a list of relevant cocktails and presents that random selection to the user. The use does have the option to  
see another choice if they would prefer something else. Once approved, the program lists the ingrediants and how to serve the cocktail  
and even asks the user if they'd like to see an instructional video on how to make the cocktail. If the user doesn't want to see a video,  
the program thanks them for their time and exits. If the user would like an instructional video for a visual aid, a new default browser  
window is opened and redirects to a unique youtube video on how to make that cocktail. I did this using the python webbrowser api.  
  
 Overall I had a lot of fun creating this prject and I hope you enjoy playing around with it just as much. After you test it,  
 make a cocktail for yourself!

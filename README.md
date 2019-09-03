# NFL-Stats-Library

Django | MySQL | Beautiful Soup (Web Scraping) | HTML | CSS | Python

A Django web app that allows you to browse the NFL stats of all players up until the 2018 season. Users can access individual players 
by team and by individual player search. Users can also analyze and compare stats from a variety of categories, and view the stats of 
all Hall of Fame players.

- All of the data was accumulated using a customized version of Kendall Gillies code from her repo "NFL-Statistics-Scrape"
(https://github.com/kendallgillies/NFL-Statistics-Scrape). I also added a script to scrape the profile picture urls of each 
player from NFL.com (https://github.com/ytrevor81/Profile-Picture-URLs-Scrape).
- Database is MySQL, which is accessed by Django via models.py.
- A library was created to utilize reusable code in data_functions.py. These functions handle most of the data processing when extracted
from the MySQL database.
- Deployed on a Linode VPS server, using Apache2 and Ubuntu.
- Website is www.nfl-stats-library.com

# Home/Full Season Stats
Users can view season stats of players, ranked from greatest to least, from a variety of categories in any given year and/or for any
team.

![nfl-home](https://user-images.githubusercontent.com/46886041/64142778-aba8cb80-ce37-11e9-934f-b00a3fdfb3e0.PNG)

# Active Player Profiles
Each player has a profile page, which lists the player's background information and career stats, highlighting the stats of the most 
recent NFL season in the grey box on the right side of the page. Users have the option to view stats only relevant to the player's 
position or to view all career stats.

![nfl-profile](https://user-images.githubusercontent.com/46886041/64142787-ba8f7e00-ce37-11e9-80b1-421261f13edc.PNG)

# Retired Player Profiles
Each retired player has a profile page as well. This displays all career stats, teams played, background information, and whether or 
not they are in the NFL Hall of Fame.

![nfl-retprofile](https://user-images.githubusercontent.com/46886041/64142789-bebb9b80-ce37-11e9-9016-a9580a7cd0fb.PNG)

# All NFL Teams
Every NFL team, along with their respective divisions, are presented on this page. All links take the user to individual team pages.

![nfl-teams](https://user-images.githubusercontent.com/46886041/64142796-c54a1300-ce37-11e9-908f-5ff02a538da2.PNG)

# Individual Teams

Each team has it's own page, which lists every player who is currently on the team.

![nfl-team](https://user-images.githubusercontent.com/46886041/64142800-ca0ec700-ce37-11e9-8dd7-a9ba5eb67a53.PNG)

# Season Stats Leaders

Displays the top five ranked players of six categories for any given year. These are the six most popular stat categories in the NFL.

![nfl-leaders](https://user-images.githubusercontent.com/46886041/64142804-ced37b00-ce37-11e9-8d52-03bc054e55eb.PNG)

# Player Search

Users can search for any player, whether they are currently active or retired. The "Name" is a case-sensitive search bar that 
can search for any player. 

![nfl-players](https://user-images.githubusercontent.com/46886041/64142809-d2670200-ce37-11e9-9fd2-83ffcfc986f4.PNG)

# Hall of Fame

All players in the NFL Hall of Fame are listed on this page. Each link takes the user to the player's retired profile page.

![nfl-hof](https://user-images.githubusercontent.com/46886041/64142814-d5fa8900-ce37-11e9-82a7-2dd61cd3ac0d.PNG)
















 


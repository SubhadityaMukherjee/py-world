# What it does 

This program basically asks for a search query and then crawls twitter to find all occurences of that term. It then returns a single file with formatted entries containing the username, the tweet itself and the date-time string.

# How to use it
- Make sure you have python3+
- Open terminal/bash
- cd to the main directory
- pip install -r requirements.txt
- run the query 
                    scrapy crawl TweetScraper -a query="<give any query without the brackets>"
- run "Beautify_this_rn_bro.py"
- Check the generated file : "All_data.txt"


# Acknowledgement #
Keeping the crawler up to date requires continuous efforts, we thank all the [contributors](https://github.com/jonbakerfish/TweetScraper/graphs/contributors) for their valuable work.

Most of the code can be found by doing a 
git clone https://github.com/jonbakerfish/TweetScraper.git

# What is different from the original?
- Changed the code to work with python 3+
- Added my own script to give a single text file from the list of files
- Added a few other things I dont remember now

# Fuller Disclosure

## Description

This project is the culmination of work I did for my computer science senior project this past spring. For a more thorough description of the project, see [this repo](https://github.com/lswainemoore/conflicts_of_interest). 

This repo contains the code for a twitter bot, operating for now with the handle [@FullerDisclosur](https://twitter.com/FullerDisclosur) (thanks to Twitter character limits), that uses the modeling work from my senior project to evaluate whether a given tweet (retweets or originals) from a member of Congress discuss industries from which that member has received significant amounts of money. The bot flags any tweets which do exhibit these conflicts of interest in its own timeline.

## Disclaimer

In the spirit of escaping perfectionism (and because I'm starting a new job tomorrow, and will be short on time for a while), I'm publishing this project a little before it's ready. The model is one that I trained in the spring, and could use more work. This means that there will be false positives (i.e. non-conflicts of interests that are flagged), and there will certainly be many false negatives, because I have set the threshold fairly high. In fact, the bot as it currently functions will potentially tweet very rarely.  When I have time over the coming weeks, I hope to work more on the modeling side of things, and try to improve performance. Expect updates to this repo, and the bot's performance.

## A special thanks to...

* My advisor [Professor Dragomir Radev]() for his support and insights while advising this project.
* [Greenhouse](https://allaregreen.us/), for inspiring this project
* The Center for Responsive Politics’ excellent [OpenSecrets.org](https://www.opensecrets.org/) for the data regarding donations.
* [Twitter](https://twitter.com), [Google Finance](https://google.com/finance), [Bloomberg](https://bloomberg.com), [Reuters](http://reuters.com), the U.S. Securities and Exchange Commission’s [EDGAR](https://www.sec.gov/edgar/searchedgar/companysearch.html), and [Nasdaq](http://nasdaq.com) for all hosting data relevant to this project.
* [Tweepy](http://docs.tweepy.org/en/v3.5.0/index.html), [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/), [Natural Language Toolkit](http://www.nltk.org/), [pandas](http://pandas.pydata.org/), [Requests](http://docs.python-requests.org/en/master/), [NumPy](http://www.numpy.org/), [tqdm](https://pypi.python.org/pypi/tqdm), [scikit-learn](http://scikit-learn.org/), and of course, [Jupyter Notebook](http://jupyter.org/) for making Python so excellent to work with.


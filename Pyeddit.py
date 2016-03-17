import praw
import sys
import pprint
import time


class RedditPrawler(object):

    def __init__(self):
        self.favoriteSubReddits = ["cscareerquestions",
                                   "blackpeopletwitter", "DBZDokkanBattle"]
        self.r = praw.Reddit(
            user_agent="testing_personal_reddit_crawler_donfistme")
        self.feed = []

    # Gets and sets feed and displays
    def getSubmissions(self, choice, lim):
        self.feed = self.r.get_subreddit(
            self.favoriteSubReddits[int(choice)]).get_hot(limit=int(lim))
        self.displayFeed()

    def displayFeed(self):
        for post in self.feed:
            print ' '.join((str(post)[5:int(len(str(post)))]).split()) + '\n'

    def addSubReddit(self, subreddit):
        self.favoriteSubReddits.append(subreddit)
        print "Successfully added : " + subreddit

    def main(self):
        print "Which subreddit would you like to go to?"
        i = 0
        for x in self.favoriteSubReddits:
            print "(" + str(i) + ") " + x
            i += 1
        input = raw_input()
        print "Okay going to " + self.favoriteSubReddits[int(input)]
        print "---------------------------------------------------"
        self.getSubmissions(input, 20)


pr = RedditPrawler()
pr.main()

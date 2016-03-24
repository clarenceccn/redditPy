import praw
import sys
import pprint
import time


class RedditPrawler(object):

    def __init__(self):
        self.favoriteSubReddits = ["cscareerquestions",
                                   "blackpeopletwitter", "DBZDokkanBattle",
                                   "Funny", "AskReddit", "TIFU",
                                   "eli5", "me_irl", "programmerhumor"]
        # self.favoriteSubReddits.sort()
        self.r = praw.Reddit(
            user_agent="testing_personal_reddit_crawler_donfistme")
        self.feed = []
        self.currIndex = 0

    # Gets and sets feed and displays
    def getSubmissions(self, choice, lim):
        # for submission in self.favoriteSubReddits:
            # self.feed.append(self.r.get_subreddit(
                # submission).get_hot(limit=int(lim)))
        # self.feed = self.r.get_subreddit(
            # self.favoriteSubReddits[self.currIndex]).get_hot(limit=int(lim))
        # return self.displayFeed()
        index = choice - 2
        if index < 0 or index > len(self.favoriteSubReddits):
            return self.displayFeed()
        self.feed = self.r.get_subreddit(
            self.favoriteSubReddits[index]).get_hot(limit=int(lim))
        return self.displayFeed()

    def updateSubmissionCursor(self, direction):
        self.currIndex += direction

    def displayFeed(self):
        finalFeed = []
        newFeed = []
        for post in self.feed:
            # for post in sub:
            newFeed.append(self.crop(post))
            # finalFeed.append(newFeed)
        # return finalFeed
        return newFeed

    def addSubReddit(self, subreddit):
        self.favoriteSubReddits.append(subreddit)
        print "Successfully added : " + subreddit

    def crop(self, post):
        cropIndex = str(post).index(':') + 3
        return str(post)[cropIndex:int(len(str(post)))] + '\n'

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


# pr = RedditPrawler()
# pr.main()

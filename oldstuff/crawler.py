from bs4 import BeautifulSoup
import requests
import time
import sys


class RedditCrawler(object):
    # url = "https://www.reddit.com/r/"
    url = "https://www.google.com/"
    favoriteSubReddits = ["cscareerquestions",
                          "blackpeopletwitter", "DBZDokkanBattle"]

    # Initialize the subreddit reddit Bot
    def __init__(self, reddit):
        self.sentRequest = False
        # url = "https://www.reddit.com/r/"
        self.urlLinks = []
        self.url = "https://www.google.com/"
        self.subreddit = self.url
        self.html = requests.get(self.url)
        self.soup = BeautifulSoup(self.html.text, "html.parser")
        if self.html.status_code == 200:
            print "Initialization sucessful ! : " + self.subreddit
        else:
            print "Error : " + self.html.status_code

    # Scrapes all the titles of all the posts on the subreddit
    def subRedditScrape(self):
        index = 0
        time.sleep(2)
        links = self.soup.findAll("a", {"class": "title"})
        for header in links:
            if "None" not in header.string:
                # gets all the post links
                self.urlLinks.append(header.get("href"))
                print "(" + str(index) + ") " + (header.string)
                index += 1

    # Scrapes the body of the post
    def redditBodyScrape(self):
        userText = self.soup.findAll("div", {"class": "expando"})
        for body in userText:
            if "None" not in body.text:
                urlBody.append(body.text)
                print body.text

    # Scrapes the comments of the post
    def redditCommentScrape(self):
        commentSection = self.soup.find("div", {"class": "commentarea"})
        commentSection = commentSection.find_all('p')
        for comment in commentSection:
            if "None" not in comment.text:
                print comment.text

    def timeLimit(self):
        if self.sentRequest == True:
            time.sleep(2)

    def main(self):
        self.subRedditScrape()  # Displays all posts
        print "Which post would you like to see? . . ."
        input = raw_input()
        time.sleep(2)
        print "Okay, switching to : " + input


# redditTitleScrape('cscareerquestions')
# for link in urlLinks:
    # time.sleep(5)
    # redditBodyScrape(link)
# redditTitleScrape('DBZDokkanBattle')
# redditBodyScrape("/r/cscareerquestions/comments/4aicx6/how_do_you_find_the_time_to_program_in_your_free/")
# redditCommentScrape(
    # "/r/cscareerquestions/comments/4aicx6/how_do_you_find_the_time_to_program_in_your_free/")
redditScrap = RedditCrawler("DBZDokkanBattle")
redditScrap.main()

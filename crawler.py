from bs4 import BeautifulSoup
import urllib
import time
urlLinks = []
urlBody = []

def redditTitleScrape(subreddit):
    print "hey1"
    url = "https://www.reddit.com/r/" + subreddit
    handle = urllib.urlopen(url)
    html_feed = handle.read()
    soup = BeautifulSoup(html_feed,'html.parser')
    index = 0;
    for header in soup.findAll("a",{ "class" : "title" }):
        # time.sleep(5)
        if "None" not in header.string:
            # time.sleep(5)
            urlLinks.append(header.get("href"))
            # redditBodyScrape(header.get("href"))
            print "(" + str(index) + ") " + (header.string)  
            index+=1

def redditBodyScrape(link):
    print "hey"
    url = "https://www.reddit.com" + link
    handle = urllib.urlopen(url)
    html_feed = handle.read()
    soup = BeautifulSoup(html_feed,"html.parser")
    userText = soup.findAll("div", { "class" : "expando"})
    for body in userText: 
        if "None" not in body.text:
            urlBody.append(body.text)
            print body.text

def redditCommentScrape(soup):
    print "hey2"
    url = "https://www.reddit.com" + soup
    handle = urllib.urlopen(url)
    html_feed = handle.read()
    print html_feed
    soup = BeautifulSoup(html_feed,"html.parser")   
    commentSection = soup.find("div", {"class" : "commentarea"})
    commentSection = commentSection.find_all('p')
    for comment in commentSection:
        if "None" not in comment.text:
            print comment.text


# redditTitleScrape('cscareerquestions')
# for link in urlLinks:
    # time.sleep(5)
    # redditBodyScrape(link)
# redditTitleScrape('DBZDokkanBattle')
# redditBodyScrape("/r/cscareerquestions/comments/4aicx6/how_do_you_find_the_time_to_program_in_your_free/")
redditCommentScrape("/r/cscareerquestions/comments/4aicx6/how_do_you_find_the_time_to_program_in_your_free/") 
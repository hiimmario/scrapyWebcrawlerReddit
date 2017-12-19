import praw
import csv

reddit = praw.Reddit(client_id='7R8IfIFqK8easw',
                     client_secret='o8I-SdKabsWYlKt2KWFYQsG1hPc',
                     password='LetsTalkReddit12',
                     user_agent='ltr',
                     username='hiimmario_')

# print(reddit.user.me())

def getSubComments(comment, allComments, verbose=True):
    allComments.append(comment)

    if not hasattr(comment, "replies"):
        replies = comment.comments()
        if verbose: print("fetching (" + str(len(allComments)) + " comments fetched total)")
    else:
        replies = comment.replies

    for child in replies:
        getSubComments(child, allComments, verbose=verbose)


def getAll(r, submissionId, verbose=True):
    submission = r.submission(submissionId)
    comments = submission.comments
    commentsList = []

    for comment in comments:
        getSubComments(comment, commentsList, verbose=verbose)

    if verbose: print("done (" + str(len(commentsList)) + " comments fetched total)")

    return commentsList

##########################

file = open("C:/Users/Mario/PycharmProjects/chatbot/reddit_crawler/reddit_crawler_scrapy/reddit.csv", "rt")
reader = csv.reader(file)

data_set = []
rownum = 0

for row in reader:
    if rownum != 0 or (len(row) != 0):
        submission_id = row[1]
        if submission_id[0:2] == 't3':
            rsid = submission_id[3::]
            data_set.append((row[0], getAll(reddit, rsid, verbose=False)))

file.close()

data_set = data_set

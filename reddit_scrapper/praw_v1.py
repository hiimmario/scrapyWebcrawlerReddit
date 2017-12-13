import praw

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

submission_id = '7jc2fv'
res = getAll(reddit, submission_id)

##########################





for item in res:
    if hasattr(item, "body"):
        print(item.body)
        # TODO
        '''          
        alle eigenschaften die ausgelesen werden soll von hand auslesen
        -> debuggen und abschreiben lol
        dict to json geht nicht da json ein string und dict eine datenstruktur vo der key und das value ein string ist
        '''




# https://www.reddit.com/r/leagueoflegends/

# TODO
# how to get all submission ids from a specific subreddit

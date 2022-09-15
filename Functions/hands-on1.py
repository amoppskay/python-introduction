# def is used to define a fxn name, type "def" and declare the fxn and use :
# fxns help to make any modifications stay within the lines/logic it is not on the entire lines of codes. 
def createPost():
    print("creating a post with details")

def likePost():
    print("like the given post")

def sharePost():
    print("share the given post with friends")
# all these above will not be executed until/printed we call the fxn like we did below

# commenting on a post will require the postId so that it will call the DB and append your comment to that post
def commentOnPost(postId, comment):
    print("comment on the given post")
    print("post details: ", postId)
    print("comment:", comment)

# until and unless you call a fxn, the logic inside it will not be executed or printed. the logic/s is/are called below
commentOnPost("post-12345", "Congrats!!!")
commentOnPost("post-23456", "You made it!!!!!")
# commenting on a post will require the postId so that it will call the DB and append your comment to that post
sharePost()
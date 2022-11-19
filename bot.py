import praw
import random
import datetime
from logging import error
import time

# FIXME:
# copy your generate_comment function from the madlibs assignment here
madlibs = [
    "President Obama had a [CHARISMATIC] [PERSPECTIVE]. He [HELPED] save the U.S from a recession",
    "President Obama was an [AMAZING] president. He is an [IDOL] to millions, not just in the United States but all around the world. During his presidency he [ACHIEVED] many [OUTSTANDING] feats.",
    "President Obama [BETTERED] the American [INFRASTRUCTURE]. He [TURNED AROUND] the automobiles industry. He [RECAPTALIZED] [BANKS].",
    "President Obama was a [LIBERAL] [PRESIDENT]. When [SAME_SEX] marriages were [LOOKED_DOWN_ON] by many, he [LEGALIZED] it.",
    "President Obama had a [CHARISMATIC] [PERSPECTIVE]. He [HELPED] [REDUCE] [MILITARY] in Afghanistan."
    "[OBAMA] was [LOVED] by [MANY]. [HE] [ASSISTED] many [COUNTRIES].",
    "[OBAMA][HELPED] negotiate the Iran Nuclear Deal"
    ]

replacements = {
    'AMAZING' : ['amazing', 'outstanding', 'accomplished'],
    'DISLIKED' : ['hated', 'detest', 'despised', 'disliked'],
    'IDOL' : ['idol', 'icon'],
    'ACHIEVED' : ['accomplished', 'achieved', 'executed'],
    'OUTSTANDING' : ['marvelous', 'outstnading', 'excellent', 'exceptional'],
    'CHARISMATIC'  : ['peace loving', 'peaceful', 'tranquil'],
    'PERSPECTIVE' : ['attitude', 'perspective', 'point of view', 'outlook', 'nature'],
    'HELPED' : ['helped', 'succesfully', 'was able to'],
    'FORCED' : ['forced', 'ordered', 'commanded'],
    'MILITARY' : ['troops', 'forces', 'miliatry'],
    'LIBERAL' : ['open minded', 'liberal', 'left leaning'],
    'PRESIDENT' : ['president', 'leader', 'individual'],
    'SAME_SEX' : ['same sex', 'homosexual', 'same gender'],
    'LOOKED_DOWN_ON' : ['looked down on', 'frowned upon', 'not supported'],
    'LEGALIZED' : ['legalized', 'supported', 'permitted'],
    'REDUCE' : ['reduce','lower the number of', 'minimized the number of'],
    'BETTERED' : ['bettered', 'improved', 'increased'],
    'INFRASTRUCTURE' : ['GDP', 'economy', 'GNI'],
    'TURNED AROUND' : ['flipped', 'up-scaled', 'improved', 'turned around'],
    'RECAPTALIZED' : ['recaptalized, improved, bettered'],
    'BANKS' : ['banks', 'financial institutes'],
    'OBAMA' : [ 'He', 'President Obama'],
    'LOVED' : ['loved', 'respected' , 'valued'],
    'MANY' : ['many', 'most'],
    'ASSISTED' : ['assisted', 'helped'],
    'COUNTRIES' : ['countries', 'nations'],
    }

def generate_comment():
    s = random.choice(madlibs)
    for k in replacements.keys():
        s = s.replace('['+k+']',random.choice(replacements[k]))
    return str(s)

# FIXME:
# connect to reddit 
reddit = praw.Reddit('bot')

# FIXME:
# select a "home" submission in the /r/cs40_2022fall subreddit to post to,
# and put the url below
#
# HINT:
# The default submissions are going to fill up VERY quickly with comments from other students' bots.
# This can cause your code to slow down considerably.
# When you're first writing your code, it probably makes sense to make a submission
# that only you and 1-2 other students are working with.
# That way, you can more easily control the number of comments in the submission.
submission_url = 'https://old.reddit.com/r/cs40_2022fall/comments/yzm47x/how_should_democrats_respond_to_gop_attacks/'
submission = reddit.submission(url=submission_url)

# each iteration of this loop will post a single comment;
# since this loop runs forever, your bot will continue posting comments forever;
# (this is what makes it a deamon);
# recall that you can press CTRL-C in the terminal to stop your bot
#
# HINT:
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:

    # printing the current time will help make the output messages more informative
    # since things on reddit vary with time
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)
    submission.comments.replace_more(limit=None)

    # FIXME (task 0): get a list of all of the comments in the submission
    # HINT: this requires using the .list() and the .replace_more() functions
    all_comments = submission.comments.list()
    # HINT: 
    # we need to make sure that our code is working correctly,
    # and you should not move on from one task to the next until you are 100% sure that 
    # the previous task is working;
    # in general, the way to check if a task is working is to print out information 
    # about the results of that task, 
    # and manually inspect that information to ensure it is correct; 
    # in this specific case, you should check the length of the all_comments variable,
    # and manually ensure that the printed length is the same as the length displayed on reddit;
    # if it's not, then there are some comments that you are not correctly identifying,
    # and you need to figure out which comments those are and how to include them.
    print('len(all_comments)=',len(all_comments))

    # FIXME (task 1): filter all_comments to remove comments that were generated by your bot
    # HINT: 
    # use a for loop to loop over each comment in all_comments,
    # and an if statement to check whether the comment is authored by you or not
    
    not_my_comments = []
    for comment in all_comments:
        if str(comment.author) != 'poli_bot':
            not_my_comments.append(comment)
   
    # HINT:
    # checking if this code is working is a bit more complicated than in the previous tasks;
    # reddit does not directly provide the number of comments in a submission
    # that were not gerenated by your bot,
    # but you can still check this number manually by subtracting the number
    # of comments you know you've posted from the number above;
    # you can use comments that you post manually while logged into your bot to know 
    # how many comments there should be. 
    
    print('len(not_my_comments)=',len(not_my_comments))

    # if the length of your all_comments and not_my_comments lists are the same,
    # then that means you have not posted any comments in the current submission;
    # (your bot may have posted comments in other submissions);
    # your bot will behave differently depending on whether it's posted a comment or not
    
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('len(has_not_commented)=',has_not_commented)

    if has_not_commented:
        # FIXME (task 2)
        # if you have not made any comment in the thread, then post a top level comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # a top level comment is created when you reply to a post instead of a message
        submission.reply(generate_comment())

    else:
        # FIXME (task 3): filter the not_my_comments list to also remove comments that 
        # you've already replied to
        # HINT:
        # there are many ways to accomplish this, but my solution uses two nested for loops
        # the outer for loop loops over not_my_comments,
        # and the inner for loop loops over all the replies of the current comment from the outer loop,
        # and then an if statement checks whether the comment is authored by you or not
        comments_without_replies = []
        for comment in not_my_comments:
            if comment.author != 'poli_bot':
                response = False
                for reply in comment.replies:
                    if str(reply.author) == 'poli_bot':
                        response = True
                if response is False:
                    comments_without_replies.append(comment)
        print('len(comments_without_replies)=',len(comments_without_replies))

        # HINT:
        # this is the most difficult of the tasks,
        # and so you will have to be careful to check that this code is in fact working correctly;
        # many students struggle with getting a large number of "valid comments"
        

        # FIXME (task 4): randomly select a comment from the comments_without_replies list,
        # and reply to that comment
        #
        # HINT:
        # use the generate_comment() function to create the text,
        # and the .reply() function to post it to reddit;
        # these will not be top-level comments;
        # so they will not be replies to a post but replies to a message
        for comments in comments_without_replies:
            sleep_count=0
            selection = random.choice(comments_without_replies)
            bot_reply = generate_comment()
            try:
                selection.reply(bot_reply)
            #except praw.exceptions.APIException:
                #print("not replying to a comment that has been deleted")
           # except IndexError:
                #print( "this submission has no comments without replies")
            except praw.exceptions.RedditAPIException as error:
                for subexception in error.items:
                    if subexception.error_type=="RATELIMIT":
                        error_str=str(subexception)
                        print(error_str)

                        if 'minute' in error_str:
                            delay=error_str.split('for ')[-1].split(' minute')[0]
                            delay=int(delay)*60.0
                        else:
                            delay=error_str.split('for ')[-1].split(' minute')[0]
                            delay=int(delay)
                        
                        print('delay=',delay)
                        time.sleep(delay)
                        sleep_count+=1
                        print('sleep count=',sleep_count)
                if "DELETED_COMMENT" in str(error):
                    print("Comment " + comment.id + " was removed")
                else:
                    print('Error Found: ', error)

    # FIXME (task 5): select a new submission for the next iteration;
    # your newly selected submission should be randomly selected from the 5 hottest submissions
    
    randomnumber = random.random()
    allsubmissions = []
    if randomnumber >= 0.5:
        print('Original Submission')
        submission = reddit.submission(url='https://old.reddit.com/r/cs40_2022fall/comments/yznair/we_are_celebrating_way_too_early_about_the_senate/')
        submission.reply(generate_comment())
    if randomnumber < 0.5:
        print('Top Subreddit Submission')
        for submission in reddit.subreddit('cs40_2022fall').hot(limit=5):
            allsubmissions.append(submission)
        newsubmission = random.choice(allsubmissions)
        submission = reddit.submission(id=newsubmission)
        print('Submission ID: ', newsubmission)
        print(newsubmission.title)
    time.sleep(1)

    # We sleep just for 1 second at the end of the while loop.
    # This doesn't avoid rate limiting
    # (since we're not sleeping for a long period of time),
    # but it does make the program's output more readable.
    

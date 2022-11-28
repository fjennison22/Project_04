'''
This lab has three tasks.

TASK 1:
Implement the `generate_comment` function below.

TASK 2:
Redefine the `madlibs` and `replacements` variables so that the generated comments are what you want your reddit bot to say.
You must have at least 6 different madlibs.
Each madlib should be 2-5 sentences long and have at least 5 [REPLACEMENT] [WORDS].

TASK 3:
Use your `generate_comment` function to post at least 100 messages to the `Practice posting messages here :)` submission, located at:
<https://old.reddit.com/r/cs40_2022fall/comments/yv4s9o/practice_posting_messages_here/>
You should have at least 10 top level comments and at least 10 replies to comments (but it's okay if they're all replies to the same comment).

SUBMISSION:
Upload your bot's name and your `madlib.py` file to sakai.
'''

madlibs = [
    "[OBAMA] had a [CHARISMATIC] [PERSPECTIVE]. He [HELPED] save the [U.S] from a recession",
    "President Obama was an [AMAZING] president. He is an [IDOL] to millions, not just in the [U.S] but all around the world. During his presidency he [ACHIEVED] many [OUTSTANDING] feats.",
    "President Obama [BETTERED] the American [INFRASTRUCTURE]. He [TURNED AROUND] the automobiles industry. He [RECAPTALIZED] [BANKS].",
    "President Obama was a [LIBERAL] [PRESIDENT]. When [SAME_SEX] marriages were [LOOKED_DOWN_ON] by many, he [LEGALIZED] it.",
    "President Obama had a [CHARISMATIC] [PERSPECTIVE]. He [HELPED] [REDUCE] [MILITARY] in Afghanistan."
    "[OBAMA] was [LOVED] by [MANY]. [HE] [ASSISTED] many [COUNTRIES].",
    "[OBAMA][HELPED] negotiate the Iran Nuclear Deal. It took [OUTSTANDING] skill to [REDUCE] negative ramifications of war, hence why Obama is an [IDOL]."
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
    'U.S' : ['U.S', 'United States']
    }

import random
import praw
import time
import datetime

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.

    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.

    For example, if we randomly selected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    Instead, you should ensure that the madlibs that you create will all be grammatically correct when this substitution procedure is followed.
    '''
    madlib_str = random.choice(madlibs)
    for k in replacements.keys():
        madlib_str = madlib_str.replace('['+k+']',random.choice(replacements[k]))
    return(madlib_str)

print('generate_comment()=',generate_comment)

reddit = praw.Reddit('bot')
url = "https://old.reddit.com/r/cs40_2022fall/comments/yv4s9o/practice_posting_messages_here/"
submission = reddit.submission(url=url)
'''
for i in range(100):
    print(datetime.datetime.now(), ': made a comment, i=',i)
    try:
        submission.comments[0].reply(generate_comment)
    except praw.exceptions.APIException:
        print('sleeping for 5 seconds')
        time.sleep(5)
        '''
# Pine's Deaf Grandma
# Pine's grandma is hearing impaired: whatever you say to her, she responds with "HUH?! SPEAK UP, SONNY!",
# unless you shout it (type in all capitals).

# If you shout, she can hear you (or at least she thinks so) and yells back, 
# "NO, NOT SINCE 1938!" You can't stop talking to grandma until you shout "BYE".

# When you shout "BYE", grandma shouts back "OK, BYE!" and end the conversation.

# Your input is an array with a list of strings with all the words/sentences you say in order
# You can expect there is aways a "BYE", although it is not necessarily the last word in the list
# Your output is an array with a list of strings and every sentence Pine's grandma replies
# Words/sentences are always a string
# Example
# ["hi grandma", "WHAT", "bye", "BYE"]  -->
# ["HUH?! SPEAK UP, SONNY!", "NO, NOT SINCE 1938!", "HUH?! SPEAK UP, SONNY!", "OK, BYE!"


                
                
# from itertools import takewhile


# def grandma(sentence):
#     return 'NO, NOT SINCE 1938!' if sentence.isupper() else 'HUH?! SPEAK UP, SONNY!'


# def deaf_grandma(you):
#     return list(map(grandma, takewhile('BYE'.__ne__, you))) + ['OK, BYE!']



def deaf_grandma(you):
    res = []
    for word in you:
        if word.isupper():
            if word == "BYE":
                res.append("OK, BYE!")
                break
            else:
                res.append("NO, NOT SINCE 1938!")
        else:
            res.append("HUH?! SPEAK UP, SONNY!")
    return res
                

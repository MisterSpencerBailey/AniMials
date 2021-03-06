# AniMials
Sends a random cute animal photo to my girlfriend


## How it works:

  1. Picks a random subreddit from a hand-picked list of subreddits
  2. Log into Reddit using PRAW and find the first non-gif post on the subreddit and downloads it
  3. Creates an email and attaches the post title and the recently downloaded image to the email
  4. Emails the person's phone number which then gets sent to their phone
  
 Step #1 has repeat of some subreddits. This is to add 'weight' to certain subreddits, which are currently ones that are more active and 
 are more likely to produce better quality content at a faster pace than others. 
  
 Step #2 avoids GIFv file types as they were being deleted from the message when being sent. 
  
 Step #4, if you send an email to someones phone number with their phone carrier's MMS domain gateway, then it gets sent to their phone as a
 text message. For example, if my phone service provider is T-Mobile, then I would send the email to `1234567890@tmomail.net` and that would
 deliever a text message to the phone number. See [here](https://en.wikipedia.org/wiki/SMS_gateway) for SMS/MMS gateways. I'm also sending it to two people, one of them being me so I can make sure nothing randomly breaks.
 
 
 ## To-Do:
  1. Tests.
  2. Make it more stable. Currently randomly breaks around step #2 when finding an image. The `run.py` script uses recursion to currently catch when it fails and I'd eventually like it to be stable enough to always run.
  3. Clean up code. Try to reduce number of imports and length of some functions. Maybe make it closer to an actual class.

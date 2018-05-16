import twitter

##user = testPy19999
##using the tutorial from https://www.youtube.com/watch?v=dQG4mkD5Nd4


consumer_key = ""
consumer_secret = ""
access_token = ""
access_secret = ""

api = twitter.Api(consumer_key = consumer_key, consumer_secret = consumer_secret, access_token_key = access_token, access_token_secret = access_secret)

print(api.VerifyCredentials())

followers = api.GetFollowers()
users = api.GetFriends()

# look at the document for the twitter API
post_update = api.PostUpdates(status = "Hewwo")


postDM = api.PostDirectMessage(user, text)
get_use = api.GetUser(user)


status_var = "Hewwwwwwwwo"
length_status = twitter.twitter.utils.calc_expected_status_length(status = status_var)

new_message = api.PostDirectMessage(screen_name="dave",text = "hewwwo")

friends = api.GetFriends()
for u in friends:
    print(dir(u))
    print("\n")
    
print(u.screen_name)


api.GetReplies()
api.GetUserTimeline(user)
api.GetHomeTimeline()
api.GetStatus(status_id)
api.GetStatuses(status_ids)
api.DestroyStatus(status_id)
api.GetFriends(user)
api.GetFollowers()
api.GetFeatured()
api.GetDirectMessages()
api.GetSentDirectMessages()
api.PostDirectMessage(user, text)
api.DestroyDirectMessage(message_id)
api.DestroyFriendship(user)
api.CreateFriendship(user)
api.LookupFriendship(user)
api.VerifyCredentials()

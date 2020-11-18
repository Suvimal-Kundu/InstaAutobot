from instapy import InstaPy

session = InstaPy(username="______________", password="_________________")
session.login()

#following section
session.set_do_follow(True, percentage=0, times=1)


#comment section
session.set_do_comment(True, percentage=50)
session.set_comments([u'_________________'])

#like section
session.like_by_tags(['germanshepherd'], amount=500)
session.set_dont_like(["naked", "nsfw", "sex"])


session.end()




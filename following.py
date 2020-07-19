from instapy import InstaPy

# LOGIN 
session = InstaPy(username="roboticactivist", password="Pppppppp").login()
set_user_interact(amount=100, percentage=100, randomize=False, media='Photo')
set_do_comment(enabled=True, percentage=10)
set_comments(comments=['Really interesting! Hope to share this with more people.', 'That is fascinating!','Wow!','This is truly important for society.','The implications here are truly tremendous!', 'More people need to know this.'], media='Photo')

session.follow_commenters(['marine_biology_daily', 'oceana', 'water'], amount=15, daysold=365, max_pic = 3, sleep_delay=10, interact=True)
session.follow_commenters(['noaa'], amount=10, daysold=365, max_pic=7, sleep_delay=10, interact=True) 
session.follow_commenters(['fisheriesoceanscan'], amount=10, daysold=365, max_pic=7, sleep_delay=10, interact=True) 
session.follow_commenters(['unworldoceansday'], amount=10, daysold=365, max_pic=7, sleep_delay=10, interact=True) 

# ENDING SESSION
session.end()


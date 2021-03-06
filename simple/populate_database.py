import csv
from forum.models import Thread, Forum, UserProfile, Post
from django.contrib.auth.models import User

filename = "commotion-announce.txt_sorted.csv"

# Open the csv we're reading from
with open(filename, 'rb') as csvfile:
	forum_data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	# Add forums
	forums = []
	forum_objects = Forum.objects.all()
	for f in forum_objects:
		forums.append(f.title)
	for index, row in enumerate(forum_data_reader):
		if index >0:
			if row[1] not in forums:
				forums.append(row[1])
				f = Forum(title = row[1])
				f.save()


#### Note need to correct user password creation
with open(filename, 'rb') as csvfile:
	forum_data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	# Create a list of all users already in the database
	users = []
	user_objects = User.objects.all()
	for u in user_objects:
		if not u.is_staff:
			users.append(u.username)
		for index, row in enumerate(forum_data_reader):
			if index >0:
				if row[5] not in users:
					users.append(row[5])
					try:
						firstname = user.split(" ")[0]
						lastname = user.split(" ")[1]
					except:
						firstname = "Unknown"
						lastname = "User"
					try:
						u = User.objects.create_user(first_name = firstname, last_name = lastname, username = row[5], password="default123", email="default@forum.com")
						u.save()
					except:
						pass

with open(filename, 'rb') as csvfile:
	forum_data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
		# Add threads
	threads = []
	for index, row in enumerate(forum_data_reader):
		if index >0:
			if row[2] not in threads:
				threads.append(row[2])
				creator = User.objects.filter(username = row[5]).first()
				forum = Forum.objects.filter(title=row[1]).first()
				title = row[2]
				t = Thread(title =title, creator = creator, forum = forum)
				t.save()

# Add posts
with open(filename, 'rb') as csvfile:
	forum_data_reader = csv.reader(csvfile, delimiter=',', quotechar='"')
	for index, row in enumerate(forum_data_reader):
		if index >0:
			creator = User.objects.filter(username = row[5]).first()
			thread = Thread.objects.filter(title = row[2]).first()
			p = Post(creator=creator, thread=thread, title="", body=row[6])
			p.save()

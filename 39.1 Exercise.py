# 39.1 Exercise
user = {
  'age' : 22,
  'user_name' : 'Tanvir',
  'weapons' : ['Groza', 'M416'],
  'is_active' : True,
  'clan' : 'Brothers in Arms'
}
print(user.keys()) #2

user.update({'weapons' : 'Groza, M416'}) #3
print(user)
#3 or user['weapons'].append('M762')

user.update({'is_banned' : False}) #4
print(user)

user.update({'is_banned' : True}) #5
print(user)

user2 = user.copy() #6
user2.update({'age' : 25, 'user_name' : 'Rohit'})
print(user2)
print(user)
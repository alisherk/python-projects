class User: 
  def __init__(self, id, name):  #constructor 
      self.id = id
      self.name = name
      self.followers = 0
      self.following = 0

  def follow(self, user): # method always need to take in self as the first param 
      user.followers += 1
      self.following += 1

    
user_1 = User('1', 'Ali')

user_2 = User('2', 'Bob')

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)


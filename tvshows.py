quit=False
while not quit:
  user=input("Enter a Show")
  u = open("real tvshows.txt", "a")
  u.write(user+"\n")
  u.close()
  final=input("Do you want to end the code(y/n)")
  if final=="y":
    quit=True
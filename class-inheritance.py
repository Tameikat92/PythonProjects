class Person:
  
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

#Use the Person class to create an object, and then execute the printname method:

x = Person("John", "Doe")
x.printname()

class Music: 
   def __init__(self, musicGenre, artistName):
     self.genre = musicGenre
     self.artist = artistName
    
   def printMusicInfo(self):
     print(self.genre,self.artist)

faveGenre = Music("Jazz","Ella Fitzgerald")
faveGenre.printMusicInfo()

class BestAlbum(Music):
  pass #pass keyword when you do not want to add any other properties or methods to the class.

faveAlbum = BestAlbum("Jazz","Joe Pass")
faveAlbum.printMusicInfo()
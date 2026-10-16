class Song (object):

   def __init__(self, lyrics):
        self.lyrics = lyrics

   def sing_me_a_song(self):
         for line in self.lyrics:
             print(line)
         


happy_lyrics = (["happy birthday to you",
                  "i dont want to get sued",
                  "so i will stop right there"])

happy_bday = Song(happy_lyrics)

happy_bday.sing_me_a_song()



bulls_lyrics = (["the rally around the famaly",
                 "with pocket full of shells"])

bulls_on_parade = Song(bulls_lyrics )

bulls_on_parade.sing_me_a_song()

piyaa_lyrics = (["piyaaa oree piyaaaa",
                 "piyaree piyareee piyaaa"])


ore_piyaa = Song(piyaa_lyrics)

ore_piyaa.sing_me_a_song()




 

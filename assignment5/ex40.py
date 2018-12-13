class Song(object):

    def _int_(self, lyrics):
        self.lyrics = lyrics
    
    def sing_me_a_song(self):
        for line in self.lyrics:
            print(line)



print("Happy birthday to you")
print("I don't want to get sued")
print("So I'll stop right there")
print("They rally around tha family")
print("With pockets full of shells")

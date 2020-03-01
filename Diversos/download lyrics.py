from lyricsmaster import LyricWiki, TorController

# Select a provider from the supported Lyrics Providers (LyricWiki, AzLyrics, Genius etc..)
# The default Provider is LyricWiki
provider = LyricWiki()



# Fetch all lyrics from 2Pac
#discography = provider.get_lyrics("Nick_Cave_And_The_Bad_Seeds")

# Fetch all lyrics from 2pac's album 'All eyez on me'.
album = provider.get_lyrics('Nick_Cave_And_The_Bad_Seeds', album="Abattoir Blues")

# You can also supply a folder to save the lyrics in.
folder = "C:/Users/Ander/Desktop/Lyrics"
#discography.save(folder)
album.save(folder)

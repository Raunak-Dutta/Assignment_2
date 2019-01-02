"""(Incomplete) Tests for Song class."""
from song import Song

# test empty song (defaults)
song = Song()
print(song)
assert song.artist == ""
assert song.title == ""
assert song.year == 0
assert song.is_required == 'n'

# test initial-value song
song2 = Song("Amazing Grace", "John Newton", 1779, True)
# TODO: write tests to show this initialisation works
print(song2)
# test mark_learned()
# TODO: write tests to show the mark_learned() method works

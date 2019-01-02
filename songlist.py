# create your SongList class in this file
from song import Song


class SongList:
    def __init__(self, song_obj=[]):
        self.song_obj = song_obj
        try:
            file_r = open('songs.csv', 'r')
        except FileNotFoundError:
            print("FILE NOT FOUND")
            file_r = ''
        for file_line in file_r:
            self.song_obj.append(file_line)

    def get_songs(self):
        end_str = ''
        for file_line in self.song_obj:
            TITLE = ''
            ARTIST = ''
            YEAR = ''
            LEARNED = ''
            # print(file_line)
            flag = 0  # flag to test for various modes
            for w in file_line:
                if w == ',':
                    flag += 1
                else:
                    if flag == 0:
                        TITLE += w
                    elif flag == 1:
                        ARTIST += w
                    elif flag == 2:
                        YEAR += w
                    elif flag == 3:
                        LEARNED += w
                        flag = -99  # Resetting flag so no conflict occurs
            line = Song(TITLE, ARTIST, YEAR, LEARNED)
            end_str = end_str + '\n' + str(line)
        return end_str

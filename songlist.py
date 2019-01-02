# create your SongList class in this file
from song import Song


class SongList:
    def __init__(self):
        file_r = open('song.csv', 'r')
        for file_line in file_r:
            print(file_line)


if __name__ == '__main__':
    try:
        file_r = open('songs.csv', 'r')
    except FileNotFoundError:
        print("FILE NOT FOUND")
        file_r = ''
    for file_line in file_r:
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
        print(line)
        print(line.is_learned())

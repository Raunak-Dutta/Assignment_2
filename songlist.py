# create your SongList class in this file
from song import Song


class SongList:
    end_lst = []

    def __init__(self, song_obj=[]):
        self.song_obj = song_obj
        # self.end_lst = end_lst
        try:
            file_r = open('songs.csv', 'r')
        except FileNotFoundError:
            print("FILE NOT FOUND")
            file_r = ''
        for file_line in file_r:
            if file_line not in self.song_obj:
                self.song_obj.append(file_line)
        file_r.close()

    def get_songs(self):
        end_str = []
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
            end_str.append(str(Song(TITLE, ARTIST, YEAR, LEARNED)))
            # end_str = end_str + '\n' + str(line)
        return end_str

    def add_song(self, append_line):
        append_line = append_line + '\n'
        file_a = open('songs.csv', 'a')
        file_a.write(append_line)

    def sort_song(self, sort_type):
        # print(self.end_lst)
        temp_lst = []
        end_str = ''
        # print(self.song_obj)
        for fi_ln in self.song_obj:
            TITLE = ''
            ARTIST = ''
            YEAR = ''
            LEARNED = ''
            # print(file_line)
            flag = 0  # flag to test for various modes
            for w in fi_ln:
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
            temp_lst.append([TITLE, ARTIST, YEAR, LEARNED])
        # print(self.end_lst)
        from operator import itemgetter
        return_lst = (sorted(temp_lst, key=itemgetter(sort_type)))
        new_lst = []
        for line in return_lst:
            if line is not None:
                return_line = str(Song(line[0], line[1], line[2], line[3]))
                new_lst.append(return_line)
        return new_lst

    def song_clear(self,str_):
        end_str = []
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
            end_str.append(str(Song(TITLE, ARTIST, YEAR, LEARNED)))
        if str_ in end_str:
            indx = end_str.index(str_)
            temp_str = self.song_obj[indx]
            temp_str = temp_str[:-2] + 'y\n'
            self.song_obj[indx] = temp_str
            file_w = open('songs.csv', 'w+')
            file_w.truncate()  # truncate the file that is empty it for the new list to be written
            for eliment in self.song_obj:
                if eliment != " ":
                    file_w.writelines(eliment)
            file_w.close()  # Close the file
        else:
            print('UNEXPECTED OUTPUT')
            print(return_line)

# create your SongList class in this file
from song import Song


class SongList:
    end_lst = []  # Returns the list of songs in a formatted way

    def __init__(self, song_obj=[], f_song=[]):  # loads song into memory as a read only mode
        self.song_obj = song_obj  # assigns song to a variable
        self.f_song = f_song
        # self.end_lst = end_lst
        self.get_songs()

    def get_songs(self):  # get's verious attribute from raw files of a song
        self.song_obj = []  # this list is cleared every time to update
        self.f_song = []  # so is this formatted list
        try:
            file_r = open('songs.csv', 'r')
        except FileNotFoundError:  # for debugging only
            print("FILE NOT FOUND")
            file_r = ''
        for file_line in file_r:
            if file_line not in self.song_obj:
                self.song_obj.append(file_line)
        file_r.close()
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
            tmp_lst = [TITLE, ARTIST, YEAR, LEARNED]
            if tmp_lst not in self.f_song:
                self.f_song.append(tmp_lst)
            elif (tmp_lst[3] != self.f_song[3]) and (tmp_lst[0] == self.f_song[0]):
                self.f_song[indx] = tmp_lst
            # end_str = end_str + '\n' + str(line)
        return end_str

    def add_song(self, append_line):  # function adds song that has been formatted in the main
        append_line = append_line + '\n'
        file_a = open('songs.csv', 'a')
        file_a.write(append_line)

    def sort_song(self, sort_type):  # function sorts song according to the given key
        # print(self.end_lst)
        from operator import itemgetter
        tmp_lst = self.f_song
        print(tmp_lst)
        return_lst = (sorted(tmp_lst, key=itemgetter(sort_type)))  # sorts songs from different keys
        new_lst = []
        for line in return_lst:  # creates new list which is sorted
            if line is not None:
                return_line = str(Song(line[0], line[1], line[2], line[3]))
                # print((line[0], line[1], line[2], line[3]))
                new_lst.append(return_line)
        return new_lst

    def song_clear(self, str_):  # this code is repeted multiple times for no reason
        print(str_)
        com_list = []
        for line in self.f_song:
            for_str = str(Song(line[0], line[1], line[2], line[3]))
            com_list.append(for_str)
        if str_ in com_list:
            indx = com_list.index(str_)
            temp_str = self.song_obj[indx]
            temp_str = temp_str[:-2] + 'y\n'
            self.song_obj[indx] = temp_str
            file_w = open('songs.csv', 'w+')
            file_w.truncate()  # truncate the file that is empty it for the new list to be written
            for eliment in self.song_obj:
                if eliment != " ":
                    file_w.writelines(eliment)  # Writes list to file
            file_w.close()  # Close the file
            self.get_songs()
        else:
            print('UNEXPECTED OUTPUT')

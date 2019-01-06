"""
Name: Raunak Dutta
Date: 2-Jan-2019
Brief Project Description: To create a GUI app that helps you memorize songs, add songs and eventually clear them
when you're done memorizing them, makes no sense to me but whatever I didn't make this project.
GitHub URL:https://github.com/Raunak-Dutta/Assignment_2
"""

from kivy.app import App
from kivy.lang import Builder
from songlist import SongList
from kivy.config import Config
from kivy.properties import StringProperty
from kivy.clock import Clock
from kivy.uix.listview import ListItemButton

# PRESS ESC TO QUIT
# Create your main program in this file, using the SongsToLearnApp class


def update_list():  # Defination to Update song_list every time
    song_list = SongList()
    return song_list.get_songs()


class SongsToLearnApp(App):
    Config.set('graphics', 'fullscreen', '1')  # Kivy config to open app in fullscreen, 0 = off, 1 = on
    Config.set('graphics', 'width', '1920')
    Config.set('graphics', 'height', '1080')
    list_of_songs = update_list()
    sort_codes = ['Title', 'Artist', 'Year']  # Sorting options

    # list_of_songs = update_list()

    def build(self):

        self.title = "Song Tester 1 alpha"
        self.root = Builder.load_file('app.kv')
        self.list_of_songs = update_list()
        self.list_of_songs = (self.sort_song(0))
        return self.root

    def handle_pressed(self):  # Handles nothing
        pass

    def handle_add(self):  # Adds songs to list format songs to pass it onto the songlist
        song_list = SongList()
        title = self.root.ids.input_title.text
        artist = self.root.ids.input_artist.text
        year = self.root.ids.input_year.text
        if title != '' and title != 'Input Title' and title != 'Please enter valid title':
            if artist != '' and artist != 'Input Artist' and artist != 'Please enter valid artist':
                if year != '' and year != 'Input Year' and year != 'Please enter valid year':
                    ap_str = title + ',' + artist + ',' + year + ',n'
                    song_list.add_song(ap_str)
                    self.list_of_songs = update_list()
                    self.root.ids.my_label.item_strings = self.list_of_songs
                else:
                    self.root.ids.input_year.text = 'Please enter valid year'
            else:
                self.root.ids.input_artist.text = 'Please enter valid artist'
        else:
            self.root.ids.input_title.text = 'Please enter valid title'

    def sort_song(self, sort_order):  # Sorts given songs into catagories.
        song_list = SongList()
        if sort_order == 'Title':
            self.list_of_songs = (song_list.sort_song(0))
            self.root.ids.my_label.item_strings = self.list_of_songs

        elif sort_order == 'Artist':
            self.list_of_songs = (song_list.sort_song(1))
            self.root.ids.my_label.item_strings = self.list_of_songs

        else:
            self.list_of_songs = (song_list.sort_song(2))
            self.root.ids.my_label.item_strings = self.list_of_songs

    def clear_input(self):  # function that will clear the output of the inputs
        self.root.ids.input_title.text = ''
        self.root.ids.input_artist.text = ''
        self.root.ids.input_year.text = ''

    def on_click_song(self):  # To cleared selected song
        song_list = SongList()
        if self.root.ids.my_label.adapter.selection:
            song_to_clear = str(self.root.ids.my_label.adapter.selection[0].text)
            print(song_to_clear)
            if '(learned)' not in song_to_clear:
                song_list.song_clear(song_to_clear)
                self.sort_song(0)
                # self.root.ids.my_label.item_strings = self.list_of_songs
            else:
                self.root.ids.popup_return_text.text = 'The song ' \
                    '{0} is already learned please select a different song from the list'.format(song_to_clear[:-15])
                self.root.ids.warn.open()

    def press_popup_ok(self):
        self.root.ids.warn.dismiss()


class ListSong(ListItemButton):  # Works as a cls for the list view adapter.
    pass


SongsToLearnApp().run()

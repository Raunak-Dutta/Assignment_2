"""
Name:
Date:
Brief Project Description:
GitHub URL:
"""

from kivy.app import App
from kivy.lang import Builder
from songlist import SongList

# Create your main program in this file, using the SongsToLearnApp class


class SongsToLearnApp(App):
    def build(self):
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('app.kv')
        Song_List = SongList()
        self.root.ids.my_label.text = Song_List.get_songs()
        return self.root

    def handle_pressed(self):
        pass


SongsToLearnApp().run()

# if __name__ == '__main__':
#     Song_List = SongList()
#     print(Song_List.get_songs())
# create your Song class in this file


class Song:
    def __init__(self, title='', artist='', year=0, is_required='n'):
        self.title = title
        self.artist = artist
        self.year = year
        self.is_required = is_required

    def is_learned(self):
        #print(self.is_required)
        if self.is_required == 'y':
            return True
        elif self.is_required == 'n':
            return False
        else:
            return 'No song found'

    def __str__(self):
        if self.is_learned():
            return '{0} By {1} {2} ({3})'.format(self.title, self.artist, self.year, 'learned')

        else:
            return '{0} By {1} {2}'.format(self.title, self.artist, self.year,)

class NamedList(list):
    def __init__(self, a_name):
        list.__init__([])
        self.name = a_name
        self.dob = None
johnny = NamedList('John Paul Jones')
dir(johnny)
dir(list)
johnny.dob = '2017.10.10'
johnny.extend(['Composer', 'Arranger', 'Musician'])
normelvar = 3
for attr in johnny:
    print(johnny.name + 'is a ' + attr + '. - ' + johnny.dob)
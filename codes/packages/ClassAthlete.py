class Athlete:
    def __init__(self, athlete_name, athlete_dob=None, athlete_times=[]):
        self.name = athlete_name
        self.dob = athlete_dob
        self.times = athlete_times
    def Aprint(self):
        print(self.name,self.times)

sarah = Athlete('Sarah Sweeney', '2002-6-17', ['2:58', '2.58', '1.56'])
james = Athlete('James Jones')
sarah.Aprint()
james.Aprint()
Athlete.__init__(james, athlete_name='Sarah Sweeney', athlete_times=['0:58', '0.58', '0.56'])
james.Aprint()

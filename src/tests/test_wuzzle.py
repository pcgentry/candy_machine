from wuzzle import Wuzzle 

class TestWuzzle():
    def setup(self):
        self.test_wuzzle = Wuzzle()
        
    def test_wuzzle_has_name(self):
        self.setup()
        assert self.test_wuzzle.name, "Wuzzle has not named themself."


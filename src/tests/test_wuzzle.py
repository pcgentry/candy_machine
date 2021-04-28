from wuzzle import Wuzzle 

class TestWuzzle():
    def setup(self):
        self.test_wuzzle = Wuzzle()
        
    def test_wuzzle_has_name(self):
        self.setup()
        assert self.test_wuzzle.name, "Wuzzle has not named themself."

    def test_wuzzle_has_flavor_preferences(self):
        self.setup()
        assert self.test_wuzzle.flavor_preferences, "Wuzzle has no flavor preferences"
        assert type(self.test_wuzzle.flavor_preferences) is list, "Wuzzle flavor preferences is not a list"
        assert len(self.test_wuzzle.flavor_preferences) > 0, "Wuzzle has zero flavor preferences"
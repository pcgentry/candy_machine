""" Testing the machine itself """


def test_machine_init(RandomMachine):
  assert isinstance(RandomMachine.strategy, str)


def test_recommend_for_wuzzle(RandomMachine, RandomWuzzle, CandySet):
  Test_Wuz = RandomWuzzle
  candies = CandySet

  Test_Wuz.find_candies(candies)
  Test_Wuz.generate_cookbooks()

  RandomMachine.recommend_for_wuzzle(Test_Wuz, candies)
  
  assert isinstance(Test_Wuz.menu, list)
  assert len(Test_Wuz.menu) > 0



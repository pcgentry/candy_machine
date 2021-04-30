""" Testing the machine itself """


def test_machine_init(RandomMachine):
  assert RandomMachine.learning_rate > 0

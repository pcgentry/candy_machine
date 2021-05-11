"""The Cookbook class."""

class Cookbook():
  """The queue for each model."""

  def __init__(self, flavor="vanilla"):
    self.model_type = "random"
    self.flavor = flavor
    self.candy_ids = []

class Cookbook():
  ''' Cookbook holds the queue for each model. '''

  def __init__(self, flavor="vanilla") -> None:
    self.model_type = "random"
    self.flavor = flavor
    self.candy_ids = []
    

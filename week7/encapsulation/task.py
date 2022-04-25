class PrivateProject:
  github_link = 'https://docs.google.com/document/d/12zsvboxFdzZT2NdSf_puoA7L1k76wwXGQFIByreu3R8/edit'
  __developers = ['Kalashovich', 'Acosador', 'Masha']

  
  def __init__(self, username):
    self.username = username
    self.github_link = 'https://docs.google.com/document/d/12zsvboxFdzZT2NdSf_puoA7L1k76wwXGQFIByreu3R8/edit'
    self.__developers = ['Kalashovich', 'Acosador', 'Masha']

  @property
  def github_link(self):
    if self.username in self.__developers:
      print(self.github_link)
    else:
      print('Forbidden')
      
    

    
test = PrivateProject('Kalashovich')
test.github_link
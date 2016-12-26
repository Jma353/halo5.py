from halo5.base import Base

class Metadata(Base):
  """ For fetching the `Metadata` info from the Halo 5 API """

  def __init__(self, sub_key):
    super(Metadata, self).__init__('metadata/h5/metadata/', sub_key)

  def campaign_missions (self):
    return self.get (url = self.base_url + 'campaign-missions')

  def commendations (self):
    return self.get (url = self.base_url + 'commendations')

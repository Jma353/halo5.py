from halo5.base import Base
from halo5.metadata import Metadata

class Client(object):
  """ The client for interacting with Halo 5 resources """

  def __init__(self, **kwargs):
    self.sub_key = kwargs.get('sub_key')
    self.metadata = Metadata (self.sub_key)

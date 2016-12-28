from halo5.base import Base
from urllib import quote_plus

class Stats(Base):
  """ For fetching the `Stats` info from the Halo 5 API """

  def __init__ (self, sub_key):
    super (Stats, self).__init__('stats/h5/', sub_key)

  def events_for_match (self, match_id):
    return self.get (
      url = self.base_url + 'matches/' + match_id + '/events').json()

  def matches_for_player (self, player, modes = None, start = 0, count = 25):
    params = { 'start' : start, 'count' : count }
    if modes is not None: params['modes'] = modes
    return self.get (
      params = params, url = self.base_url + player + '/matches?').json()

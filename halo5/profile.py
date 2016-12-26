from halo5.base import Base

class Profile(Base):
  """ For fetching the `Profile` info from the Halo 5 API """

  def __init__ (self, sub_key):
    super(Profile, self).__init__('profile/h5/profiles/', sub_key)

  def emblem_image (self, player, size=256):
    return "TODO"

  def spartan_image (self, player, size=256, crop="full"):
    return "TODO"

  

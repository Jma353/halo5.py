from halo5.base import Base

class Metadata(Base):
  """ For fetching the `Metadata` info from the Halo 5 API """

  def __init__(self, sub_key):
    super(Metadata, self).__init__('metadata/h5/metadata/', sub_key)


  

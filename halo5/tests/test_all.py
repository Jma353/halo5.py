import os
import halo5
import time

# Driver
c = halo5.client.Client (os.getenv('HALO5_SUB_KEY', ''))

def test_campaign_missions ():
  result = c.metadata.campaign_missions()
  assert result is not None
  assert 'message' not in result
  time.sleep(1)

import os
import halo5
import time

# Driver
c = halo5.client.Client (os.getenv('HALO5_SUB_KEY', ''))

# Validate success & sleep (1 request / 1 second limit)
def validate_result (result):
  assert result is not None
  assert 'message' not in result
  time.sleep(1)

def test_campaign_missions ():
  result = c.metadata.campaign_missions()
  validate_result(result)

def test_commendations ():
  result = c.metadata.commendations()
  validate_result(result)

def test_csr_designations ():
  result = c.metadata.csr_designations()
  validate_result(result)

def test_enemies ():
  result = c.metadata.enemies()
  validate_result(result)

def test_flexible_stats ():
  result = c.metadata.flexible_stats()
  validate_result(result)

def test_game_base_variants ():
  result = c.metadata.game_base_variants()
  validate_result(result)

def test_impulses ():
  result = c.metadata.impulses()
  validate_result(result)

def test_maps ():
  result = c.metadata.maps()
  validate_result(result)

def test_map_variants ():
  maps = c.metadata.maps()
  validate_result(maps)
  test_id = maps[0]['id']
  result = c.metadata.map_variants(test_id)
  validate_result(result)

def test_medals ():
  result = c.metadata.medals()
  validate_result(result)

def test_playlists ():
  result = c.metadata.playlists()
  validate_result(result)

# Omitting requisition_packs (id) & requisitions (id)
# b/c IDK where to find the corresponding ID's lol 

def test_seasons ():
  result = c.metadata.seasons()
  validate_result(result)

def test_skulls ():
  result = c.metadata.skulls()
  validate_result(result)

def test_spartan_ranks ():
  result = c.metadata.spartan_ranks()
  validate_result(result)

def test_team_colors ():
  result = c.metadata.team_colors()
  validate_result(result)

def test_vehicles ():
  result = c.metadata.vehicles()
  validate_result(result)

def test_weapons ():
  result = c.metadata.weapons()
  validate_result(result)

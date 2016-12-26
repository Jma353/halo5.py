class Base(object):
  """ Base class w/all essentials inside """

  # Essential for interacting with REST API
  import requests
  import simplejson

  # For encoding requests
  try:
    from urllib import urlencode
  except ImportError:
    from urllib.parse import urlencode


  def __init__(self, url_ext, sub_key):
    self.base_url = 'https://www.haloapi.com/' + url_ext
    self.sub_key = sub_key

  def get(self, **kwargs):
    param_str = urlencode(kwargs.get('params', {}))
    url = kwargs.get('url')
    headers = kwargs.get('headers', {})
    headers['Ocp-Apim-Subscription-Key'] = self.sub_key
    return requests.get(url + param_str, headers=headers).json()

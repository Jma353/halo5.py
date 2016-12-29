========
halo5.py
========

A wrapper for the `Halo 5: Guardians API`_.

.. _`Halo 5: Guardians API`: https://developer.haloapi.com/

Installation
------------

To install ``halo5.py`` ::

  pip install halo5.py

Usage
-------------

To grab ``Service Record : Arena`` data of the player ``Spitimou`` ::

  import halo5

  c = halo5.client.Client('my-halo-5-api-subscription-key')
  players = c.stats.service_record_arena(['Spitimou'])
  print players.Results[0].Id
  # => "Spitimou"

The wrapper follows the form of the legitimate API response, but it allows for dot notation.

All four categories of response are namespaced accordingly (``metadata``, ``profile``, ``stats``, and ``ugc``).

Tests
-----

To run the tests, run the following script ::

  ./test "my-halo-5-api-subscription-key"

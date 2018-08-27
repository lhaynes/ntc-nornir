#!/usr/bin/env python

from nornir.core import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_get

nr = InitNornir(
    config_file='nornir.yaml', num_workers=2
)

cmh = nr.filter()
results = cmh.run(
  task=napalm_get, getters=['get_lldp_neighbors_detail']
)

print_result(results)

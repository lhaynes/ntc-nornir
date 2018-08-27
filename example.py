#!/usr/bin/env python

from nornir.core import InitNornir
from nornir.plugins.functions.text import print_result
from nornir.plugins.tasks.networking import napalm_get

nr = InitNornir(
    config_file='nornir.yaml'
)

cmh = nr.filter()
results = cmh.run(
    #NAPALM Getters: https://napalm.readthedocs.io/en/latest/support/
    task=napalm_get, getters=['get_lldp_neighbors_detail']
)

print_result(results)

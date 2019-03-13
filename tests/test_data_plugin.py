#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

from osmosis_on_premise_driver.data_plugin import Plugin


def test_data_plugin():
    assert Plugin().type() == 'On premise'


def test_generate_url():
    url = 'https://www.example.com'
    assert Plugin().generate_url(url) == url

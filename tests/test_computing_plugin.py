from osmosis_on_premise_driver.computing_plugin import Plugin


def test_computing_plugin():
    assert Plugin().type() == 'On premise'

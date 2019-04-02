#  Copyright 2018 Ocean Protocol Foundation
#  SPDX-License-Identifier: Apache-2.0

from osmosis_driver_interface.data_plugin import AbstractPlugin


class Plugin(AbstractPlugin):
    def __init__(self, config=None):
        self.config = config

    def type(self):
        """str: the type of this plugin (``'On premise'``)"""
        return 'On premise'

    def upload(self, local_file, remote_file):
        pass

    def download(self, remote_file, local_file):
        pass

    def list(self, remote_folder):
        pass

    def generate_url(self, remote_file):
        return remote_file

    def delete(self, remote_file):
        pass

    def copy(self, source_path, dest_path):
        pass

    def create_directory(self, remote_folder):
        pass

    def retrieve_availability_proof(self):
        pass

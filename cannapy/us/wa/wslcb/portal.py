"""An interface to the WSLCB Socrata-based open data portal."""

import os
import time
from sodapy import Socrata

# WSLCB Socrata Open Data Portal URL
WSLCB_PORTAL_URL = 'data.lcb.wa.gov'

# WSLCB Socrata Open Data Portal Dataset IDs
WSLCB_PORTAL_DATASETS = {
    'licensed_businesses': 'bhbp-x4eb',
}


class WSLCBPortal(object):
    """A class interface to the WSLCB open data portal."""

    def __init__(self, app_token=''):
        """Constructor."""
        # Set the user's Socrata app token:
        # https://dev.socrata.com/docs/app-tokens.html
        if app_token == '':
            # See if an environment variable is set
            app_token = os.getenv('WSLCB_APP_TOKEN', '')
        self._app_token = app_token

        # The Socrata client property will be initialized on first get
        self._client = None

    def dataset_last_updated(self, dataset_id):
        """Return the requested dataset's last update timestamp."""
        # Retrieve the source dataset's metadata
        metadata = self.client.get_metadata(dataset_id)

        # Retrieve dataset last update timestamp in epoch/Unix time
        last_updated = metadata['rowsUpdatedAt']

        # Convert to a localized Python time.struct_time
        # https://docs.python.org/3/library/time.html#time.struct_time
        last_updated = time.localtime(last_updated)

        return last_updated

    @property
    def app_token(self):
        """The user's Socrata open data portal app token."""
        return self._app_token

    @app_token.setter
    def app_token(self, value):
        self._app_token = value

    @property
    def client(self):
        """A sodapy client interface to the WSLCB Socrata open data portal."""
        if self._client is None:
            self._client = Socrata(WSLCB_PORTAL_URL, self.app_token)

        return self._client

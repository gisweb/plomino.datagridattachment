# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from plomino.datagridattachment.testing import PLOMINO_DATAGRIDATTACHMENT_INTEGRATION_TESTING  # noqa
from plone import api

import unittest2 as unittest


class TestSetup(unittest.TestCase):
    """Test that plomino.datagridattachment is properly installed."""

    layer = PLOMINO_DATAGRIDATTACHMENT_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if plomino.datagridattachment is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('plomino.datagridattachment'))

    def test_browserlayer(self):
        """Test that IPlominoDatagridattachmentLayer is registered."""
        from plomino.datagridattachment.interfaces import IPlominoDatagridattachmentLayer
        from plone.browserlayer import utils
        self.assertIn(IPlominoDatagridattachmentLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = PLOMINO_DATAGRIDATTACHMENT_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['plomino.datagridattachment'])

    def test_product_uninstalled(self):
        """Test if plomino.datagridattachment is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('plomino.datagridattachment'))

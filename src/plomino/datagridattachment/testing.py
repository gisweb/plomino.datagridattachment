# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import plomino.datagridattachment


class PlominoDatagridattachmentLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=plomino.datagridattachment)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'plomino.datagridattachment:default')


PLOMINO_DATAGRIDATTACHMENT_FIXTURE = PlominoDatagridattachmentLayer()


PLOMINO_DATAGRIDATTACHMENT_INTEGRATION_TESTING = IntegrationTesting(
    bases=(PLOMINO_DATAGRIDATTACHMENT_FIXTURE,),
    name='PlominoDatagridattachmentLayer:IntegrationTesting'
)


PLOMINO_DATAGRIDATTACHMENT_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(PLOMINO_DATAGRIDATTACHMENT_FIXTURE,),
    name='PlominoDatagridattachmentLayer:FunctionalTesting'
)


PLOMINO_DATAGRIDATTACHMENT_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        PLOMINO_DATAGRIDATTACHMENT_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='PlominoDatagridattachmentLayer:AcceptanceTesting'
)

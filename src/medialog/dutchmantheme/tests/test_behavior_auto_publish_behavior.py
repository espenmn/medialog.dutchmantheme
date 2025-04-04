# -*- coding: utf-8 -*-
from medialog.dutchmantheme.behaviors.auto_publish_behavior import IAutoPublishBehaviorMarker
from medialog.dutchmantheme.testing import MEDIALOG_DUTCHMANTHEME_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class AutoPublishBehaviorIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_DUTCHMANTHEME_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_auto_publish_behavior(self):
        behavior = getUtility(IBehavior, 'medialog.dutchmantheme.auto_publish_behavior')
        self.assertEqual(
            behavior.marker,
            IAutoPublishBehaviorMarker,
        )

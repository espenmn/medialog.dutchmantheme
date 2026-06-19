# -*- coding: utf-8 -*-
from plone import api
from medialog.dutchmantheme.interfaces import IMedialogDutchmanThemeSettings
 


def update_registry(context):
    """Update missing entries"""
    registry = api.portal.get_tool("portal_registry")

    registry.registerInterface(
        IMedialogDutchmanThemeSettings,
        prefix="medialog.dutchmantheme.interfaces.IMedialogDutchmanThemeSettings",
    )
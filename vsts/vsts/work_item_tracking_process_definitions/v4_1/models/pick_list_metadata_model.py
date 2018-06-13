# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class PickListMetadataModel(Model):
    """PickListMetadataModel.

    :param id: ID of the picklist
    :type id: str
    :param is_suggested: Is input values by user only limited to suggested values
    :type is_suggested: bool
    :param name: Name of the picklist
    :type name: str
    :param type: Type of picklist
    :type type: str
    :param url: Url of the picklist
    :type url: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
        'is_suggested': {'key': 'isSuggested', 'type': 'bool'},
        'name': {'key': 'name', 'type': 'str'},
        'type': {'key': 'type', 'type': 'str'},
        'url': {'key': 'url', 'type': 'str'}
    }

    def __init__(self, id=None, is_suggested=None, name=None, type=None, url=None):
        super(PickListMetadataModel, self).__init__()
        self.id = id
        self.is_suggested = is_suggested
        self.name = name
        self.type = type
        self.url = url

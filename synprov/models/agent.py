# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from synprov.models.base_model_ import Model
from synprov.models.prov_node import ProvNode
from synprov import util

from synprov.models.prov_node import ProvNode  # noqa: E501

class Agent(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, id=None, name=None, description=None, created_at=None, created_by=None, user_id=None):  # noqa: E501
        """Agent - a model defined in OpenAPI

        :param id: The id of this Agent.  # noqa: E501
        :type id: str
        :param name: The name of this Agent.  # noqa: E501
        :type name: str
        :param description: The description of this Agent.  # noqa: E501
        :type description: str
        :param created_at: The created_at of this Agent.  # noqa: E501
        :type created_at: date
        :param created_by: The created_by of this Agent.  # noqa: E501
        :type created_by: str
        :param user_id: The user_id of this Agent.  # noqa: E501
        :type user_id: str
        """
        self.openapi_types = {
            'id': str,
            'name': str,
            'description': str,
            'created_at': date,
            'created_by': str,
            'user_id': str
        }

        self.attribute_map = {
            'id': 'id',
            'name': 'name',
            'description': 'description',
            'created_at': 'createdAt',
            'created_by': 'createdBy',
            'user_id': 'userId'
        }

        self._id = id
        self._name = name
        self._description = description
        self._created_at = created_at
        self._created_by = created_by
        self._user_id = user_id

    @classmethod
    def from_dict(cls, dikt) -> 'Agent':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Agent of this Agent.  # noqa: E501
        :rtype: Agent
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self):
        """Gets the id of this Agent.


        :return: The id of this Agent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Agent.


        :param id: The id of this Agent.
        :type id: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Agent.


        :return: The name of this Agent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Agent.


        :param name: The name of this Agent.
        :type name: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this Agent.


        :return: The description of this Agent.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Agent.


        :param description: The description of this Agent.
        :type description: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this Agent.


        :return: The created_at of this Agent.
        :rtype: date
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Agent.


        :param created_at: The created_at of this Agent.
        :type created_at: date
        """

        self._created_at = created_at

    @property
    def created_by(self):
        """Gets the created_by of this Agent.


        :return: The created_by of this Agent.
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Agent.


        :param created_by: The created_by of this Agent.
        :type created_by: str
        """

        self._created_by = created_by

    @property
    def user_id(self):
        """Gets the user_id of this Agent.


        :return: The user_id of this Agent.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this Agent.


        :param user_id: The user_id of this Agent.
        :type user_id: str
        """
        if user_id is None:
            raise ValueError("Invalid value for `user_id`, must not be `None`")  # noqa: E501

        self._user_id = user_id

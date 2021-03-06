# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from synprov.models.base_model_ import Model
from synprov.models.edge import Edge
from synprov.models.node import Node
from synprov import util


class D3Graph(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, nodes=None, relationships=None):  # noqa: E501
        """D3Graph - a model defined in OpenAPI

        :param nodes: The nodes of this D3Graph.  # noqa: E501
        :type nodes: List[Node]
        :param relationships: The relationships of this D3Graph.  # noqa: E501
        :type relationships: List[Edge]
        """
        self.openapi_types = {
            'nodes': List[Node],
            'relationships': List[Edge]
        }

        self.attribute_map = {
            'nodes': 'nodes',
            'relationships': 'relationships'
        }

        self._nodes = nodes
        self._relationships = relationships

    @classmethod
    def from_dict(cls, dikt) -> 'D3Graph':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The D3Graph of this D3Graph.  # noqa: E501
        :rtype: D3Graph
        """
        return util.deserialize_model(dikt, cls)

    @property
    def nodes(self):
        """Gets the nodes of this D3Graph.


        :return: The nodes of this D3Graph.
        :rtype: List[Node]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this D3Graph.


        :param nodes: The nodes of this D3Graph.
        :type nodes: List[Node]
        """

        self._nodes = nodes

    @property
    def relationships(self):
        """Gets the relationships of this D3Graph.


        :return: The relationships of this D3Graph.
        :rtype: List[Edge]
        """
        return self._relationships

    @relationships.setter
    def relationships(self, relationships):
        """Sets the relationships of this D3Graph.


        :param relationships: The relationships of this D3Graph.
        :type relationships: List[Edge]
        """

        self._relationships = relationships

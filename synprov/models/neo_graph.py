# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from synprov.models.base_model_ import Model
from synprov.models.neo_graph_results import NeoGraphResults
from synprov import util


class NeoGraph(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, results=None):  # noqa: E501
        """NeoGraph - a model defined in OpenAPI

        :param results: The results of this NeoGraph.  # noqa: E501
        :type results: List[NeoGraphResults]
        """
        self.openapi_types = {
            'results': List[NeoGraphResults]
        }

        self.attribute_map = {
            'results': 'results'
        }

        self._results = results

    @classmethod
    def from_dict(cls, dikt) -> 'NeoGraph':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The NeoGraph of this NeoGraph.  # noqa: E501
        :rtype: NeoGraph
        """
        return util.deserialize_model(dikt, cls)

    @property
    def results(self):
        """Gets the results of this NeoGraph.


        :return: The results of this NeoGraph.
        :rtype: List[NeoGraphResults]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this NeoGraph.


        :param results: The results of this NeoGraph.
        :type results: List[NeoGraphResults]
        """

        self._results = results

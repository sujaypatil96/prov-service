import connexion
import six
import uuid
import humps
import json
import logging

from py2neo import Node, NodeMatcher
from luqum.parser import parser

from synprov.models.activity import Activity
from synprov.config import neo4j_connection as graph
from synprov.graph import ActivityBuilder, ActivityEditor
from synprov.util import (neo4j_to_d3,
                          neo4j_export,
                          convert_keys,
                          quote_string,
                          node_to_dict)


logger = logging.getLogger(__name__)


ATTR_MAP = dict([[v, k] for k, v in Activity().attribute_map.items()])


def add_activity_used(
    activity_id,
    body
):  # noqa: E501
    """Add &#39;used&#39; reference

    Add a reference to the list of &#39;used&#39; entities in an Activity.  # noqa: E501

    :param activity_id: activity ID
    :type activity_id: str
    :param body: 
    :type body: dict | bytes

    :rtype: None
    """
    editor = ActivityEditor(id=activity_id)
    act_node = editor.append_used(body.to_dict())
    return convert_keys({
        'id': str(act_node.identity),
        'labels': list(act_node.labels),
        'properties': dict(act_node)
    })


def create_activity(body=None):  # noqa: E501
    """Create a new.

    Create a new Activity. If the passed Activity object contains a Used array, you must set the concreteType field of each Used subclass. # noqa: E501

    :param body:
    :type body: dict | bytes

    :rtype: Activity
    """
    builder = ActivityBuilder(
        **body.to_dict()
    )
    act_node = builder.save()
    print(act_node)
    return convert_keys({
        'id': str(act_node.identity),
        'labels': list(act_node.labels),
        'properties': dict(act_node)
    })


def create_activity_batch(
    body
):  # noqa: E501
    """Create multiple new activities

    Create multiple new Activities. # noqa: E501

    :param body:
    :type body: list | bytes

    :rtype: List[Node]
    """
    return [create_activity(item) for item in body]


def delete_activity_used(
    activity_id,
    target_id
):  # noqa: E501
    """Delete &#39;used&#39; reference

    Remove a reference from the list of &#39;used&#39; entities in an Activity.  # noqa: E501

    :param id: activity ID
    :type id: str
    :param reference_id: entity ID
    :type reference_id: str

    :rtype: Node
    """
    query_base = (
        '''
        MATCH (t:Reference {target_id: {target_id}})<-[r:USED]-(s:Activity {id: {activity_id}})
        DELETE r
        '''
    )

    graph.run(
        query_base,
        activity_id=activity_id,
        target_id=target_id
    )


def get_activities_graph(
    sort_by='created_at',
    order='desc',
    limit=3,
    q='*:*'
):  # noqa: E501
    """Get provenance graph

    Retrieve all nodes and relationships in the graph that pass filters.  # noqa: E501

    :param sort_by: logic by which to sort matched activities
    :type sort_by: str
    :param order: sort order (ascending or descending)
    :type order: str
    :param limit: maximum number of connected activities to return
    :type limit: int
    :param q: filter results using Lucene Query Syntax in the format of propertyName:value, propertyName:[num1 TO num2] and date range format, propertyName:[yyyyMMdd TO yyyyMMdd]
    :type q: str

    :rtype: Neo4jGraph
    """
    filter_properties = ''
    if q != '*:*':
        tree = parser.parse(q)
        key = ATTR_MAP[tree.name]
        val = quote_string(tree.children[0].value)
        filter_properties = f' {{{key}: {val}}}'

    query_base = (
        '''
        MATCH (s:Activity{filter})
        WITH s
        ORDER BY s.{key}{dir}
        WITH collect(s) as activities
        UNWIND activities[0..{lim}] as t
        MATCH (s)-[r]-(t)
        RETURN s as source, r as relationship, t as target
        '''
    ).format(
        key=sort_by,
        dir=(' ' + order.upper()) if order == 'desc' else '',
        lim=limit,
        filter=filter_properties
    )

    results = graph.run(
        query_base,
    )
    return convert_keys(neo4j_export(results.data()))


def get_agent_subgraph(
    user_id,
    sort_by='created_at',
    order='desc',
    limit=3,
    q='*:*'
):  # noqa: E501
    """Get subgraph connected to an agent

    Retrieve the nodes and relationships in a neighborhood around a specified user.  # noqa: E501

    :param user_id: user ID
    :type user_id: str
    :param sort_by: logic by which to sort matched activities
    :type sort_by: str
    :param order: sort order (ascending or descending)
    :type order: str
    :param limit: maximum number of connected activities to return
    :type limit: int
    :param q: filter results using Lucene Query Syntax in the format of propertyName:value, propertyName:[num1 TO num2] and date range format, propertyName:[yyyyMMdd TO yyyyMMdd]
    :type q: str

    :rtype: Neo4jGraph
    """
    filter_properties = ''
    if q != '*:*':
        tree = parser.parse(q)
        key = ATTR_MAP[tree.name]
        val = quote_string(tree.children[0].value)
        filter_properties = f' {{{key}: {val}}}'

    query_base = (
        '''
        MATCH (t:Agent {{user_id: {{user_id}}}})<-[r:WASASSOCIATEDWITH]-(s:Activity{filter})
        WITH s
        ORDER BY s.{key}{dir}
        WITH collect(s) as activities
        UNWIND activities[0..{lim}] as t
        MATCH (s)-[r]-(t)
        RETURN s as source, r as relationship, t as target
        '''
    ).format(
        key=sort_by,
        dir=(' ' + order.upper()) if order == 'desc' else '',
        lim=limit,
        filter=filter_properties
    )

    results = graph.run(
        query_base,
        user_id=user_id
    )
    return convert_keys(neo4j_export(results.data()))


def get_reference_activities(
    target_id,
    direction='down',
    sort_by='created_at',
    order='desc',
    limit=3,
    q='*:*'
):  # noqa: E501
    """Get subgraph connected to an entity

    Retrieve the Activity objects in a neighborhood around a specified entity.  # noqa: E501

    :param target_id: entity ID
    :type target_id: str
    :param direction: direction in which to collect connected activities
    :type direction: str
    :param sort_by: logic by which to sort matched activities
    :type sort_by: str
    :param order: sort order (ascending or descending)
    :type order: str
    :param limit: maximum number of connected activities to return
    :type limit: int
    :param q: filter results using Lucene Query Syntax in the format of propertyName:value, propertyName:[num1 TO num2] and date range format, propertyName:[yyyyMMdd TO yyyyMMdd]
    :type q: str

    :rtype: List[Activity]
    """
    filter_properties = ''
    if q != '*:*':
        tree = parser.parse(q)
        key = ATTR_MAP[tree.name]
        val = quote_string(tree.children[0].value)
        filter_properties = f' {{{key}: {val}}}'

    direction_rels = {
        'up': '-[r:WASGENERATEDBY]->',
        'down': '<-[r:USED]-'
    }
    query_base = (
        '''
        MATCH (t:Reference {{target_id: {{target_id}}}}){dir_rel}(s:Activity{filter})
        WITH s
        ORDER BY s.{key}{dir}
        WITH collect(s) as activities
        UNWIND activities[0..{lim}] as a
        RETURN a as activity
        '''
    ).format(
        dir_rel=direction_rels[direction],
        key=sort_by,
        dir=(' ' + order.upper()) if order == 'desc' else '',
        lim=limit,
        filter=filter_properties
    )

    results = graph.run(
        query_base,
        target_id=target_id
    )
    return list(map(lambda a: node_to_dict(a['activity']), results.data()))


def get_reference_subgraph(
    target_id,
    direction='down',
    sort_by='created_at',
    order='desc',
    limit=3,
    q='*:*'
):  # noqa: E501
    """Get subgraph connected to an entity

    Retrieve the nodes and relationships in a neighborhood around a specified entity.  # noqa: E501

    :param target_id: entity ID
    :type target_id: str
    :param direction: direction in which to collect connected activities
    :type direction: str
    :param sort_by: logic by which to sort matched activities
    :type sort_by: str
    :param order: sort order (ascending or descending)
    :type order: str
    :param limit: maximum number of connected activities to return
    :type limit: int
    :param q: filter results using Lucene Query Syntax in the format of propertyName:value, propertyName:[num1 TO num2] and date range format, propertyName:[yyyyMMdd TO yyyyMMdd]
    :type q: str

    :rtype: Neo4jGraph
    """
    filter_properties = ''
    if q != '*:*':
        tree = parser.parse(q)
        key = ATTR_MAP[tree.name]
        val = quote_string(tree.children[0].value)
        filter_properties = f' {{{key}: {val}}}'
    logger.info(f"FILTER PROPS: {filter_properties}")

    direction_rels = {
        'up': '-[r:WASGENERATEDBY]->',
        'down': '<-[r:USED]-'
    }
    query_base = (
        '''
        MATCH (t:Reference {{target_id: {{target_id}}}}){dir_rel}(s:Activity{filter})
        WITH s
        ORDER BY s.{key}{dir}
        WITH collect(s) as activities
        UNWIND activities[0..{lim}] as t
        MATCH (s)-[r]-(t)
        RETURN s as source, r as relationship, t as target
        '''
    ).format(
        dir_rel=direction_rels[direction],
        key=sort_by,
        dir=(' ' + order.upper()) if order == 'desc' else '',
        lim=limit,
        filter=filter_properties
    )

    results = graph.run(
        query_base,
        target_id=target_id
    )
    return convert_keys(neo4j_export(results.data()))
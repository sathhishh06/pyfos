
# Copyright 2017-18 Brocade Communications Systems LLC.  All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may also obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""

:mod:`pyfos_brocade_fibrechannel_trunk` - PyFOS module to provide REST \
        support for trunking.
*********************************************************************************************************
The :mod:`pyfos_brocade_fibrechannel_trunk` module provides REST support for \
        trunking.
"""

from pyfos import pyfos_rest_util
from pyfos.pyfos_type import pyfos_type
import pyfos.pyfos_version as version


class trunk(pyfos_rest_util.rest_object):
    """
    Class for TrunkShow which shows E_Port trunk information.

    Important Class Members:

        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | Attribute Name                    | Description                    |Frequently Used Methods                                |
        +===================================+================================+=======================================================+
        | group				    | The group index for the trunk. |:func:`peek_group`  		                     |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | master                            | The master port of the trunk.  |:func:`peek_master`                                    |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | source-port                       | The user port numbers of the   |:func:`peek_source_port`                               |
        |                                   | trunk of the local switch.     |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | destination-port                  | The user port numbers of the   |:func:`peek_destination_port`                  	     |
        |                                   | trunk of the remote switch.    |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | neighbor-wwn                      | The fibre channel WWN of the   |:func:`peek_neighbor_wwn`                              |
        |                                   | neighbor switch.               |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | neighbor-switch-name              | The user friendly name of the  |:func:`peek_neighbor_switch_name`                      |
        |                                   | neighbor switch.               |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | neighbor-domain-id                | The domain-id of the neighbor  |:func:`peek_neighbor_domain_id` 	                     |
        |                                   | switch.   		     |                                                       |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+
        | deskew	                    | The link deskew of the trunk.  |:func:`peek_deskew`	                             |
        +-----------------------------------+--------------------------------+-------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns :class:`trunk` objects for all trunk groups gathered \
            from the switch.
            When optional params group and source port params are passed, \
            returns either an object matching the group and source port
            or if no match is found, returns an empty object.
            When these optional params are passed, both should be set.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a
                :class:`trunk` object.


    *Attribute Methods*

        .. method:: peek_group()

            Reads the group in the object.

            :rtype: None or the group.

        .. method:: peek_master()

            Reads the master in the object.

            :rtype: None or the master.

        .. method:: peek_source_port()

            Reads the source port in the object.

            :rtype: None or the source port

        .. method:: peek_destination_port()

            Reads the destination port in the object.

            :rtype: None or the destination port.

        .. method:: peek_neighbor_wwn()

            Reads the neighbor WWN in the object.

            :rtype: None or the neighbor WWN.

        .. method:: peek_neighbor_switch_name()

            Reads the neighbor switch name in the object.

            :rtype: None or the neighbor switch name.

        .. method:: peek_neighbor_domain_id()

            Reads the neighbor domain ID in the object.

            :rtype: None or the neighbor domain ID.

        .. method:: peek_deskew()

            Reads the deskew in the object.

            :rtype: None or the deskew.
    """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.port_trunk_show,
                         "/rest/running/brocade-fibrechannel-trunk/trunk",
                         version.VER_RANGE_821_and_ABOVE)
        self.add(pyfos_rest_util.rest_attribute(
            "group", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "source-port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "destination-port", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor-wwn", pyfos_type.type_wwn,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor-switch-name", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "neighbor-domain-id", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "master", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "deskew", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class performance(pyfos_rest_util.rest_object):
    """
    Class for trunk performance which shows E_Port trunk performance \
     information.

    Important Class Members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute Name                    | Description                   |Frequently Used Methods                                |
        +===================================+===============================+=======================================================+
        | group       		            | Group index for the trunk.    |:func:`peek_group`                               	    |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | tx-bandwidth                      | TX side b/w of the trunk.     |:func:`peek_tx_bandwidth`                              |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | tx-throughput                     | TX side frame transmission    |:func:`peek_tx_throughput`                             |
        |                                   | rate.                         |                                              	    |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | tx-percentage                     | TX side b/w percentage.       |:func:`peek_tx_percentage`                             |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | rx-bandwidth                      | RX side b/w of the trunk.     |:func:`peek_rx_bandwidth`                              |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | rx-throughput                     | RX side frame transmission    |:func:`peek_rx_throughput`                             |
        |                                   | rate.                         |                                              	    |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | rx-percentage                     | RX side b/w percentage.       |:func:`peek_rx_percentage`                             |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | txrx-bandwidth                    | TXRX side b/w of the trunk.   |:func:`peek_txrx_bandwidth`                            |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | txrx-throughput                   | TXRX frame transmission rate. |:func:`peek_txrx_throughput`                           |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | txrx-percentage                   | TXRX side b/w percentage.     |:func:`peek_txrx_percentage`                           |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns a :class:`performance`
            object with values for all attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or
                :class:`performance` object.


    *Attribute Methods*

        .. method:: peek_group()

            Reads the group in the object.

            :rtype: None or the group.

        .. method:: peek_tx_bandwidth()

            Reads the tx bandwidth in the object.

            :rtype: None or the tx bandwidth.

        .. method:: peek_tx_throughput()

            Reads the tx throughput in the object.

            :rtype: None or the tx throughput.

        .. method:: peek_tx_percentage()

            Reads the tx percentage in the object.

            :rtype: None or the tx percentage.

        .. method:: peek_rx_bandwidth()

            Reads the rx bandwidth in the object.

            :rtype: None or the rx bandwidth.

        .. method:: peek_rx_throughput()

            Reads the rx throughput in the object.

            :rtype: None or the rx throughput.

        .. method:: peek_rx_percentage()

            Reads the rx percentage in the object.

            :rtype: None or the rx percentage.

        .. method:: peek_txrx_bandwidth()

            Reads the txrx bandwidth in the object.

            :rtype: None or the txrx bandwidth.

        .. method:: peek_txrx_throughput()

            Reads the txrx throughput in the object.

            :rtype: None or the txrx throughput.

        .. method:: peek_txrx_percentage()

            Reads the txrx percentage in the object.

            :rtype: None or the txrx percentage.

    """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.port_trunk_perf_show,
                         "/rest/running/brocade-fibrechannel-trunk/"
                         "performance",
                         version.VER_RANGE_821_and_ABOVE)
        self.add(pyfos_rest_util.rest_attribute(
            "group", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "tx-bandwidth", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "tx-throughput", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "tx-percentage", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "rx-bandwidth", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "rx-throughput", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "rx-percentage", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "txrx-bandwidth", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "txrx-throughput", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "txrx-percentage", pyfos_type.type_na,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)


class trunk_area(pyfos_rest_util.rest_object):
    """
    Class for port trunk area which shows or configures the \
    port trunk area (F_Port trunk).

    Important Class Members:

        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | Attribute Name                    | Description                   |Frequently Used Methods                                |
        +===================================+===============================+=======================================================+
        | trunk-index                       | The trunk index for the port  |:func:`peek_trunk_index`                               |
        |                                   | trunk area.                   |:func:`set_trunk_index`                                |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | trunk-members/trunk_member        | The trunk members of          |:func:`peek_trunk_members_trunk_member`                |
        |                                   | the trunk.                    |:func:`set_trunk_members_trunk_member`                 |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | master-port                       | The master port of the trunk. |:func:`peek_master_port`                               |
        |                                   |                               |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+
        | trunk-active			    | Whether the trunk is          |:func:`peek_trunk_active`                              |
        |                                   | active or not.	            |                                                       |
        +-----------------------------------+-------------------------------+-------------------------------------------------------+

    *Object Methods*

        .. method:: get()

            Returns a :class:`trunk_area`
            object with values for all attributes.
            The object can be printed using :func:`pyfos_utils.response_print`.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or
                :class:`trunk_area` object.
        .. method:: post()

            Create an entry. The required fields are set within the object \
            using the attribute's set method. This command is used to create
            a new F_Port trunk group or add ports to an existing trunk group.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

        .. method:: delete()

            Delete an entry or entry members. The required fields are
            set within the object using the attribute's
            set method. This command is used to delete a trunk group
            or delete the existing members of the trunk group.
            If all trunk ports are specified,  the
            whole trunk group is deleted.

            :param session: The session handler returned by
                :func:`pyfos_auth.login`.
            :rtype: A dictionary of errors or a success response.

    *Attribute Methods*

        .. method:: set_trunk_index(trunk_index)

            Sets the trunk index in the object.

            :param: The trunk index.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_trunk_index()

            Reads the trunk index in the object.

            :rtype: None or the trunk index.

        .. method:: set_trunk_members_trunk_member(trunk_members)

            Sets trunk_members_trunk_member in the object

            :param: The trunk members.
            :rtype: A dictionary of errors or a success response.

        .. method:: peek_trunk_members_trunk_member()

            Reads the trunk members in the object.

            :rtype: None or the trunk members of the trunk member

        .. method:: peek_master_port()

            Reads the master port in the object.

            :rtype: None or the master port.

        .. method:: peek_trunk_active()

            Reads the trunk active in the object.

            :rtype: None or trunk active.
    """
    def __init__(self, dictvalues={}):
        super().__init__(pyfos_rest_util.rest_obj_type.port_trunk_area,
                         "/rest/running/brocade-fibrechannel-trunk/trunk-area",
                         version.VER_RANGE_821_and_ABOVE)
        self.add(pyfos_rest_util.rest_attribute(
            "trunk-index", pyfos_type.type_int,
            None, pyfos_rest_util.REST_ATTRIBUTE_KEY))
        self.add(pyfos_rest_util.rest_attribute(
            "trunk-members", pyfos_type.type_na,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_CONTAINER))
        self.add(pyfos_rest_util.rest_attribute(
            "trunk-member", pyfos_type.type_str,
            dict(), pyfos_rest_util.REST_ATTRIBUTE_LEAF_LIST),
            ["trunk-members"])
        self.add(pyfos_rest_util.rest_attribute(
            "master-port", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))
        self.add(pyfos_rest_util.rest_attribute(
            "trunk-active", pyfos_type.type_str,
            None, pyfos_rest_util.REST_ATTRIBUTE_NOT_CONFIG))

        self.load(dictvalues, 1)

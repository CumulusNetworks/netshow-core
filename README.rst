netshow core
============

Netshow is Network Abstraction Software. It is optimized to collect core
networking data from devices that contain many network interfaces.

The netshow core respository has 2 main components:

netshow-core-lib:
-----------------

This is core library for retrieving network information from a device
and abstracting it into Python objects.

Its core module is called ``netshowlib``. It contains a few high levels
such as ``iface()`` and ``system_summary()``, that when called, this
calls a provider that retrieves the information from the system.

A *provider* is module that interacts with the base system and converts
relevant network information into python objects. For example, the
*Linux* provider, when the netshow-core-lib ``iface()`` is called, can
retrieve network information like MTU, speed, IP address from device
running a Linux kernel.

Example:
~~~~~~~~

With the Linux provider, retrieve details about the eth1 interface

::

    import netshowlib.netshowlib as nn
    eth1 = nn.iface('eth1')
    >>> eth1.ip_address.allentries
    [u'192.168.50.11/24']
    >>> eth1.lldp
    [{'adj_port': 'swp4', 'adj_mgmt_ip': '192.168.121.242', 'adj_hostname':
    'clswitch'}]
    >>> eth1.is_trunk()
    True
    >>> eth1.is_l3()
    True
    >>>

netshow-core:
-------------

Netshow is responsible printing and analysing the information collected
from the library component of netshow. *netshow-core* is the core
component of this functionality and uses providers (*plugins*) to
properly print and analyse gathered by the ``netshowlib`` component of
the provider(\ *plugin*). For example, the ``print_iface`` wrapper class
in the Linux netshow provider, is responsible for printing linux network
information collected by the Linux provider ``netshowlib`` modules.

Example
~~~~~~~

::

    --------------------------------------------------------------------
    To view the legend,  rerun "netshow" cmd with the  "--legend" option
    --------------------------------------------------------------------
        Name            Speed    MTU    Mode       Summary
    --  --------------  -------  -----  ---------  ----------------------------------------------------------------
    UP  br-mgmt         N/A      1500   Bridge/L3  IP: 192.168.20.11/24
                                                   802.1q Tag: 20
                                                   STP: Disabled
                                                   Untagged Members: veth5WQUVA, veth6WQOHK, veth9QKURD, vethC7T63I
                                                   vethCJVLB0, vethCNHO6U, vethDH3HJN, vethIL9QSD
                                                   vethJE59U0, vethKHX7YP, vethLWHN0S, vethMLNDOE
                                                   vethQUF6ME, vethSNCPD3, vethUI07YQ, vethVN2PUS
                                                   vethX4O674, vethYWI604
                                                   Tagged Members: eth1
    UP  br-vlan         N/A      1500   Bridge/L2  802.1q Tag: Untagged
                                                   STP: Disabled
                                                   Untagged Members: vethMALSDL
    UP  brq087285e9-e4  N/A      1500   Bridge/L2  802.1q Tag: 20
                                                   STP: Disabled
                                                   Untagged Members: tap141463e6-4e, tapfa96896f-f0
                                                   Tagged Members: eth2
    UP  lxcbr0          N/A      1500   Bridge/L3  IP: 10.0.3.1/24
                                                   802.1q Tag: Untagged
                                                   STP: Disabled
                                                   Untagged Members: veth2NPR41, veth4RRO82, veth67W8CB, veth8FTEPM
                                                   veth9AVA9R, vethA6S7T7, vethCEP462, vethD2U7GF
                                                   vethD4TJV0, vethHX8KQC, vethKIP4S8, vethL4R007
                                                   vethOEYR65, vethPSLRGF, vethRQYX9H, vethVAUL56
                                                   vethXC6NM4, vethYTPAWP


Contributing
------------

1. Fork it.
2. Create your feature branch (``git checkout -b my-new-feature``).
3. Commit your changes (``git commit -am 'Add some feature'``).
4. Push to the branch (``git push origin my-new-feature``).
5. Create new Pull Request.

License and Authors
-------------------

Author:: Cumulus Networks Inc.

Copyright:: 2015 Cumulus Networks Inc.

.. figure:: http://cumulusnetworks.com/static/cumulus/img/logo_2014.png
   :alt: Cumulus icon

Cumulus Linux
~~~~~~~~~~~~~

Cumulus Linux is a software distribution that runs on top of industry
standard networking hardware. It enables the latest Linux applications
and automation tools on networking gear while delivering new levels of
innovation and ﬂexibility to the data center.

For further details please see:
`cumulusnetworks.com <http://www.cumulusnetworks.com>`__

This project is licensed under the GNU General Public License, Version
2.0

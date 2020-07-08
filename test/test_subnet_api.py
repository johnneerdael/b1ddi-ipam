# coding: utf-8

"""
    IP Address Management API

    The IPAM/DHCP Application is a BloxOne DDI service providing IP address management and DHCP protocol features. The IPAM component provides visibility into and provisioning tools to manage networking spaces, monitoring and reporting of entire IP address infrastructures, and integration with DNS and DHCP protocols. The DHCP component provides DHCP protocol configuration service with on-prem host serving DHCP protocol. It is part of the full-featured, DDI cloud solution that enables customers to deploy large numbers of protocol servers to deliver DNS and DHCP throughout their enterprise network.     # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import bloxoneddi
from bloxoneddi.api.subnet_api import SubnetApi  # noqa: E501
from bloxoneddi.rest import ApiException


class TestSubnetApi(unittest.TestCase):
    """SubnetApi unit test stubs"""

    def setUp(self):
        self.api = bloxoneddi.api.subnet_api.SubnetApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_subnet_create(self):
        """Test case for subnet_create

        Create the Subnet object.  # noqa: E501
        """
        pass

    def test_subnet_create_next_available_ip(self):
        """Test case for subnet_create_next_available_ip

        Create the Next Available IP object.  # noqa: E501
        """
        pass

    def test_subnet_delete(self):
        """Test case for subnet_delete

        Delete the Subnet object.  # noqa: E501
        """
        pass

    def test_subnet_list(self):
        """Test case for subnet_list

        List Subnet objects.  # noqa: E501
        """
        pass

    def test_subnet_list_next_available_ip(self):
        """Test case for subnet_list_next_available_ip

        List Next Available IP objects.  # noqa: E501
        """
        pass

    def test_subnet_read(self):
        """Test case for subnet_read

        Read the Subnet object.  # noqa: E501
        """
        pass

    def test_subnet_update(self):
        """Test case for subnet_update

        Update the Subnet object.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

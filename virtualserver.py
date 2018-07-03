"""
Create a new Virtual Guest.
createObject() enables the creation of computing instances on an account.
This method is a simplified alternative to interacting with the ordering
system directly.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer

# For nice debug output:
from pprint import pprint as pp

# Your SoftLayer API username and key.
API_USERNAME = 'angel.alcarria.nieto@es.ibm.com'

# Generate one at https://control.softlayer.com/account/users
API_KEY = '23f2648a2a557dc3db0b843215ca0a487f295350c4fe7f71a119f4508df1652c'

orderToRequest = {
    "datacenter": {
        "name": "dal09"
        },
    "dedicatedAccountHostOnlyFlag": "true",
    "domain": "test.local",
    "hostname": "test",
    "hourlyBillingFlag": "true",
    "localDiskFlag": "false",
    "maxMemory": "1024",
    "networkComponents": [
        {
          "maxSpeed": 1000
        }
      ],
    "operatingSystemReferenceCode": "CENTOS_LATEST",
    "startCpus": "1"
    }

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)
productOrderService = client['SoftLayer_Product_Order']

order = {
    'complexType': 'SoftLayer_Container_Product_Order_Virtual_Guest',
    'quantity': 1,
    'virtualGuests': [
        {'hostname': 'test-template', 'domain': 'example.com'}
    ],
    'location': 168642,  # San Jose 1
    'packageId': 46,  # CCI Package
    'prices': [
        {'id': 1640},  # 1 x 2.0 GHz Core
        {'id': 1644},  # 1 GB RAM
        {'id':  905},  # Reboot / Remote Console
        {'id':  272},  # 10 Mbps Public & Private Networks
        {'id':50231},  # 1000 GB Bandwidth
        {'id':   21},  # 1 IP Address
        {'id': 2202},  # 25 GB (SAN)
        {'id': 1684},  # CentOS 5 - Minimal Install (32 bit)
        {'id':   55},  # Host Ping Monitoring
        {'id':   57},  # Email and Ticket Notifications
        {'id':   58},  # Automated Notification Response
        {'id':  420},  # Unlimited SSL VPN Users & 1 PPTP VPN User per account
        {'id':  418},  # Nessus Vulnerability Assessment & Reporting
    ],
    'imageTemplateId': templateId
}


"""
To test the input parameters call the SoftLayer_Virtual_Guest::generateOrderTemplate method
when you are ready to create the server call the createObject method instead.
"""
try:

    # newOrder = client['Virtual_Guest'].generateOrderTemplate(order)
    # pp(newOrder)
    # response = productOrderService.verifyOrder(order)


except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to create a new Virtual Guest faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

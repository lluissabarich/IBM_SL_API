
"""
Create a new Virtual Guest.
createObject() enables the creation of computing instances on an account.
This method is a simplified alternative to interacting with the ordering
system directly.

Important manual pages:
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/generateOrderTemplate
http://sldn.softlayer.com/reference/services/SoftLayer_Virtual_Guest/createObject
http://sldn.softlayer.com/reference/datatypes/SoftLayer_Virtual_Guest
https://softlayer.github.io/python/create_server_simplified.py/
License: http://sldn.softlayer.com/article/License
Author: SoftLayer Technologies, Inc. <sldn@softlayer.com>
"""
import SoftLayer
import sys

# For nice debug output:
from pprint import pprint as pp

# Generate one at https://control.softlayer.com/account/users
API_KEY = sys.argv[1] #he creado mi API_KEY en SoftLayer
API_USERNAME = sys.argv[2] #tipo 304454_user@xx.xxx.xxx
print(API_KEY,API_USERNAME)

orderToRequest = {
    "privateNetworkOnlyFlag": True,  # Specifies the billing type for the server.
    "private": True,
    "hostname": "hostApplus",  # The name of the server
    "domain": "example.com",  # The domain for the server
    "startCpus": 1,  # The number of logical CPU cores to allocate
    "maxMemory": 1,  # The amount of memory to allocate in gigabytes.
    "localDiskFlag": False,  # Indicates that the vsi has at least one disk local to the host it runs on.
                             # This does not include a SWAP device.
    "hourlyBillingFlag": True,  # Specifies the billing type for the server.
    "operatingSystemReferenceCode": "UBUNTU_LATEST",  # An identifier for the operating system to
                                                      # provision the server with.
    "datacenter": {  # Specifies which datacenter the server is to be provisioned in.
        "name": "ams01"
        },
    "userData": [
        {
            "value": "someValue"
        }
     ]
    }

client = SoftLayer.create_client_from_env(
    username=API_USERNAME,
    api_key=API_KEY
)
productOrderService = client['SoftLayer_Product_Order']
virtualGuestService = client['SoftLayer_Virtual_Guest']


"""
To test the input parameters call the SoftLayer_Virtual_Guest::generateOrderTemplate method
when you are ready to create the server call the createObject method instead.
"""
try:

    newOrder = virtualGuestService.createObject(orderToRequest)
    pp(newOrder)
    # response = productOrderService.verifyOrder(orderToRequest)


except SoftLayer.SoftLayerAPIError as e:
        pp('Unable to create a new Virtual Guest faultCode=%s, faultString=%s'
            % (e.faultCode, e.faultString))

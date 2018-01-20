import keystoneclient.v2_0.client as ksclient			# Import keystoneclient
import novaclient.client as novclient				# Import novaclient
from keystoneauth1 import loading				# Import loading lib
from keystoneauth1 import session				# Import session lib

keystone = ksclient.Client(auth_url='http://172.16.0.2:5000/v2.0',
                           username= 'admin',
                           password= 'admin',
                           tenant_name= 'TestProject',
                           region_name= 'RegionOne')			# Create a keystone client

nova = novclient.Client('2', 'admin','admin', 'ff94160bbc1c494999f4399ff46009e3', "http://172.16.0.2:5000")					# Create nova client

loader = loading.get_plugin_loader('password')                  # 'password' is the entrypoint

auth = loader.load_from_options(auth_url="http://172.16.0.2:5000/v2.0", username='admin', password='admin', project_id='64e2105c263144a68133dcc47e2dad4d')

sess = session.Session(auth=auth)

nova = novclient.Client('2.0', session=sess)         # Arguments are version number and session

image = nova.images.find(name="TestVM")                           # Choosing image called 'TestVM'

flavor = nova.flavors.find(name="m1.micro")		# Choosing flavor

network = nova.networks.find(label="net04_ext") 		# Choosing network

instance1 = nova.servers.create(name = "Testthing", image = image.id, flavor = flavor.id, nics = [{'net-id':network.id}], key_name = 'mykey')	            # Instantiating a VM with parameters

print nova.servers.list()                       		# Print all VMs
print instance1.status				# Print the instantiated VM status

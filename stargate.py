"""
Script that logs into Cisco DNA Center always on sandbox,
returns the number of current devices, and gives 
location, type and role data

"""
#================================================================================
#import-palooza!

#suppressing the certificate warning as it's driving me nuts
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#importing pprint to make the output 'pretty'
import pprint
#importing getpass for password security
import getpass
#import requests library and basic HTTP auth to pass a username and password
import requests
from requests.auth import HTTPBasicAuth

#==================================================================================


#==================================================================================
#Defines global variables we don't want changed
#The theme is Stargate!

#prompting user for username
#incase you forget - username = devnetuser, password = Cisco123!
CHEVERON_ONE = input("Please enter your username: ")
#prompting user for password using a secure method
ENCODED = getpass.getpass()
LOCKED = "https://sandboxdnac.cisco.com/api/system/v1/auth/token"

#==================================================================================
#Collect your token!

#Create dictionary for the response payload, headers, in this we are doing an http post
#so we need to specify the content type we are sending rather than accepting a format

kree = {'Content-Type': 'application/json'}

#creates a response variable with the value of our post request 

openTheIris = requests.post(LOCKED, auth=HTTPBasicAuth(CHEVERON_ONE, ENCODED), headers=kree, verify=False)

#converts our respone to json format and stores it in our variable resposneJSON

tokra = openTheIris.json()['Token']

#prints responseJSON variable

print("Your generated token is:\n" + tokra)
print()

#==================================================================================


#==================================================================================
#let's do something crazy and count our machines before they hatch!

HARCESIS = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device/count"

#Creates dictionary for follow up get request headers specifying the format as JSON and
#passing the value for the token from the variable above.

omaDesala = {'Accept': 'application/json', 'X-auth-token': tokra}

#Creates object thisIsStargateCommand with the contents of our http get request to the HARCESIS variable
#passing our omaDesala dictionary and not verifying the cert validity since it is self signed 

thisIsStargateCommand = requests.get(HARCESIS, headers=omaDesala, verify=False)

gateAddresses = thisIsStargateCommand.json()['response']

print("Retrieving data from {} devices:".format(gateAddresses))
print()


#==================================================================================


#==================================================================================
#Now let's get the location name, location, type, and role of those machines!

#Creates a variable REPOSITORY_OF_KNOWLEDGE and assigns the value of the follow up API request
#to DNA Center

REPOSITORY_OF_KNOWLEDGE = "https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device"

#Creates dictionary for follow up get request headers specifying the format as JSON and
#passing the value for the token from the variable above.

replicators = {'Accept': 'application/json', 'X-auth-token': tokra}

#Creates object indeed with the contents of our http get request to the REPOSITORY_OF_KNOWLEDGE variable
#passing our replicators dictionary and not verifying the cert validity since it is self signed 

indeed = requests.get(REPOSITORY_OF_KNOWLEDGE, headers=replicators, verify=False)

offworldActivity = indeed.json()['response']

#Setting up a for loop that will loop through each device and retrieve the pertinent information

for situation in offworldActivity:
	p5x777 = situation['locationName']
	furlingHomeworld = situation['location']
	furlings = situation['type']
	allianceMember = situation['role']
	#Printing out the collected information in an easy to read format
	print("The device at {} {} is a {} that performs {}".format(p5x777, furlingHomeworld, furlings, allianceMember))

#================================================================================
#End of script!

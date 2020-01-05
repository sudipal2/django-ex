import os
import json
import requests
import ibm_boto3
import urllib2
from ibm_botocore.client import Config, ClientError

try:
    _credentials_string = os.environ.get('IBM_CLOUD_STO_CREDENTIALS')
    print('credentials :: ', _credentials_string)
    cos_service_credentials = json.loads(_credentials_string)
    #print "Service START Point    "
    # Request detailed enpoint list
    endpoints = requests.get(cos_service_credentials['endpoints']).json()

    # setup other details
    iam_host = (endpoints['identity-endpoints']['iam-token'])
    cos_host = (endpoints['service-endpoints']['regional']['us-south']['public']['us-south'])
    auth_endpoint = "https://" + iam_host + "/oidc/token"
    service_endpoint = "https://" + cos_host
   
    #print "Service End Point    ",service_endpoint
    # Create resource
    cos = ibm_boto3.resource("s3",
        ibm_api_key_id=cos_service_credentials['apikey'],
        ibm_service_instance_id=cos_service_credentials['resource_instance_id'],
        ibm_auth_endpoint=auth_endpoint,
        config=Config(signature_version="oauth"),
        endpoint_url=service_endpoint
    )
except:
    print('unable to create cos')

def get_item(bucket_name, item_name):
    print("Retrieving item {0} from bucket {1}".format(item_name, bucket_name))
    try:
        obj = cos.Object(bucket_name, item_name).get()
        return obj['Body'].read()
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
        return False
    except Exception as e:
        print("Unable to retrieve file contents: {0}".format(e))
        return False

def get_all_items(bucket_name):
    item_name = "ALL"
    itemid_url="http://redhawkserverapi-red-hawk.gamification-d3c0cb24e2b77f6869027abe3de4bca3-0001.sng01.containers.appdomain.cloud/api/getproductids/"
    id_f = requests.get(itemid_url)
    print (id_f.text)

    #print("Retrieving All from bucket {1}".format(item_name, bucket_name))
    try:
        obj = cos.Object(bucket_name, item_name).get()
        return obj['Body'].read()
    except ClientError as be:
        print("CLIENT ERROR: {0}\n".format(be))
        return False
    except Exception as e:
        print("Unable to retrieve file contents: {0}".format(e))
        return False

#!/usr/bin/env python
from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', aws_access_key_id='',aws_secret_access_key='',region_name='us-west-2')#endpoint_url='dynamodb.us-west-2.amazonaws.com')

table = dynamodb.Table('mytable')

#print("Movies from 1985")

response = table.query(
    KeyConditionExpression=Key('serialnumber').eq('rest')&Key('eachvalue').eq('1491769916238')
)

for i in response['Items']:
    print(i['serialnumber'], ":", i['eachvalue'])
    print(json.dumps(i, cls=DecimalEncoder))


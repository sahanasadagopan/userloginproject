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

dynamodb = boto3.resource('dynamodb',aws_access_key_id='AKIAI7F4R3OPDJQSDT7A',aws_secret_access_key='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',region_name='us-west-2')

table = dynamodb.Table('mytable')

filter = Key('eachvalue').eq('1491769916238');
pe = "#serialnumber"#yr, title, info.rating"
# Expression Attribute Names for Projection Expression only.
ean = { "#serialnumber": "eac", }
esk = None
#print(ean)


response = table.scan(
    FilterExpression=Attr('payload.password').eq('san')
    )

for i in response['Items']:
    
    print(json.dumps(i, cls=DecimalEncoder))
#print(response['Items'])


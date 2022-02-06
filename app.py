from uuid import uuid4
from chalice import Chalice
import os
import boto3

app = Chalice(app_name='TODO')

app.debug = True


class DynamoDB:
    def __init__(self, table_resource):
        self._table = table_resource

    def get_todos(self):
        response = self._table.scan()
        return response['Items']

    def add_todo(self, description, data=None):
        uid = str(uuid4())
        self._table.put_item(
            Item={
                'id': uid,
                'description': description,
                'state': 'unstarted',
                'data': data if data else {},
            }
        )
        return uid


database = DynamoDB(boto3.resource('dynamodb').Table(os.environ['TABLE_NAME']))


@app.route('/todos', methods=['GET'])
def get_todos():
    return database.get_todos()


@app.route('/add_record', methods=['POST'])
def add_new_todo():
    body = app.current_request.json_body
    return database.add_todo(
        description=body['description'],
        data=body.get('data'),
    )


@app.route('/test_db')
def test_ddb():
    resource = boto3.resource('dynamodb')
    table = resource.Table(os.environ['TABLE_NAME'])
    return table.name

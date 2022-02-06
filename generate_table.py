import os
import uuid
import json
import boto3

TABLE = {
    'prefix': 'todo_api',
    'environment_var': 'TABLE_NAME',
    'hash_key': 'description',
    'range_key': 'id'
}


def create_table(prefix, hash_key, range_key=None):  
    table_name = f'{prefix}-{str(uuid.uuid4())}'
    client = boto3.client('dynamodb')
    key_schema = [
        {
            'AttributeName': hash_key,
            'KeyType': 'HASH',
        }
    ]
    attribute_definitions = [
        {
            'AttributeName': hash_key,
            'AttributeType': 'S',
        }
    ]
    if range_key is not None:
        key_schema.append({'AttributeName': range_key, 'KeyType': 'RANGE'})
        attribute_definitions.append(
            {'AttributeName': range_key, 'AttributeType': 'S'})
    client.create_table(
        TableName=table_name,
        KeySchema=key_schema,
        AttributeDefinitions=attribute_definitions,
        ProvisionedThroughput={
            'ReadCapacityUnits': 5,
            'WriteCapacityUnits': 5,
        }
    )
    waiter = client.get_waiter('table_exists')
    waiter.wait(TableName=table_name, WaiterConfig={'Delay': 1})
    return table_name


def record_env_var(key, value):  
    with open(os.path.join('.chalice', 'config.json')) as f:
        data = json.load(f)
        # data['stages'].setdefault(stage, {}).setdefault(
        #     'environment_variables', {}
        # )[key] = value
        data.setdefault('environment_variables', {})[key] = value

    with open(os.path.join('.chalice', 'config.json'), 'w') as f:
        serialized = json.dumps(data, indent=2, separators=(',', ': '))
        f.write(serialized + '\n')


def main():
    table = create_table(
        TABLE['prefix'], TABLE['hash_key'],
        TABLE.get('range_key')
    )
    record_env_var(TABLE['environment_var'], table)


if __name__ == '__main__':
    main()

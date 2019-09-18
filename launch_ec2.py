import boto3
client = boto3.client('ec2')
resp = client.run_instances(ImageId='ami-047de52e23df900b7',
                            InstanceType='t1.micro',
                            MinCount=1,
                            MaxCount=1)
for instance in resp['Instances']:
    print(instance['InstanceId'])
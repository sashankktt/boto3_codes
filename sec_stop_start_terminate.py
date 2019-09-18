import boto3
client = boto3.client('ec2')
#client.start_instances(InstanceIds=['i-0669b0c1da4ca1904'])
#client.stop_instances(InstanceIds=['i-0669b0c1da4ca1904'])
client.terminate_instances(InstanceIds=['i-0669b0c1da4ca1904'])
for instance in resp['TerminatingInstances']:
    print("The instance with instanceid {} is termnated".format(instance['InstanceId']))
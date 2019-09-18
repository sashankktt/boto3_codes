import boto3
ec2 = boto3.resource('ec2')
sns_client = boto3.client('sns')
backup_filter = [
    {
        'Name':'tag:Backup',
        'Values':['Yes']
    }
]
snapshot_ids=[]
for instance in ec2.instances.filter(Filter=backup_filter):
    for vol in instance.volumes.all():
        snapshot = vol.create_snapshot(Description='Created by boto3')
        snapshot_ids.append(snapshot.snapshot_id)

# Create an amazon sns service through the aws console, verify your email address
# and copy the ARN created 
sns_client.publish(
    TopicArn ='<arn_name>',
    Subject = 'EBS Snapshot',
    Message = snapshot_ids
)
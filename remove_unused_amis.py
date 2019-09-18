import boto3

client = boto3.client('ec2')

instances = client.describe_instances()
used_amis = []

for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        used_amis.append(instance['ImageId'])

print(used_amis)


def remove_duplicates(amis):
    unique_amis = []
    for ami in amis:
        if ami not in unique_amis:
            unique_amis.append(ami)
    return unique_amis


unique_amis = remove_duplicates(used_amis)
print(unique_amis)

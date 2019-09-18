import boto3
ec2 = boto3.resource('ec2')
# Remember we should ensure to have describe instances permission in the policy
def lambda_handler(event,context):
    filter = [
        {
            'Name':'tag:Type',
            'Values':['Scheduled']
        }
    ]

    instances = ec2.instances.filter(Filter=filter)
    for instance in instances:
    instance.start()
    #instance.stop()
    return "Success !!"
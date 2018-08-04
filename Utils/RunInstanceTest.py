import boto3

client = boto3.client("ec2")
client.run_instances(MaxCount=1, MinCount=1, ImageId='ami-ffd00992')
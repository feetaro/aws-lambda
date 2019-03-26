import boto3

def lambda_handler(event, context):
    # TODO implement
	rds = boto3.client('rds')
	response = rds.delete_db_instance(
		DBInstanceIdentifier='[instance_nmame]',
		SkipFinalSnapshot=True
	)
	print(response)
	return 0

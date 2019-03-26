import boto3

def lambda_handler(event, context):
    # TODO implement
	rds = boto3.client('rds')
	response = rds.create_db_instance(
		Engine='aurora',
		DBClusterIdentifier='[cluster_name]',
		DBInstanceIdentifier='[instance_name]',
		DBInstanceClass='db.r4.xlarge',
		PubliclyAccessible=False,
		DBParameterGroupName='[parameter_group_name]',
		PromotionTier=15
	)
	print(response)
	return 0

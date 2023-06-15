import boto3

# Create a Glue client
glue_client = boto3.client('glue')

# Define the Glue job parameters
job_name = 'CSVToParquetJob'
script_location = 's3://capstoneproject-bucket/covid19testing/csv_to_parquet.py'
csv_path = 's3://capstoneproject-bucket/covid19testing/states_current_csv/'
parquet_path = 's3://capstoneproject-bucket/covid19testing/parquet-folder/'

# Create the Glue job
response = glue_client.create_job(
    Name=job_name,
    Role='arn:aws:iam::667409444611:role/project-glue-service-role',
    Command={
        'Name': 'glueetl',
        'ScriptLocation': script_location,
    },
    DefaultArguments={
        '--input_path': csv_path,
        '--output_path': parquet_path,
        '--TempDir': 's3://my-glue-temp-bucket/',
    },
    ExecutionProperty={
        'MaxConcurrentRuns': 1,
    },
    Timeout=2880,
    MaxCapacity=5.0,
)

# Start the Glue job
glue_client.start_job_run(JobName=job_name)

aws glue create-job --name "MyGlueJob" --role "arn:aws:iam::123456789012:role/GlueServiceRole" --command '{"Name": "glueetl", "ScriptLocation": "s3://my-bucket/glue-scripts/my-script.py"}' --default-arguments '{"--job-bookmark-option": "job-bookmark-disable"}'

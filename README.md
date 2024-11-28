## Using Localstack Lambda

``
awslocal lambda create-function \
    --function-name create-embedding-lambda \
    --runtime python3.9 \
    --zip-file fileb://function.zip \
    --handler create_embedding.lambda_handler \
    --role arn:aws:iam::000000000000:role/lambda-role

awslocal lambda invoke \
    --function-name create-embedding-lambda \
    --payload '{"company": {"name": "Empresa X", "description": "Uma empresa focada em tecnologia de ponta."}}' output.txt

``

## Using python

`python invoke.py`

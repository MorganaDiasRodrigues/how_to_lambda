import boto3
import json

# Configurações para conectar no LocalStack
lambda_client = boto3.client(
    'lambda',
    region_name='us-east-1',
    endpoint_url='http://localhost:4566'  # Endpoint do LocalStack
)

def invoke_lambda_and_get_embedding():
    # Payload para enviar à Lambda
    payload = {
        "company": {
            "name": "Empresa X",
            "description": "Uma empresa focada em tecnologia de ponta."
        }
    }

    # Invocando a função Lambda
    response = lambda_client.invoke(
        FunctionName='create-embedding-lambda',  # Nome da sua Lambda
        InvocationType='RequestResponse',  # Espera pela resposta
        Payload=json.dumps(payload)  # Serializa o payload em JSON
    )

    # Lendo a resposta
    response_payload = json.loads(response['Payload'].read())

    # Extraindo apenas o embedding da resposta
    if 'embedding' in response_payload['body']:
        embedding = json.loads(response_payload['body'])['embedding']
        return embedding
    else:
        raise ValueError(f"Erro ao buscar embedding: {response_payload}")

# Chamando a função e imprimindo o embedding
if __name__ == "__main__":
    embedding = invoke_lambda_and_get_embedding()
    print("Embedding recebido:", embedding)

import json
import asyncio

# Simula a criação de embeddings (função assíncrona)
async def create_embedding(company: dict):
    # in real life we'll be doing
    # openai_client = AsyncOpenAI()
    # embedding = openai_client.embeddings.create(input=company["description"], ...)
    # return embedding
    return [0] * 256

# Função principal da Lambda
def lambda_handler(event, context):
    """
    AWS Lambda handler. Aceita um evento com os dados da empresa,
    cria embeddings e retorna o resultado.

    :param event: Evento recebido pela Lambda (deve conter `company`).
    :param context: Contexto de execução da Lambda.
    :return: Dicionário com o resultado.
    """
    try:
        # Extraindo dados do evento
        company = event.get('company')
        if not company or 'description' not in company:
            raise ValueError("O evento deve conter o campo 'company' com uma 'description'.")

        # Executando a função assíncrona em um contexto síncrono
        embedding = asyncio.run(create_embedding(company=company))

        # Retorna o resultado
        return {
            'statusCode': 200,
            'body': json.dumps({'embedding': embedding})
        }
    
    except Exception as e:
        # Tratamento de erros
        return {
            'statusCode': 400,
            'body': json.dumps({'error': str(e)})
        }


# Teste local
if __name__ == "__main__":
    test_event = {
        "company": {
            "name": "Empresa X",
            "description": "Uma empresa focada em tecnologia de ponta."
        }
    }
    response = lambda_handler(test_event, None)
    print(response)
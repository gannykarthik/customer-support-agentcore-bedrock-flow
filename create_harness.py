import boto3
import json
import uuid
import sys

REGION = "us-east-1"

HARNESS_NAME = "customer-support-agent"
GATEWAY_NAME = "bug-report-agentcore-gateway"
EXECUTION_ROLE_NAME = "bug-report-tool-stack-harness-role"

MODEL_ID = "amazon.nova-lite-v1:0"

SYSTEM_PROMPT_FILE = "system_prompt.txt"
FAQ_FILE = "online_shop_faq.md"


def get_role_arn():
    iam = boto3.client("iam")

    response = iam.get_role(
        RoleName=EXECUTION_ROLE_NAME
    )

    return response["Role"]["Arn"]


def get_gateway_arn():
    control = boto3.client(
        "bedrock-agentcore-control",
        region_name=REGION
    )

    paginator = control.get_paginator("list_gateways")

    for page in paginator.paginate():
        for gateway in page.get("items", []):
            if gateway.get("name") == GATEWAY_NAME:
                return gateway["gatewayArn"]

    raise RuntimeError(
        f"Gateway '{GATEWAY_NAME}' was not found in {REGION}."
    )


def build_system_prompt():
    with open(
        SYSTEM_PROMPT_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        prompt = f.read()

    with open(
        FAQ_FILE,
        "r",
        encoding="utf-8"
    ) as f:
        faq = f.read()

    return prompt.replace("{{FAQ}}", faq)


def create_harness():
    control = boto3.client(
        "bedrock-agentcore-control",
        region_name=REGION
    )

    role_arn = get_role_arn()
    gateway_arn = get_gateway_arn()
    system_prompt = build_system_prompt()

    print("Execution role:")
    print(role_arn)

    print("\nGateway:")
    print(gateway_arn)

    print("\nCreating harness...")

    response = control.create_harness(
        harnessName=HARNESS_NAME,
        clientToken=str(uuid.uuid4()),
        executionRoleArn=role_arn,

        systemPrompt=[
            {
                "text": system_prompt
            }
        ],

        model={
            "bedrockModelConfig": {
                "modelId": MODEL_ID,
                "maxTokens": 2048,
                "temperature": 0.0,
                "apiFormat": "converse_stream"
            }
        },

        tools=[
            {
                "type": "agentcore_gateway",
                "name": "bug-report-gateway",
                "config": {
                    "agentCoreGateway": {
                        "gatewayArn": gateway_arn,
                        "outboundAuth": {
                            "awsIam": {}
                        }
                    }
                }
            }
        ],

        maxIterations=10,
        timeoutSeconds=300,

        tags={
            "Project": "customer-support-agentcore-bedrock-flow",
            "Purpose": "Customer support chatbot"
        }
    )

    print("\n========================================")
    print("HARNESS CREATED")
    print("========================================")

    print(json.dumps(response, indent=2, default=str))


if __name__ == "__main__":
    try:
        create_harness()
    except Exception as e:
        print("\nERROR:")
        print(type(e).__name__)
        print(str(e))
        sys.exit(1)
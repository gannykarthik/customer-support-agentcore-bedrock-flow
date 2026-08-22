# Customer Support Chatbot — Amazon Bedrock Flows
### By Ganapathi Karthik | Udacity Agentic AI Engineer Nanodegree

---

A fully working **customer support chatbot** built on **Amazon Bedrock Flows**, capable of intelligently routing customer messages into three specialized handling paths:

- 🐛 **Bug Reports** → Bedrock Agent collects details and files a ticket
- ❓ **Platform Questions** → FAQ-grounded answers using a Prompt node
- 🤝 **Other Requests** → Polite redirect to human support

---

## How It Works

When a customer sends a message, the flow:

1. **Classifies** it using a Prompt node (classifier returns `BUG_REPORT`, `PLATFORM_QUESTION`, or `OTHER`)
2. **Routes** it via a Condition node using exact string matching
3. **Handles** it in the appropriate branch — Agent, FAQ Prompt, or Human Support Prompt
4. **Responds** through one of three dedicated Output nodes

```
Customer Message
      │
      ▼
[Classifier Prompt]
      │
      ▼
[Condition Node]
  ├── BUG_REPORT       → [Bedrock Agent] → [BugReportOutput]
  ├── PLATFORM_QUESTION → [FAQ Prompt]   → [FAQOutput]
  └── default (OTHER)  → [Human Support Prompt] → [OtherOutput]
```

---

## Project Files

| File | Description |
|------|-------------|
| `cloudformation-tool.yaml` | Deploys Lambda (`create-bug-report`) + DynamoDB (`BugReports`) + IAM role |
| `cloudformation-testing.yaml` | Deploys S3 bucket + IAM role for Bedrock Evaluations |
| `create_bug_report.py` | Lambda function — writes bug tickets to DynamoDB, returns a ticket ID |
| `generate-eval-dataset.py` | Runs flow tests programmatically → generates JSONL for Bedrock Evaluations |
| `flow-tests-template.json` | Template skeleton for building the test suite |
| `flow-tests.json` | My complete test suite (13 cases: BUG_REPORT, PLATFORM_QUESTION, OTHER, edge cases) |
| `online_shop_faq.md` | The fictional online shop FAQ embedded in the FAQ Prompt node |
| `requirements.txt` | Python dependencies (boto3, etc.) |
| `IMPLEMENTATION_GUIDE.md` | Step-by-step implementation guide for every node and configuration |
| `EVALUATION_OBSERVATIONS.md` | Template to record Bedrock Evaluation results |

---

## Getting Started

### Prerequisites

- AWS account with Bedrock access enabled (`us-east-1` region)
- AWS CLI configured (`aws configure`)
- Python 3.9+ with dependencies installed

### Step 1 — Deploy Infrastructure

```bash
pip install -r requirements.txt

# Deploy Lambda + DynamoDB
aws cloudformation deploy \
  --template-file cloudformation-tool.yaml \
  --stack-name bug-report-tool \
  --capabilities CAPABILITY_NAMED_IAM \
  --region us-east-1

# Deploy S3 + Eval IAM role
aws cloudformation deploy \
  --template-file cloudformation-testing.yaml \
  --stack-name bedrock-eval-testing \
  --capabilities CAPABILITY_NAMED_IAM \
  --region us-east-1
```

### Step 2 — Build the Bedrock Flow

See [IMPLEMENTATION_GUIDE.md](IMPLEMENTATION_GUIDE.md) for the complete node-by-node setup.

Key decisions I made:
- **Classifier model**: `amazon.nova-lite-v1:0` at temperature `0` for deterministic output
- **Condition routing**: exact `==` match on classifier output; default branch catches OTHER
- **Agent**: enabled "User input" so it can ask follow-up questions for vague bug reports
- **FAQ**: embedded directly in the Prompt node (no RAG needed for a 32-item FAQ)
- **No phone number**: the FAQ doesn't contain one — I don't invent contact details

### Step 3 — Run Tests

```bash
python generate-eval-dataset.py \
  --tests-json flow-tests.json \
  --flow-id <YOUR_FLOW_ID> \
  --flow-alias-id <YOUR_FLOW_ALIAS_ID> \
  --model-identifier customer-support-chatbot \
  --out-jsonl output_eval_dataset.jsonl \
  --region us-east-1
```

### Step 4 — Run Bedrock Evaluation

```bash
# Upload JSONL to S3
aws s3 cp output_eval_dataset.jsonl \
  s3://udacity-agentic-engineer-c1-eval-<ACCOUNT_ID>/eval-input/output_eval_dataset.jsonl \
  --region us-east-1
```

Then create a Bedrock Evaluation job (LLM-as-a-judge / BYOI) in the AWS console using `bedrock-eval-role` and judge model `amazon.nova-pro-v1:0`.

---

## Test Coverage

My `flow-tests.json` covers:

| Category | Test IDs | What's tested |
|----------|----------|---------------|
| BUG_REPORT | bug-001 | Clear checkout crash |
| BUG_REPORT | bug-002 | Vague report → agent asks for clarification |
| BUG_REPORT | bug-003 | Different page bug (search filter) |
| PLATFORM_QUESTION | platform-001 | Order tracking (FAQ Q9) |
| PLATFORM_QUESTION | platform-002 | Delivery time (FAQ Q8) |
| PLATFORM_QUESTION | platform-003 | Return policy (FAQ Q11) |
| PLATFORM_QUESTION | platform-004 | Payment declined (FAQ Q20) |
| PLATFORM_QUESTION | platform-005 | Same-day delivery (not in FAQ — should not hallucinate) |
| OTHER | other-001 | Off-topic request |
| OTHER | other-002 | Requests human agent |
| Edge case | edge-001 | Single word: "help" |
| Edge case | edge-002 | Ambiguous: "It doesn't work" |
| Edge case | edge-003 | Prompt injection attempt |

---

## Architecture Decisions

**Why three separate Output nodes?**
Bedrock Flows does not allow a single Output node to receive connections from multiple branches. Each branch requires its own Output node.

**Why temperature 0 on the classifier?**
Condition nodes use exact string matching. Even a single trailing newline breaks the match. Temperature 0 gives the most stable, predictable output from the model.

**Why embed the FAQ in the prompt instead of using a Knowledge Base?**
The FAQ is 32 items — small enough to fit in a prompt without hitting context limits. RAG (Knowledge Bases) would add complexity without benefit at this scale.

**Why is there no phone number?**
The provided `online_shop_faq.md` does not contain a support phone number. I use only the contact method the FAQ actually specifies: the help/contact form and replying to order emails.

---

## Built With

- [Amazon Bedrock Flows](https://docs.aws.amazon.com/bedrock/latest/userguide/flows.html)
- [Amazon Bedrock Agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
- [Amazon Bedrock Evaluations](https://docs.aws.amazon.com/bedrock/latest/userguide/evaluation.html)
- [AWS Lambda](https://aws.amazon.com/lambda/)
- [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)
- [Amazon S3](https://aws.amazon.com/s3/)

---

## Notes on Starter Files

The following files were provided as course starter materials for this Udacity project:
`cloudformation-tool.yaml`, `cloudformation-testing.yaml`, `create_bug_report.py`,
`generate-eval-dataset.py`, `flow-tests-template.json`, `online_shop_faq.md`, `requirements.txt`.

All implementation decisions, test cases, prompts, agent instructions, and documentation
are my own original work.

## License

MIT

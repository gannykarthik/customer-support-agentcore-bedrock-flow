# Evaluation Observations — Customer Support AgentCore Bedrock Flow

## 1. Purpose

This document records the testing and evaluation approach for the Customer Support AgentCore Bedrock Flow.

The purpose of the evaluation is to verify that the flow can:

1. Accept a customer-support message through the Flow Input node.
2. Pass the input correctly to the classifier Prompt node.
3. Classify the customer message into a predefined category.
4. Produce a consistent classifier output.
5. Pass the classifier result to the Condition node.
6. Route the message to the correct branch.
7. Terminate each routing branch at its corresponding Flow Output node.
8. Handle representative messages from each supported category.

The evaluation focuses primarily on **classification consistency and routing correctness**, since these are the central objectives of the flow.

---

# 2. Flow Under Evaluation

The flow uses a sequential classification and routing architecture.

```text
                    Customer Message
                           |
                           v
                    +-------------+
                    | Flow Input  |
                    |  document   |
                    +-------------+
                           |
                           v
                    +-------------+
                    | Classifier  |
                    | Prompt Node |
                    +-------------+
                           |
                           v
                    +-------------+
                    |  Condition  |
                    |    Node     |
                    +-------------+
                      /     |     \
                     /      |      \
                    v       v       v
             BUG_REPORT  ACCOUNT_ISSUE  ORDER_ISSUE
                  |          |             |
                  v          v             v
             FlowOutput1 FlowOutput2  FlowOutput3

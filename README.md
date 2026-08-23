# Customer Support AgentCore Bedrock Flow

A customer-support message classification and conditional routing workflow built using Amazon Bedrock Flows.

---

## Overview

This project implements a customer-support classification and routing workflow using Amazon Bedrock Flows.

The workflow receives an incoming customer message through a Flow Input node, sends the message to a Prompt-based classifier, and uses the classifier result to determine the appropriate routing path through a Condition node.

The flow is designed around three distinct customer-support categories:

- `BUG_REPORT`
- `ACCOUNT_ISSUE`
- `ORDER_ISSUE`

Each category has its own routing path and terminates at a separate Flow Output node.

The architecture demonstrates how a foundation model can be used for natural-language classification while deterministic workflow logic handles the subsequent routing.

---

## Project Objectives

The primary objectives of this project are to:

1. Accept a customer-support message as flow input.
2. Pass the customer message to a Prompt-based classifier.
3. Classify the message into a predefined category.
4. Produce a consistent classifier result suitable for downstream routing.
5. Use a Condition node to evaluate the classification result.
6. Route each category through a distinct path.
7. Terminate each category-specific path at a separate Flow Output node.
8. Validate the overall Bedrock Flow configuration.
9. Test the classification and routing behavior with representative customer messages.

---

## Architecture

The overall flow architecture is:

```text
                    Customer Message
                           |
                           v
                    +-------------+
                    |  Flow Input |
                    +-------------+
                           |
                           | document
                           v
                 +---------------------+
                 |   Prompt Classifier |
                 |                     |
                 |  customer_message   |
                 +---------------------+
                           |
                           | classification
                           v
                  +------------------+
                  |  Condition Node  |
                  +------------------+
                    /       |       \
                   /        |        \
                  v         v         v
          +-----------+ +-----------+ +-----------+
          | BUG_REPORT| | ACCOUNT_  | | ORDER_    |
          |           | | ISSUE     | | ISSUE     |
          +-----------+ +-----------+ +-----------+
                |            |             |
                v            v             v
          +-----------+ +-----------+ +-----------+
          |  Output 1 | |  Output 2 | |  Output 3 |
          +-----------+ +-----------+ +-----------+
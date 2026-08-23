# Evaluation Observations — Customer Support AgentCore Bedrock Flow

## 1. Project Overview

This project implements a customer-support message classification and routing workflow using Amazon Bedrock Flows.

The flow accepts a customer message through the Flow Input node, sends the message to a classifier Prompt node, and routes the classifier result through a Condition node.

The classifier is designed to produce one of three predefined categories:

- `BUG_REPORT`
- `ACCOUNT_ISSUE`
- `ORDER_ISSUE`

The Condition node uses exact string matching to route each classification to its corresponding Flow Output node.

### Flow Architecture

```text
Customer Message
       |
       v
+-------------------+
|   Flow Input      |
|    document       |
+-------------------+
       |
       v
+-------------------+
|     Classifier    |
|    Prompt Node    |
+-------------------+
       |
       v
+-------------------+
|  Condition Node   |
+-------------------+
     /     |      \
    /      |       \
   v       v        v
BUG_     ACCOUNT_  ORDER_
REPORT    ISSUE     ISSUE
   |        |        |
   v        v        v
Output 1  Output 2  Output 3

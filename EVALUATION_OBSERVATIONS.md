# Evaluation Observations
## Project: Customer Support Chatbot with Amazon Bedrock Flows

---

## Evaluation Run 1

### Job Metadata

| Field | Value |
|-------|-------|
| Evaluation job name | *(fill in)* |
| Job ARN | *(fill in)* |
| Date run | *(fill in)* |
| Region | us-east-1 |
| Judge model | amazon.nova-pro-v1:0 |
| Input JSONL file | output_eval_dataset.jsonl |
| S3 input path | *(fill in)* |
| S3 output path | *(fill in)* |
| IAM role used | bedrock-eval-role |
| Flow ID | *(fill in)* |
| Flow alias ID | *(fill in)* |

---

### Overall Scores

| Metric | Score |
|--------|-------|
| Correctness (overall) | *(fill in, e.g. 0.85)* |
| Number of test cases | 13 |
| Test cases passed | *(fill in)* |
| Test cases failed | *(fill in)* |

---

### Per-Category Scores

| Category | Cases | Passed | Failed | Notes |
|----------|-------|--------|--------|-------|
| BUG_REPORT | 3 | | | |
| PLATFORM_QUESTION | 5 | | | |
| OTHER | 2 | | | |
| Edge cases | 3 | | | |

---

### Per-Test-Case Observations

#### BUG_REPORT Tests

**bug-001 — Clear checkout bug**
- Routed correctly: Yes / No
- Agent asked follow-up: Yes / No / Not needed
- Ticket ID returned: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

**bug-002 — Vague bug description**
- Routed correctly: Yes / No
- Agent asked for description: Yes / No
- Ticket created after clarification: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

**bug-003 — Search filter bug**
- Routed correctly: Yes / No
- Agent collected details: Yes / No
- Ticket ID returned: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

---

#### PLATFORM_QUESTION Tests

**platform-001 — Order tracking**
- Routed correctly: Yes / No
- Answer matched FAQ Q9: Yes / No
- Hallucination observed: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

**platform-002 — Delivery time**
- Routed correctly: Yes / No
- Answer matched FAQ Q8: Yes / No
- Hallucination observed: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

**platform-003 — Return policy**
- Routed correctly: Yes / No
- Answer matched FAQ Q11: Yes / No
- Hallucination observed: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

**platform-004 — Payment declined**
- Routed correctly: Yes / No
- Answer matched FAQ Q20: Yes / No
- Hallucination observed: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

**platform-005 — Same-day delivery (not in FAQ)**
- Routed correctly: Yes / No
- Correctly said not in FAQ: Yes / No
- Hallucination observed: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

---

#### OTHER Tests

**other-001 — Restaurant recommendation**
- Routed correctly: Yes / No
- Polite redirect provided: Yes / No
- Invented contact info: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

**other-002 — Human agent request**
- Routed correctly: Yes / No
- Redirected to support form: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

---

#### Edge Case Tests

**edge-001 — "help" (very short)**
- Classification: *(fill in: BUG_REPORT / PLATFORM_QUESTION / OTHER)*
- Expected: OTHER
- Correct: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

**edge-002 — "It doesn't work" (ambiguous)**
- Classification: *(fill in)*
- Agent asked for clarification: Yes / No
- Ticket created prematurely: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

**edge-003 — Prompt injection attempt**
- Classification: *(fill in)*
- Expected: OTHER
- Injection succeeded: Yes / No
- Judge score: *(fill in)*
- Notes: *(fill in)*

---

### Failures and Root Causes

| Test ID | What failed | Root cause | Severity |
|---------|-------------|------------|----------|
| *(fill in)* | *(fill in)* | *(fill in)* | High / Medium / Low |

---

### Improvements Made After Run 1

| Issue | Change made | File/component affected |
|-------|-------------|------------------------|
| *(fill in)* | *(fill in)* | *(fill in)* |

---

## Evaluation Run 2 (if applicable)

### Job Metadata

| Field | Value |
|-------|-------|
| Evaluation job name | *(fill in)* |
| Date run | *(fill in)* |
| Change from Run 1 | *(describe what was changed)* |

### Overall Scores

| Metric | Run 1 | Run 2 | Delta |
|--------|-------|-------|-------|
| Correctness | *(fill in)* | *(fill in)* | *(fill in)* |

### Observations

*(Fill in: what improved, what didn't, what still needs work)*

---

## Final Assessment

### Correctness Score Achieved
*(Fill in final score)*

### Strengths Observed
- *(fill in)*
- *(fill in)*

### Remaining Weaknesses
- *(fill in)*
- *(fill in)*

### Recommendations for Further Improvement
- *(fill in)*
- *(fill in)*

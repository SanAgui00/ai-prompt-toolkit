# AWS CloudWatch Alarms Generator

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** devops
**Variables:** `{{SERVICE_NAME}}`, `{{RESOURCE_TYPE}}`, `{{RESOURCE_ID}}`, `{{ALERT_EMAIL}}`

---

Generate AWS CloudWatch alarms for `{{SERVICE_NAME}}`, a `{{RESOURCE_TYPE}}` resource (valid values: `ec2`, `lambda`, `ecs-service`) with ID/name `{{RESOURCE_ID}}`.

Requirements:
- **SNS Topic** — Create an SNS topic `{{SERVICE_NAME}}-alerts` with an email subscription to `{{ALERT_EMAIL}}`
- **Alarms — generate all that apply to `{{RESOURCE_TYPE}}`:**

  | Alarm | Metric | Threshold | Period | Eval Periods |
  |---|---|---|---|---|
  | High CPU | `CPUUtilization` | > 80% | 60s | 3 |
  | High Memory (EC2/ECS) | `MemoryUtilization` | > 85% | 60s | 3 | ⚠️ EC2: requires CloudWatch Agent installed on the instance |
  | Error Rate (Lambda) | `Errors` | > 5 | 60s | 1 |
  | Throttles (Lambda) | `Throttles` | > 0 | 60s | 2 |
  | High Latency (Lambda) | `Duration` | > 3000ms | 60s | 3 |
  | Unhealthy Hosts (ECS) | `UnhealthyHostCount` | >= 1 | 60s | 1 |

- Each alarm must:
  - Use `ALARM` action → publish to the SNS topic ARN
  - Use `OK` action → publish to the same SNS topic (recovery notification)
  - Set `TreatMissingData: notBreaching`
- Output format: Terraform (`aws_cloudwatch_metric_alarm` resources) or AWS CLI commands — whichever is specified by the user; default to Terraform

Also provide:
1. A `locals` block with the SNS topic ARN to avoid repetition
2. Instructions to confirm the SNS email subscription after `terraform apply`

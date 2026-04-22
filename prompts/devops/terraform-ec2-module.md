# Terraform EC2 Module

**Model:** Claude Sonnet 4.6 / GPT-4o
**Category:** devops
**Variables:** `{{MODULE_NAME}}`, `{{APP_NAME}}`, `{{AWS_REGION}}`

---

Generate a reusable Terraform module (`{{MODULE_NAME}}`) that provisions an EC2 instance for `{{APP_NAME}}` in `{{AWS_REGION}}`.

Module structure to generate:
```
modules/{{MODULE_NAME}}/
  main.tf
  variables.tf
  outputs.tf
```

Requirements:
- **`variables.tf`** — Define input variables with type, description, and default where appropriate:
  - `ami_id` (string, required)
  - `instance_type` (string, default `"t3.micro"`)
  - `subnet_id` (string, required)
  - `vpc_id` (string, required)
  - `key_name` (string, optional)
  - `allowed_cidr_blocks` (list of string, default `[]` — intentionally empty; since SSM is used, port 22 does not need to be open; only add CIDR blocks for `app_port` if the app is publicly accessible)
  - `app_port` (number, required)
  - `tags` (map of string, default `{}`)
- **`main.tf`** — Resources:
  - `aws_security_group` allowing ingress on `app_port` and port 22, egress all
  - `aws_iam_role` + `aws_iam_instance_profile` with `AmazonSSMManagedInstanceCore` policy (no SSH keys needed)
  - `aws_instance` referencing the above, with `user_data` placeholder variable, `ebs_optimized = true`, and `monitoring = true`
  - Merge `var.tags` with a `Name` tag using `merge()`
- **`outputs.tf`** — Output `instance_id`, `public_ip`, `private_ip`, `security_group_id`

Also provide:
1. A `versions.tf` snippet with required Terraform (`>= 1.5`) and AWS provider (`~> 5.0`) version constraints
2. Example `module` block showing how to call this module from a root configuration

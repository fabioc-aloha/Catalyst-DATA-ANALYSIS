---
applyTo: "**/*security*,**/*encryption*,**/*access*,**/*auth*"
description: "Data security protocols, encryption, access controls"
---

# Data Security Procedural Memory

## Access Control Implementation
- Implement role-based access control (RBAC) with principle of least privilege
- Use multi-factor authentication for sensitive data access
- Create time-limited access tokens with automatic expiration
- Establish regular access reviews and certification processes
- Implement session management and timeout policies

## Data Encryption Standards
- Use AES-256 encryption for data at rest in all storage systems
- Implement TLS 1.3 for data in transit across all connections
- Use envelope encryption for database-level security
- Establish key management and rotation procedures
- Implement field-level encryption for PII and sensitive data

## Network Security
- Implement network segmentation and VPC isolation
- Use firewall rules to restrict data access to authorized systems
- Establish VPN requirements for remote data access
- Monitor network traffic for suspicious data access patterns
- Implement intrusion detection and prevention systems

## Data Masking and Anonymization
- Use dynamic data masking for non-production environments
- Implement k-anonymity and differential privacy techniques
- Create synthetic data generation for testing and development
- Establish data pseudonymization procedures for analytics
- Monitor re-identification risks in anonymized datasets

## Security Monitoring and Incident Response
- Implement real-time security event monitoring and alerting
- Create detailed audit logs for all data access and modifications
- Establish incident response procedures for data security breaches
- Conduct regular security assessments and penetration testing
- Maintain security compliance documentation and reporting

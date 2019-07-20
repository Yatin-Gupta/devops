# AWS Lambdas
This repository consist of lambda scripts that I had made for 2 projects **Cloudportal** and **PaaS**.

Scripts used in the project are as:

| Script Name                       | Description                                                           | Plateform   | Project     |
| --------------------------------- | --------------------------------------------------------------------- | ----------- | ----------- |
| Extract-snapidfromImage           | Get snapshot id of custom AMIs.                                       | Javascript  | CloudPortal |
| EBS-Snapshot                      | Create snapshot by volume id.                                         | Javascript  | CloudPortal |
| Createtags                        | Create Tag by resource id.                                            | Javascript  | CloudPortal |
| AMIbasedinstanceid                | Incomplete functionality.                                             | Javascript  | CloudPortal |
| autoScalingdesc                   | Return ids of instances running in autoscaling group.                 | Javascript  | CloudPortal |
| RDSSnap                           | Create RDS snapshot by instance id.                                   | Javascript  | CloudPortal |
| delete_ami                        | Delete custom AMI after applying description filter.                  | Javascript  | CloudPortal |
| delete_rds_snapshot               | Delete RDS snapshot by snapshot id.                                   | Javascript  | CloudPortal |
| delete_snapshots                  | Delete the snapshot by snapshot id.                                   | Javascript  | CloudPortal |
| describe_ami                      | Return AMI information after applying description filter.             | Javascript  | CloudPortal |
| describe_rds_snapshots            | Return information of rds snapshot by db instance id.                 | Javascript  | CloudPortal |
| describe_snapshots                | Return information of ebs snapshot by volume id.                      | Javascript  | CloudPortal |
| describe_volume                   | Get ids of volumes attached with ec2 instance.                        | Javascript  | CloudPortal |
| lambda-bak                        | Get instance data by instance id.                                     | Javascript  | CloudPortal |
| Pimcore-ContainerHosts-runCommand | Script to run command on remote instance.                             | Python      | PaaS        |
| Pimcore-CreateCF                  | Create Cloudformation stack for creating Pimcore environment on AWS.  | Python      | PaaS        |
| Pimcore-DeleteCF                  | Delete Cloudformation stack by stack name.                            | Python      | PaaS        |
| Pimcore-DescribeCF                | Return the Cloudformation stack output.                               | Python      | PaaS        |
| Pimcore-runCommand-Script         | Script to run command on remote instance.                             | Python      | PaaS        |
| PimcoreKeyPush                    | Script to push SSH keys from s3 to remote instance.                   | Python      | PaaS        |


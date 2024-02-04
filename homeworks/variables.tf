variable "credentials" {
  description = "My Credentials"
  default     = "../keys/google-credentials.json"
}


variable "project" {
  description = "Project"
  default     = "playground-s-11-bf1171a7"
}

variable "region" {
  description = "Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

variable "bq_dataset_name" {
  description = "My BigQuery Dataset Name"
  default     = "sch_wolf_demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage Bucket Name"
  default     = "sch-wolf-terraform-demo-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
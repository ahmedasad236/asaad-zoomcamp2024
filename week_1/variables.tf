variable "credentials_file" {
  description = "The path to the credentials file"
  default = "./keys/my-creds.json"
  
}

variable "project" {
  description = "The project ID to deploy to"
  default = "dtc-homework-1-412309"
}

variable "region" {
  description = "The region to deploy to"
  default = "us-central1"
}

variable "location" {
  description = "The location of the resources"
  default = "US"
  
}

variable "bq_dataset_name" {
  description = "My BigQuery dataset name"
  default = "demo_dataset"
}

variable "gcs_bucket_name" {
  description = "My Storage bucket name"
  default = "dtc-homework-1-412309-terra-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket storage class"
  default = "STANDARD"
}
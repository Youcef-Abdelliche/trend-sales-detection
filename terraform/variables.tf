variable "gcp-creds" {
default= "focused-sprite-401907-14e430ea106b.json"
}


variable "project_id" {
    default = "focused-sprite-401907"
}

variable "region" {
  default = "europe-west9"
}

variable "zone" {
  default = "europe-west9-c"
}

locals {
  storage_bucket = "youcef_retail_project"
}

variable "storage_class" {
  default = "STANDARD"
}

variable "BQ_DATASET" {
  type = string
  default = "sales_bq_dataset"
}
terraform {
  backend "s3" {
    encrypt = true
    bucket = "s3-lambdaapps-261358786165"
    region = "us-east-2"
    key = "terraform.tfstate"
    #profile = "felipe"
  }
}
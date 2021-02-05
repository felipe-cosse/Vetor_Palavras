resource "aws_dynamodb_table" "ddbtable" {
  name             = "vetor_palavras_tb"
  hash_key         = "eventDateTime"
  billing_mode   = "PROVISIONED"
  read_capacity  = 5
  write_capacity = 5
  attribute {
    name = "eventDateTime"
    type = "S"
  }
}
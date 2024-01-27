resource "aws_s3_bucket" "aws_bucket" {
  bucket = var.bucket_name
  tags = {
    Name        = format("%s-devops-bucket", var.app_name)
    Environment = "dev"
  }
}

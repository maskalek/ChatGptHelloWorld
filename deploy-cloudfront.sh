#!/usr/bin/env bash
# Deploy the react-hello-world example to Amazon S3 and create a CloudFront distribution.
# Usage: ./deploy-cloudfront.sh <bucket-name> [region]
# Requires the AWS CLI and appropriate credentials.

set -euo pipefail

BUCKET=${1:-}
REGION=${2:-us-east-1}

if [[ -z "$BUCKET" ]]; then
  echo "Usage: $0 <bucket-name> [region]"
  exit 1
fi

# Create the bucket if it does not exist
aws s3 mb s3://$BUCKET --region $REGION || true

# Upload website files
aws s3 sync react-hello-world/ s3://$BUCKET --delete

# Enable static website hosting
aws s3 website s3://$BUCKET --index-document index.html --error-document index.html

# Create CloudFront distribution
CF_ID=$(aws cloudfront create-distribution --origin-domain-name "$BUCKET.s3.amazonaws.com" \
  --default-root-object index.html --query 'Distribution.Id' --output text)

echo "Created CloudFront distribution: $CF_ID"

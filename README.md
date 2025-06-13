# ChatGptHelloWorld

This repository contains small examples. The `react-hello-world` directory shows a simple React component styled with a modern glass-like design.

Open `react-hello-world/index.html` in a browser to see the animation.

## Deploying to AWS CloudFront

You can host the React example using Amazon S3 and CloudFront. The basic steps
are:

1. Create a new S3 bucket and enable static website hosting.
2. Upload the files from `react-hello-world/` to the bucket:

   ```bash
   aws s3 sync react-hello-world/ s3://YOUR_BUCKET --delete
   ```

3. Create a CloudFront distribution with the bucket as its origin:

   ```bash
   aws cloudfront create-distribution --origin-domain-name YOUR_BUCKET.s3.amazonaws.com
   ```

4. Once the distribution status becomes **Deployed**, open the distribution's
   domain name in your browser.

The `deploy-cloudfront.sh` script automates these steps with the AWS CLI.

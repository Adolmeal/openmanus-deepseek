try:
    import boto3
except ImportError:
    boto3 = None

class BedrockClient:
    def __init__(self):
        if boto3 is not None:
            self.client = boto3.client('bedrock')
        else:
            self.client = None
            print("Warning: boto3 is not installed. BedrockClient functionality is limited.")

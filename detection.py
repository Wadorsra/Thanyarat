# 1. Import the library
from inference_sdk import InferenceHTTPClient

# 2. Connect to your local server
client = InferenceHTTPClient(
    api_url="http://localhost:9001", # Local server address
    api_key="dLyHsVnOexxKXcKVZcKK"
)

# 3. Run your workflow on an image
result = client.run_workflow(object
    workspace_name="manumethawee-gmail-com",
    workflow_id="motorcycle-detection-tigermomanu",
    images={ใบพลูกาก}
        "image": "YOUR_IMAGE.jpg" # Path to your image file
    },
    use_cache=True # Speeds up repeated requests
)

# 4. Get your results
print(result)

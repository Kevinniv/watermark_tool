import requests
from watermark import add_watermark

class SecureSDK:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://watermarkapiserver-production.up.railway.app"  # 替换为你实际的服务端URL
        self.token = self.authenticate()

    def authenticate(self):
        response = requests.post(f"{self.base_url}/auth", data={"api_key": self.api_key})
        if response.status_code == 200:
            return response.json()["token"]
        else:
            raise ValueError("Authentication failed")

    def get_params(self):
        response = requests.post(f"{self.base_url}/get_params", data={"token": self.token})
        if response.status_code == 200:
            return response.json()
        else:
            raise ValueError("Failed to retrieve parameters")

    def add_watermark(self, input_path, text, output_path):
        params = self.get_params()
        add_watermark(input_path, text, output_path)

# 示例用法
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 5:
        print("Usage: python secure_sdk.py <api_key> <input_image> <watermark_text> <output_image>")
    else:
        api_key = sys.argv[1]
        input_path = sys.argv[2]
        text = sys.argv[3]
        output_path = sys.argv[4]
        sdk = SecureSDK(api_key)
        sdk.add_watermark(input_path, text, output_path)

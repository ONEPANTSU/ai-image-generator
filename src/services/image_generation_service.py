import replicate

from request import Request


class ImageGenerationService:
    DEFAULT_MODEL = "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b"

    def __init__(self, api_token, model: str = DEFAULT_MODEL):
        self.client = replicate.Client(api_token=api_token)
        self.model = model

    def generate(self, request: Request):
        result = self.client.run(self.model, input=request.get_dict())
        return result[0]

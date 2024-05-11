# ai-image-generator

## Run example
```bash
echo "REPLICATE_API_TOKEN=your-replicate-api-token" > .env
docker build . --tag="ai-image-generator"
docker run -p 8501:8501 ai-image-generator
```
The app will be started on `8501` port.
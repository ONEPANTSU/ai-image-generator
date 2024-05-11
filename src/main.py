from config import Config
from services.image_generation_service import ImageGenerationService
from services.page_render_service import PageRenderService


def main():
    config = Config(".env")
    image_generator = ImageGenerationService(config.REPLICATE_API_TOKEN)
    page_render = PageRenderService(image_generator)
    page_render.render()


if __name__ == '__main__':
    main()

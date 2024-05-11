"""
File to deploy via Streamlit
"""

import streamlit as st
from services.image_generation_service import ImageGenerationService
from services.page_render_service import PageRenderService


def main():
    image_generator = ImageGenerationService(st.secrets["REPLICATE_API_TOKEN"])
    page_render = PageRenderService(image_generator)
    page_render.render()


if __name__ == '__main__':
    main()

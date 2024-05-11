import streamlit as st
from services.image_generation_service import ImageGenerationService
from request import Request


class PageRenderService:
    def __init__(self, image_generator: ImageGenerationService):
        self.image_generator = image_generator

    def render(self):
        st.title('AI Image Generator')
        request = self.__create_sidebar()
        if request.submitted:
            with st.spinner('Generating...'):
                image = self.image_generator.generate(request)
                with st.container():
                    st.image(image, caption="Generated Image")


    @staticmethod
    def __create_sidebar():
        with st.sidebar:
            with st.form('sidebar'):
                width = st.number_input("Image Width", min_value=256, max_value=4096, step=16, value=1024)
                height = st.number_input("Image Height", min_value=256, max_value=4096, step=16, value=1024)
                prompt = st.text_area("Prompt", )
                submitted = st.form_submit_button("Submit", type="primary")

        return Request(
            width=width,
            height=height,
            prompt=prompt,
            submitted=submitted
        )
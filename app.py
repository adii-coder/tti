# import streamlit as st
# from huggingface_hub import InferenceClient
# from PIL import Image
# import io

# # Set your Hugging Face API key
# API_KEY = ""

# # Initialize Hugging Face Inference Client
# client = InferenceClient(api_key=API_KEY)

# # Streamlit UI
# st.set_page_config(page_title="AI Image Generator", page_icon="🎨", layout="centered")
# st.title("🎨 AI Image Generator")
# st.write("Generate images using **Stable Diffusion 3.5** powered by Hugging Face!")

# # User input
# prompt = st.text_area("Enter your prompt:", "A futuristic cyberpunk city at night with neon lights")

# if st.button("Generate Image"):
#     with st.spinner("Generating image... Please wait ⏳"):
#         try:
#             # Generate the image
#             image = client.text_to_image(prompt, model="stabilityai/stable-diffusion-3.5-large")

#             # Display the image
#             st.image(image, caption="Generated Image", use_column_width=True)

#             # Convert image to bytes for download
#             img_bytes = io.BytesIO()
#             image.save(img_bytes, format="PNG")
#             img_bytes = img_bytes.getvalue()

#             # Download button
#             st.download_button(label="📥 Download Image", data=img_bytes, file_name="generated_image.png", mime="image/png")

#         except Exception as e:
#             st.error(f"❌ Error: {e}")

# # Footer
# st.markdown("---")
# st.write("⚡ Powered by [Stable Diffusion 3.5](https://huggingface.co/stabilityai/stable-diffusion-3.5-large) & Hugging Face Inference API.")



























# import streamlit as st
# from huggingface_hub import InferenceClient
# from PIL import Image, ImageEnhance, ImageOps
# import io
# import random
# import base64

# # Set your Hugging Face API key
# API_KEY = ""
# client = InferenceClient(api_key=API_KEY)

# # Streamlit UI Configuration
# st.set_page_config(page_title="AI Image Generator", page_icon="🎨", layout="wide")

# # ---- 🌟 Custom CSS for Styling 🌟 ----
# st.markdown(
#     """
#     <style>
#         body { background-color: #0E1117; color: #EAEAEA; }
#         .stButton button { background-color: #4CAF50; color: white; font-size: 16px; border-radius: 10px; }
#         .stDownloadButton button { background-color: #007BFF; color: white; border-radius: 10px; }
#         .stSidebar { background-color: #20232A; }
#         img { border-radius: 10px; }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # ---- 🌟 Sidebar Settings 🌟 ----
# st.sidebar.header("⚙️ Settings")

# # Model Selection
# model = st.sidebar.selectbox(
#     "Select Model",
#     ["stabilityai/stable-diffusion-3.5-large", "stabilityai/stable-diffusion-xl", "stabilityai/stable-diffusion-2-1"],
#     index=0
# )

# # Resolution & Image Variations
# resolution = st.sidebar.radio("🖼️ Select Resolution", ["512x512", "768x768", "1024x1024"], index=1)
# num_variations = st.sidebar.slider("🔄 Number of Variations", 1, 5, 1)

# # Style Presets
# style_presets = {
#     "None": "",
#     "Cyberpunk": "A futuristic cyberpunk city with neon lights",
#     "Anime": "Anime-style fantasy landscape",
#     "Oil Painting": "A beautiful oil painting of a sunset over the mountains",
#     "Sketch": "A pencil sketch of a medieval castle",
#     "Realistic": "A highly detailed and photorealistic portrait"
# }
# style = st.sidebar.selectbox("🎨 Apply Style Preset", list(style_presets.keys()), index=0)

# # AI Parameters
# guidance_scale = st.sidebar.slider("🎚️ Guidance Scale", 1.0, 15.0, 7.5)
# inference_steps = st.sidebar.slider("⚡ Inference Steps", 10, 100, 50)

# # ---- 🌟 Main UI 🌟 ----
# st.title("🎨 AI Image Generator")
# st.markdown("**Generate high-quality images using AI-powered Stable Diffusion 3.5!** 🚀")

# # User Input
# prompt = st.text_area("📝 Enter your prompt:", "A futuristic cyberpunk city at night with neon lights")
# negative_prompt = st.text_area("🚫 Negative Prompt (Optional):", "blurry, distorted, low quality")

# # ---- 🌟 Image Upload for Enhancement 🌟 ----
# st.subheader("📂 Upload an Image for Enhancement")
# uploaded_file = st.file_uploader("Enhance an existing image (Optional)", type=["png", "jpg", "jpeg"])
# enhance_option = st.radio("🔍 Enhancement Type", ["None", "Sharpen", "Contrast", "Grayscale"], index=0)

# if uploaded_file:
#     image = Image.open(uploaded_file)
#     if enhance_option == "Sharpen":
#         enhancer = ImageEnhance.Sharpness(image)
#         image = enhancer.enhance(2.0)
#     elif enhance_option == "Contrast":
#         enhancer = ImageEnhance.Contrast(image)
#         image = enhancer.enhance(1.5)
#     elif enhance_option == "Grayscale":
#         image = ImageOps.grayscale(image)
    
#     st.image(image, caption="🖼️ Enhanced Image", use_column_width=True)

# # ---- 🌟 Generate AI Image Button 🌟 ----
# if st.button("🚀 Generate Image"):
#     with st.spinner("Generating... ⏳"):
#         try:
#             final_prompt = f"{prompt}, {style_presets[style]}" if style_presets[style] else prompt

#             images = []
#             for _ in range(num_variations):
#                 generated_image = client.text_to_image(final_prompt, model=model)
#                 images.append(generated_image)

#             # Display images in a grid
#             cols = st.columns(num_variations)
#             for idx, img in enumerate(images):
#                 with cols[idx]:
#                     st.image(img, caption=f"Generated Image {idx+1}", use_column_width=True)

#                     # Convert image to bytes for download
#                     img_bytes = io.BytesIO()
#                     img.save(img_bytes, format="PNG")
#                     img_bytes = img_bytes.getvalue()

#                     st.download_button(label="📥 Download Image", data=img_bytes, file_name=f"generated_image_{idx+1}.png", mime="image/png")

#                     # Save to session history
#                     if "history" not in st.session_state:
#                         st.session_state.history = []
#                     st.session_state.history.append(img)

#         except Exception as e:
#             st.error(f"❌ Error: {e}")

# # ---- 🌟 Image History Panel 🌟 ----
# st.sidebar.subheader("📜 Image History")
# if "history" in st.session_state and st.session_state.history:
#     for idx, img in enumerate(st.session_state.history[::-1][:5]):  # Show last 5 images
#         st.sidebar.image(img, caption=f"Previous {idx + 1}")

# # ---- 🌟 Footer & Dark Mode Option 🌟 ----
# st.markdown("---")
# st.markdown("🔹 **Powered by Stable Diffusion & Hugging Face** | Created with ❤️ by AI Enthusiasts")


















# import streamlit as st
# import requests
# from io import BytesIO
# from PIL import Image

# # Hugging Face API Setup
# API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-3.5-large"
# HEADERS = {"Authorization": "Bearer "}  # Replace with your Hugging Face API key

# def generate_image(prompt):
#     payload = {"inputs": prompt}
#     response = requests.post(API_URL, headers=HEADERS, json=payload)
    
#     if response.status_code == 200:
#         image = Image.open(BytesIO(response.content))
#         return image
#     else:
#         st.error(f"Error {response.status_code}: {response.text}")
#         return None

# # Streamlit UI
# st.set_page_config(page_title="AI Image Generator", layout="wide")
# st.title("🎨 AI Image Generator using Stable Diffusion")
# st.markdown("Enter a description and generate high-quality AI images instantly!")

# prompt = st.text_area("Enter your prompt:", "A futuristic city with neon lights")
# if st.button("Generate Image"):  
#     with st.spinner("Generating image..."):
#         image = generate_image(prompt)
#         if image:
#             st.image(image, caption="Generated Image", use_column_width=True)

# # Custom Styling
# st.markdown("""
#     <style>
#         .stTextInput, .stButton { text-align: center; }
#         .stButton > button { background-color: #4CAF50; color: white; font-size: 18px; padding: 10px 24px; }
#     </style>
# """, unsafe_allow_html=True)





































# import streamlit as st
# from huggingface_hub import InferenceClient
# from PIL import Image, ImageEnhance, ImageOps
# import io
# import random
# import base64

# # Set your Hugging Face API key
# API_KEY = ""
# client = InferenceClient(api_key=API_KEY)

# # Streamlit UI Configuration
# st.set_page_config(page_title="Rachna", page_icon="🎨", layout="wide")

# # ---- 🌟 Custom CSS for Styling 🌟 ----
# st.markdown(
#     """
#     <style>
#         body { background-color: #0E1117; color: #EAEAEA; }
#         .stButton button { background-color: #4CAF50; color: white; font-size: 16px; border-radius: 10px; }
#         .stDownloadButton button { background-color: #007BFF; color: white; border-radius: 10px; }
#         .stSidebar { background-color: #20232A; transition: all 0.3s ease-in-out; }
#         img { border-radius: 10px; }
#         .small-image img { width: 150px !important; height: auto !important; }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # ---- 🌟 Sidebar Settings 🌟 ----
# st.sidebar.header("⚙️ Settings")

# # Model Selection
# model = st.sidebar.selectbox(
#     "Select Model",
#     ["stabilityai/stable-diffusion-3.5-large", "stabilityai/stable-diffusion-xl", "stabilityai/stable-diffusion-2-1"],
#     index=0
# )

# # Resolution & Image Variations
# resolution = st.sidebar.radio("🖼️ Select Resolution", ["512x512", "768x768", "1024x1024"], index=0)
# num_variations = st.sidebar.slider("🔄 Number of Variations", 1, 5, 1)

# # Style Presets
# style_presets = {
#     "None": "",
#     "Cyberpunk": "A futuristic cyberpunk city with neon lights",
#     "Anime": "Anime-style fantasy landscape",
#     "Oil Painting": "A beautiful oil painting of a sunset over the mountains",
#     "Sketch": "A pencil sketch of a medieval castle",
#     "Realistic": "A highly detailed and photorealistic portrait"
# }
# style = st.sidebar.selectbox("🎨 Apply Style Preset", list(style_presets.keys()), index=0)

# # ---- 🌟 Main UI 🌟 ----
# st.title("🌟 Rachna - AI Image Creator 🌟")
# st.markdown("**Create stunning AI-generated images with ease!** 🎨✨")

# # User Input
# prompt = st.text_area("📝 Enter your prompt:", "A futuristic cyberpunk city at night with neon lights")
# negative_prompt = st.text_area("🚫 Negative Prompt (Optional):", "blurry, distorted, low quality")

# # ---- 🌟 Generate AI Image Button 🌟 ----
# if st.button("🚀 Generate Image"):
#     with st.spinner("Generating... ⏳"):
#         try:
#             final_prompt = f"{prompt}, {style_presets[style]}" if style_presets[style] else prompt

#             images = []
#             for _ in range(num_variations):
#                 variation_prompt = f"{final_prompt}, variation {_+1}"  # Unique variations
#                 generated_image = client.text_to_image(variation_prompt, model=model)
#                 generated_image = generated_image.resize((512, 512))  # Resize for UI aesthetics
#                 images.append(generated_image)

#             # Display images in a grid
#             cols = st.columns(num_variations)
#             for idx, img in enumerate(images):
#                 with cols[idx]:
#                     st.image(img, caption=f"Generated Image {idx+1}", use_container_width=True)

#                     # Convert image to bytes for download
#                     img_bytes = io.BytesIO()
#                     img.save(img_bytes, format="PNG")
#                     img_bytes = img_bytes.getvalue()

#                     st.download_button(label="📥 Download Image", data=img_bytes, file_name=f"generated_image_{idx+1}.png", mime="image/png")

#                     # Save to session history
#                     if "history" not in st.session_state:
#                         st.session_state.history = []
#                     st.session_state.history.append(img)

#         except Exception as e:
#             st.error(f"❌ Error: {e}")

# # ---- 🌟 Image Enhancement Section 🌟 ----
# st.header("✨ Image Enhancement")

# uploaded_file = st.file_uploader("📂 Upload an Image for Enhancement", type=["png", "jpg", "jpeg"])
# enhance_option = st.radio("🔍 Enhancement Type", ["None", "Sharpen", "Contrast", "Grayscale"], index=0)

# def enhance_image(image, enhance_option):
#     if enhance_option == "Sharpen":
#         enhancer = ImageEnhance.Sharpness(image)
#         return enhancer.enhance(2.0)
#     elif enhance_option == "Contrast":
#         enhancer = ImageEnhance.Contrast(image)
#         return enhancer.enhance(1.5)
#     elif enhance_option == "Grayscale":
#         return ImageOps.grayscale(image)
#     return image

# if uploaded_file:
#     st.subheader("📌 Uploaded Image Preview")
#     image = Image.open(uploaded_file).resize((300, 300))  # Resize for UI aesthetics
#     st.image(image, caption="🖼️ Uploaded Image", use_container_width=True)

#     if st.button("✨ Enhance Image"):
#         enhanced_image = enhance_image(image, enhance_option)
#         st.image(enhanced_image, caption="🖼️ Enhanced Image", use_container_width=True)

#         # Convert enhanced image to bytes for download
#         img_bytes = io.BytesIO()
#         enhanced_image.save(img_bytes, format="PNG")
#         img_bytes = img_bytes.getvalue()

#         st.download_button(label="📥 Download Enhanced Image", data=img_bytes, file_name="enhanced_image.png", mime="image/png")

# # ---- 🌟 Image History Panel 🌟 ----
# st.sidebar.subheader("📜 Image History")
# if "history" in st.session_state and st.session_state.history:
#     for idx, img in enumerate(st.session_state.history[::-1][:5]):  # Show last 5 images
#         st.sidebar.image(img, caption=f"Previous {idx + 1}", use_container_width=True)

# # ---- 🌟 Footer & Dark Mode Option 🌟 ----
# st.markdown("---")
# st.markdown("🔹 **Powered by Stable Diffusion** | Created with ❤️ by AI Enthusiasts ADITYA TIWARI")






















# import streamlit as st
# from huggingface_hub import InferenceClient
# from PIL import Image, ImageEnhance, ImageOps
# import io
# import random
# import base64

# # Set your Hugging Face API key from Streamlit Secrets
# HF_API_KEY = st.secrets["HF_API_KEY"]
# client = InferenceClient(api_key=HF_API_KEY)

# # Streamlit UI Configuration
# st.set_page_config(page_title="Rachna", page_icon="🎨", layout="wide")

# # ---- 🌟 Custom CSS for Styling 🌟 ----
# st.markdown(
#     """
#     <style>
#         body { background-color: #0E1117; color: #EAEAEA; }
#         .stButton button { background-color: #4CAF50; color: white; font-size: 16px; border-radius: 10px; }
#         .stDownloadButton button { background-color: #007BFF; color: white; border-radius: 10px; }
#         .stSidebar { background-color: #20232A; transition: all 0.3s ease-in-out; }
#         img { border-radius: 10px; max-width: 500px; height: auto; }
#         .small-image img { width: 150px !important; height: auto !important; }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # ---- 🌟 Sidebar Settings 🌟 ----
# st.sidebar.header("⚙️ Settings")

# # Model Selection
# model = st.sidebar.selectbox(
#     "Select Model",
#     ["stabilityai/stable-diffusion-3.5-large", "stabilityai/stable-diffusion-xl", "stabilityai/stable-diffusion-2-1"],
#     index=0
# )

# # Resolution & Image Variations
# resolution = st.sidebar.radio("🎨 Select Resolution", ["512x512", "768x768", "1024x1024"], index=2)  # Default to highest resolution
# num_variations = st.sidebar.slider("🔄 Number of Variations", 1, 5, 1)

# # Style Presets
# style_presets = {
#     "None": "",
#     "Cyberpunk": "A futuristic cyberpunk city with neon lights",
#     "Anime": "Anime-style fantasy landscape",
#     "Oil Painting": "A beautiful oil painting of a sunset over the mountains",
#     "Sketch": "A pencil sketch of a medieval castle",
#     "Realistic": "A highly detailed and photorealistic portrait"
# }
# style = st.sidebar.selectbox("🎨 Apply Style Preset", list(style_presets.keys()), index=0)

# # Image Enhancement Section Toggle
# enhance_toggle = st.sidebar.checkbox("Enable Image Enhancement")

# # ---- 🌟 Main UI 🌟 ----
# st.title("🌟 Rachna - AI Image Creator 🌟")
# st.markdown("**Create stunning AI-generated images with ease!** 🎨✨")

# # User Input
# prompt = st.text_area("📝 Enter your prompt:", "A futuristic cyberpunk city at night with neon lights")
# negative_prompt = st.text_area("🚫 Negative Prompt (Optional):", "blurry, distorted, low quality")

# # ---- 🌟 Generate AI Image Button 🌟 ----
# if st.button("🚀 Generate Image"):
#     with st.spinner("Generating... ⏳"):
#         try:
#             final_prompt = f"{prompt}, {style_presets[style]}" if style_presets[style] else prompt

#             images = []
#             for _ in range(num_variations):
#                 variation_prompt = f"{final_prompt}, variation {_+1}"  # Unique variations
#                 generated_image = client.text_to_image(variation_prompt, model=model)
#                 generated_image = generated_image.resize((512, 512))  # Smaller display size
#                 images.append(generated_image)

#             # Display images in a grid
#             cols = st.columns(num_variations)
#             for idx, img in enumerate(images):
#                 with cols[idx]:
#                     st.image(img, caption=f"Generated Image {idx+1}", use_container_width=True)

#                     # Convert image to bytes for download
#                     img_bytes = io.BytesIO()
#                     img.save(img_bytes, format="PNG")
#                     img_bytes = img_bytes.getvalue()

#                     st.download_button(label="💽 Download Image", data=img_bytes, file_name=f"generated_image_{idx+1}.png", mime="image/png")

#                     # Save to session history
#                     if "history" not in st.session_state:
#                         st.session_state.history = []
#                     st.session_state.history.append(img)
        
#         except Exception as e:
#             st.error(f"❌ Error: {e}")

# # ---- 🌟 Image Enhancement Section (Only Visible If Enabled) 🌟 ----
# if enhance_toggle:
#     st.sidebar.header("✨ Image Enhancement")
#     uploaded_file = st.sidebar.file_uploader("📂 Upload an Image for Enhancement", type=["png", "jpg", "jpeg"])
#     enhance_options = st.sidebar.multiselect("🔍 Enhancement Options", ["Sharpen", "Contrast", "Grayscale"], default=[])

#     def enhance_image(image, options):
#         if "Sharpen" in options:
#             image = ImageEnhance.Sharpness(image).enhance(2.0)
#         if "Contrast" in options:
#             image = ImageEnhance.Contrast(image).enhance(1.5)
#         if "Grayscale" in options:
#             image = ImageOps.grayscale(image)
#         return image

#     if uploaded_file:
#         image = Image.open(uploaded_file).resize((300, 300))  # Resize for UI aesthetics
#         st.sidebar.image(image, caption="🎨 Uploaded Image", use_container_width=True)

#         if st.sidebar.button("✨ Enhance Image"):
#             enhanced_image = enhance_image(image, enhance_options)
#             st.sidebar.image(enhanced_image, caption="🎨 Enhanced Image", use_container_width=True)

#             # Convert enhanced image to bytes for download
#             img_bytes = io.BytesIO()
#             enhanced_image.save(img_bytes, format="PNG")
#             img_bytes = img_bytes.getvalue()

#             st.sidebar.download_button(label="💽 Download Enhanced Image", data=img_bytes, file_name="enhanced_image.png", mime="image/png")

# # ---- 🌟 Footer & Dark Mode Option 🌟 ----
# st.markdown("---")
# st.markdown("🔹 **Powered by Stable Diffusion** | Created with ❤️ by AI Enthusiasts ADITYA TIWARI")



























# import streamlit as st
# from huggingface_hub import InferenceClient
# from PIL import Image, ImageEnhance, ImageOps
# import io
# import base64

# # Set your Hugging Face API key from Streamlit Secrets
# HF_API_KEY = st.secrets["HF_API_KEY"]
# client = InferenceClient(api_key=HF_API_KEY)

# # Streamlit UI Configuration
# st.set_page_config(page_title="Rachna", page_icon="🎨", layout="wide")

# # ---- 🌟 Custom CSS for Styling 🌟 ----
# st.markdown(
#     """
#     <style>
#         body { background-color: #0E1117; color: #EAEAEA; }
#         .stButton button { background-color: #4CAF50; color: white; font-size: 16px; border-radius: 10px; }
#         .stDownloadButton button { background-color: #007BFF; color: white; border-radius: 10px; }
#         .stSidebar { background-color: #20232A; transition: all 0.3s ease-in-out; }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # ---- 🌟 Sidebar Settings 🌟 ----
# st.sidebar.header("⚙️ Settings")

# # Model Selection
# model = st.sidebar.selectbox(
#     "Select Model",
#     ["stabilityai/stable-diffusion-3.5-large", "stabilityai/stable-diffusion-xl", "stabilityai/stable-diffusion-2-1"],
#     index=0
# )

# # Resolution & Image Variations
# resolution_map = {"512x512": (512, 512), "768x768": (768, 768), "1024x1024": (1024, 1024)}
# resolution = st.sidebar.radio("🎨 Select Resolution", list(resolution_map.keys()), index=2)
# num_variations = st.sidebar.slider("🔄 Number of Variations", 1, 5, 1)

# # Style Presets
# style_presets = {
#     "None": "",
#     "Cyberpunk": "A futuristic cyberpunk city with neon lights",
#     "Anime": "Anime-style fantasy landscape",
#     "Oil Painting": "A beautiful oil painting of a sunset over the mountains",
#     "Sketch": "A pencil sketch of a medieval castle",
#     "Realistic": "A highly detailed and photorealistic portrait"
# }
# style = st.sidebar.selectbox("🎨 Apply Style Preset", list(style_presets.keys()), index=0)

# # ---- 🌟 Main UI 🌟 ----
# st.title("🌟 Rachna - AI Image Creator 🌟")
# st.markdown("**Create stunning AI-generated images with ease!** 🎨✨")

# # Image Enhancement Section Toggle
# if "enhance_mode" not in st.session_state:
#     st.session_state.enhance_mode = False

# def toggle_enhance_mode():
#     st.session_state.enhance_mode = not st.session_state.enhance_mode

# st.sidebar.button("✨ Image Enhancement", on_click=toggle_enhance_mode)

# if st.session_state.enhance_mode:
#     st.markdown("## ✨ Image Enhancement")
#     uploaded_file = st.file_uploader("📂 Upload an Image for Enhancement", type=["png", "jpg", "jpeg"])
#     enhance_options = st.multiselect("🔍 Enhancement Options", ["Sharpen", "Contrast", "Grayscale", "Brightness", "Saturation"], default=[])
    
#     def enhance_image(image, options):
#         if "Sharpen" in options:
#             image = ImageEnhance.Sharpness(image).enhance(2.0)
#         if "Contrast" in options:
#             image = ImageEnhance.Contrast(image).enhance(1.5)
#         if "Brightness" in options:
#             image = ImageEnhance.Brightness(image).enhance(1.3)
#         if "Saturation" in options:
#             image = ImageEnhance.Color(image).enhance(1.5)
#         if "Grayscale" in options:
#             image = ImageOps.grayscale(image)
#         return image
    
#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="🎨 Uploaded Image", use_container_width=True)

#         if st.button("✨ Enhance Image"):
#             enhanced_image = enhance_image(image, enhance_options)
#             st.image(enhanced_image, caption="🎨 Enhanced Image", use_container_width=True)
#             img_bytes = io.BytesIO()
#             enhanced_image.save(img_bytes, format="PNG")
#             img_bytes = img_bytes.getvalue()
#             st.download_button(label="💽 Download Enhanced Image", data=img_bytes, file_name="enhanced_image.png", mime="image/png")
# else:
#     # ---- 🌟 Generate AI Image Section 🌟 ----
#     prompt = st.text_input("📝 Enter Your Prompt", "A beautiful landscape with mountains and a river")
    
#     if st.button("🚀 Generate Image"):
#         with st.spinner("Generating... ⏳"):
#             try:
#                 final_prompt = f"{prompt}, {style_presets[style]}" if style_presets[style] else prompt
                
#                 images = []
#                 for _ in range(num_variations):
#                     variation_prompt = f"{final_prompt}, variation {_+1}"
#                     generated_image = client.text_to_image(variation_prompt, model=model)
#                     generated_image = generated_image.resize(resolution_map[resolution])
#                     images.append(generated_image)
                
#                 if "history" not in st.session_state:
#                     st.session_state.history = []
                
#                 for idx, img in enumerate(images):
#                     st.image(img, caption=f"Generated Image {idx+1}", use_container_width=True)
#                     img_bytes = io.BytesIO()
#                     img.save(img_bytes, format="PNG")
#                     img_bytes = img_bytes.getvalue()
#                     st.download_button(label="💽 Download Image", data=img_bytes, file_name=f"generated_image_{idx+1}.png", mime="image/png")
#                     st.session_state.history.append(img_bytes)
#             except Exception as e:
#                 st.error(f"❌ Error: {e}")

# # ---- 🌟 History Section 🌟 ----
# st.sidebar.subheader("📜 Image History")
# if "history" in st.session_state and st.session_state.history:
#     for idx, img_bytes in enumerate(st.session_state.history[-5:]):
#         img = Image.open(io.BytesIO(img_bytes))
#         st.sidebar.image(img, caption=f"History {idx+1}", use_container_width=True)
#         st.sidebar.download_button(label="💽 Download", data=img_bytes, file_name=f"history_image_{idx+1}.png", mime="image/png")

# if st.sidebar.button("🗑️ Clear History"):
#     st.session_state.history = []

# # ---- 🌟 Footer & Dark Mode Option 🌟 ----
# st.markdown("---")
# st.markdown("🔹 **Powered by Stable Diffusion** | Created with ❤️ by AI Enthusiasts ADITYA TIWARI")






















































# B  E  S  T

# import streamlit as st
# from huggingface_hub import InferenceClient
# from PIL import Image, ImageEnhance, ImageOps
# import io
# import base64

# # Set your Hugging Face API key from Streamlit Secrets
# HF_API_KEY = st.secrets["HF_API_KEY"]
# client = InferenceClient(api_key=HF_API_KEY)

# # Streamlit UI Configuration
# st.set_page_config(page_title="Rachna",page_icon="https://raw.githubusercontent.com/adii-coder/tti/refs/heads/main/favicon.ico",layout="wide")

# # ---- 🌟 Custom CSS for Styling 🌟 ----
# st.markdown(
#     """
#     <style>
#         body { background-color: #0E1117; color: #EAEAEA; }
#         .stButton button { background-color: #4CAF50; color: white; font-size: 16px; border-radius: 10px; }
#         .stDownloadButton button { background-color: #007BFF; color: white; border-radius: 10px; }
#         .stSidebar { background-color: #20232A; transition: all 0.3s ease-in-out; }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # ---- 🌟 Sidebar Settings 🌟 ----
# st.sidebar.header("⚙️ Settings")

# # Model Selection
# model = st.sidebar.selectbox(
#     "Select Model",
#     ["stabilityai/stable-diffusion-3.5-large", "stabilityai/stable-diffusion-xl", "stabilityai/stable-diffusion-2-1"],
#     index=0
# )

# # Resolution & Image Variations
# resolution_map = {"512x512": (512, 512), "768x768": (768, 768), "1024x1024": (1024, 1024)}
# resolution = st.sidebar.radio("🎨 Select Resolution", list(resolution_map.keys()), index=2)
# num_variations = st.sidebar.slider("🔄 Number of Variations", 1, 5, 1)

# # Style Presets
# style_presets = {
#     "None": "",
#     "Cyberpunk": "A futuristic cyberpunk city with neon lights",
#     "Anime": "Anime-style fantasy landscape",
#     "Oil Painting": "A beautiful oil painting of a sunset over the mountains",
#     "Sketch": "A pencil sketch of a medieval castle",
#     "Realistic": "A highly detailed and photorealistic portrait"
# }
# style = st.sidebar.selectbox("🎨 Apply Style Preset", list(style_presets.keys()), index=0)

# # ---- 🌟 Main UI 🌟 ----
# st.title("🌟 Rachna - AI Image Creator 🌟")
# st.markdown("**Create stunning AI-generated images with ease!** 🎨✨")

# # Image Enhancement Section Toggle
# if "enhance_mode" not in st.session_state:
#     st.session_state.enhance_mode = False

# def toggle_enhance_mode():
#     st.session_state.enhance_mode = not st.session_state.enhance_mode

# st.sidebar.button("✨ Image Enhancement", on_click=toggle_enhance_mode)

# if st.session_state.enhance_mode:
#     st.markdown("## ✨ Image Enhancement")
#     uploaded_file = st.file_uploader("📂 Upload an Image for Enhancement", type=["png", "jpg", "jpeg"])
#     enhance_options = st.multiselect("🔍 Enhancement Options", ["Sharpen", "Contrast", "Grayscale", "Brightness", "Saturation", "HDR Effect"], default=[])
    
#     def enhance_image(image, options):
#         if "Sharpen" in options:
#             image = ImageEnhance.Sharpness(image).enhance(3.0)
#         if "Contrast" in options:
#             image = ImageEnhance.Contrast(image).enhance(2.0)
#         if "Brightness" in options:
#             image = ImageEnhance.Brightness(image).enhance(1.5)
#         if "Saturation" in options:
#             image = ImageEnhance.Color(image).enhance(2.0)
#         if "Grayscale" in options:
#             image = ImageOps.grayscale(image)
#         if "HDR Effect" in options:
#             image = ImageEnhance.Contrast(image).enhance(2.5)
#             image = ImageEnhance.Sharpness(image).enhance(3.0)
#         return image
    
#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="🎨 Uploaded Image", use_container_width=True)

#         if st.button("✨ Enhance Image"):
#             enhanced_image = enhance_image(image, enhance_options)
#             st.image(enhanced_image, caption="🎨 Enhanced Image", use_container_width=True)
#             img_bytes = io.BytesIO()
#             enhanced_image.save(img_bytes, format="PNG")
#             img_bytes = img_bytes.getvalue()
#             st.download_button(label="💽 Download Enhanced Image", data=img_bytes, file_name="enhanced_image.png", mime="image/png")
# else:
#     # ---- 🌟 Generate AI Image Section 🌟 ----
#     prompt = st.text_input("📝 Enter Your Prompt", "A beautiful landscape with mountains and a river")
    
#     if st.button("🚀 Generate Image"):
#         with st.spinner("Generating... ⏳"):
#             try:
#                 final_prompt = f"{prompt}, {style_presets[style]}" if style_presets[style] else prompt
                
#                 images = []
#                 for _ in range(num_variations):
#                     generated_image = client.text_to_image(final_prompt, model=model)
#                     generated_image = generated_image.resize(resolution_map[resolution])
#                     images.append(generated_image)
                
#                 if "history" not in st.session_state:
#                     st.session_state.history = []
                
#                 for idx, img in enumerate(images):
#                     st.image(img, caption=f"Generated Image {idx+1}", use_container_width=True)
#                     img_bytes = io.BytesIO()
#                     img.save(img_bytes, format="PNG")
#                     img_bytes = img_bytes.getvalue()
#                     st.download_button(label="💽 Download Image", data=img_bytes, file_name=f"generated_image_{idx+1}.png", mime="image/png")
#                     st.session_state.history.append(img_bytes)
#             except Exception as e:
#                 st.error(f"❌ Error: {e}")

# # ---- 🌟 History Section 🌟 ----
# st.sidebar.subheader("📜 Image History")
# if "history" in st.session_state and st.session_state.history:
#     for idx, img_bytes in enumerate(st.session_state.history[-5:]):
#         img = Image.open(io.BytesIO(img_bytes))
#         st.sidebar.image(img, caption=f"History {idx+1}", use_container_width=True)
#         st.sidebar.download_button(label="💽 Download", data=img_bytes, file_name=f"history_image_{idx+1}.png", mime="image/png")

# if st.sidebar.button("🗑️ Clear History"):
#     st.session_state.history = []

# # ---- 🌟 Footer & Dark Mode Option 🌟 ----
# st.markdown("---")
# st.markdown("🔹 **Powered by Stable Diffusion** | Created with ❤️ by AI Enthusiasts ADITYA TIWARI")































# import streamlit as st
# from huggingface_hub import InferenceClient
# from PIL import Image, ImageEnhance, ImageOps
# import io
# import random
# import base64

# # Set your Hugging Face API key from Streamlit Secrets
# HF_API_KEY = st.secrets["HF_API_KEY"]
# client = InferenceClient(api_key=HF_API_KEY)

# # Streamlit UI Configuration
# st.set_page_config(page_title="Rachna - AI Image Creator", page_icon="🎨", layout="wide")

# # ---- 🌟 Custom CSS & Dark Mode 🌟 ----
# if "dark_mode" not in st.session_state:
#     st.session_state.dark_mode = True  # Default dark mode

# def toggle_dark_mode():
#     st.session_state.dark_mode = not st.session_state.dark_mode

# st.sidebar.button("🌙 Toggle Dark Mode" if st.session_state.dark_mode else "☀️ Light Mode", on_click=toggle_dark_mode)

# st.markdown(
#     f"""
#     <style>
#         body {{ background-color: {"#0E1117" if st.session_state.dark_mode else "#FFFFFF"}; color: {"#EAEAEA" if st.session_state.dark_mode else "#000000"}; }}
#         .stButton button {{ background-color: #4CAF50; color: white; font-size: 16px; border-radius: 10px; }}
#         .stDownloadButton button {{ background-color: #007BFF; color: white; border-radius: 10px; }}
#         .stSidebar {{ background-color: {"#20232A" if st.session_state.dark_mode else "#F0F0F0"}; transition: all 0.3s ease-in-out; }}
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # ---- 🌟 Sidebar Settings 🌟 ----
# st.sidebar.header("⚙️ Settings")

# # Model Selection
# model = st.sidebar.selectbox(
#     "Select Model",
#     ["stabilityai/stable-diffusion-3.5-large", "stabilityai/stable-diffusion-xl", "stabilityai/stable-diffusion-2-1"],
#     index=0
# )

# # Resolution & Image Variations
# resolution_map = {
#     "1280x720 (720p)": (1280, 720),
#     "1920x1080 (1080p)": (1920, 1080),
#     "2560x1440 (2K)": (2560, 1440),
#     "3840x2160 (4K)": (3840, 2160),
#     "7680x4320 (8K)": (7680, 4320),
#     "12288x6480 (12K)": (12288, 6480)
# }
# resolution = st.sidebar.radio("🎨 Select Resolution", list(resolution_map.keys()), index=2)
# num_variations = st.sidebar.slider("🔄 Number of Variations", 1, 5, 1)

# # Style Presets
# style_presets = {
#     "None": "",
#     "Cyberpunk": "A futuristic cyberpunk city with neon lights",
#     "Anime": "Anime-style fantasy landscape",
#     "Oil Painting": "A beautiful oil painting of a sunset over the mountains",
#     "Sketch": "A pencil sketch of a medieval castle",
#     "Realistic": "A highly detailed and photorealistic portrait"
# }
# style = st.sidebar.selectbox("🎨 Apply Style Preset", list(style_presets.keys()), index=0)

# # Negative Prompt (New Feature)
# negative_prompt = st.sidebar.text_input("🚫 Negative Prompt", "blurry, distorted, low quality")

# # ---- 🌟 Main UI 🌟 ----
# st.title("🌟 Rachna - AI Image Creator 🌟")
# st.markdown("**Create stunning AI-generated images with ease!** 🎨✨")

# # Image Enhancement Section Toggle
# if "enhance_mode" not in st.session_state:
#     st.session_state.enhance_mode = False

# def toggle_enhance_mode():
#     st.session_state.enhance_mode = not st.session_state.enhance_mode

# st.sidebar.button("✨ Image Enhancement", on_click=toggle_enhance_mode)

# if st.session_state.enhance_mode:
#     st.markdown("## ✨ Image Enhancement")
#     uploaded_file = st.file_uploader("📂 Upload an Image for Enhancement", type=["png", "jpg", "jpeg"])
#     enhance_options = st.multiselect("🔍 Enhancement Options", ["Sharpen", "Contrast", "Grayscale", "Brightness", "Saturation", "HDR Effect"], default=[])

#     def enhance_image(image, options):
#         if "Sharpen" in options:
#             image = ImageEnhance.Sharpness(image).enhance(4.0)
#         if "Contrast" in options:
#             image = ImageEnhance.Contrast(image).enhance(2.5)
#         if "Brightness" in options:
#             image = ImageEnhance.Brightness(image).enhance(1.8)
#         if "Saturation" in options:
#             image = ImageEnhance.Color(image).enhance(2.5)
#         if "Grayscale" in options:
#             image = ImageOps.grayscale(image)
#         if "HDR Effect" in options:
#             image = ImageEnhance.Contrast(image).enhance(3.0)
#             image = ImageEnhance.Sharpness(image).enhance(4.0)
#         return image

#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="🎨 Uploaded Image", use_container_width=True)

#         if st.button("✨ Enhance Image"):
#             enhanced_image = enhance_image(image, enhance_options)
#             st.image(enhanced_image, caption="🎨 Enhanced Image", use_container_width=True)
#             img_bytes = io.BytesIO()
#             enhanced_image.save(img_bytes, format="PNG")
#             st.download_button(label="💽 Download Enhanced Image", data=img_bytes, file_name="enhanced_image.png", mime="image/png")
# else:
#     # ---- 🌟 Generate AI Image Section 🌟 ----
#     prompt = st.text_input("📝 Enter Your Prompt", "A beautiful landscape with mountains and a river")

#     if st.button("🚀 Generate Image"):
#         with st.spinner("Generating... ⏳"):
#             try:
#                 final_prompt = f"{prompt}, {style_presets[style]}" if style_presets[style] else prompt

#                 if "history" not in st.session_state:
#                     st.session_state.history = []

#                 images = []
#                 cols = st.columns(num_variations)
#                 for i in range(num_variations):
#                     seed = random.randint(1, 1000000)  # Ensure unique variations
#                     variation_prompt = f"{final_prompt}, variation {i+1}, different angle, lighting, and style"
#                     generated_image = client.text_to_image(variation_prompt, model=model, seed=seed, negative_prompt=negative_prompt)
#                     generated_image = generated_image.resize(resolution_map[resolution])
#                     images.append(generated_image)

#                     with cols[i]:
#                         st.image(generated_image, caption=f"Generated Image {i+1}", use_container_width=True)
#                         img_bytes = io.BytesIO()
#                         generated_image.save(img_bytes, format="PNG")
#                         img_bytes = img_bytes.getvalue()
#                         st.download_button(label=f"💽 Download {i+1}", data=img_bytes, file_name=f"generated_image_{i+1}.png", mime="image/png")
#                         st.session_state.history.append(img_bytes)
#             except Exception as e:
#                 st.error(f"❌ Error: {e}")

# # ---- 🌟 History Section 🌟 ----
# st.sidebar.subheader("📜 Image History")
# if "history" in st.session_state and st.session_state.history:
#     for idx, img_bytes in enumerate(st.session_state.history[-5:]):
#         img = Image.open(io.BytesIO(img_bytes)).resize((100, 100))
#         st.sidebar.image(img, caption=f"History {idx+1}", use_container_width=True)
#         st.sidebar.download_button(label="💽 Download", data=img_bytes, file_name=f"history_image_{idx+1}.png", mime="image/png")

# if st.sidebar.button("🗑️ Clear History"):
#     st.session_state.history = []

# st.markdown("---")
# st.markdown("🔹 **Powered by Stable Diffusion** | Created with ❤️ by AI Enthusiasts ADITYA TIWARI")






#propr working

# import streamlit as st
# from huggingface_hub import InferenceClient
# from PIL import Image, ImageEnhance, ImageOps
# import io
# import random

# # Set your Hugging Face API key from Streamlit Secrets
# HF_API_KEY = st.secrets["HF_API_KEY"]
# client = InferenceClient(api_key=HF_API_KEY)

# # Streamlit UI Configuration
# st.set_page_config(page_title="Rachna - AI Image Creator", page_icon="🎨", layout="wide")

# # ---- 🌟 Sidebar - Settings & Image Enhancement Toggle 🌟 ----
# st.sidebar.header("⚙️ Settings")

# # Toggle for Image Enhancement Mode
# if "enhancement_mode" not in st.session_state:
#     st.session_state.enhancement_mode = False

# def toggle_enhancement_mode():
#     st.session_state.enhancement_mode = not st.session_state.enhancement_mode

# st.sidebar.button("🖼️ Image Enhancement", on_click=toggle_enhancement_mode)

# # ---- 🌟 Sidebar - Model Selection (Only when Enhancement Mode is Off) 🌟 ----
# if not st.session_state.enhancement_mode:
#     model = st.sidebar.selectbox(
#         "Select Model",
#         [
#             "stabilityai/stable-diffusion-3.5-large",
#             "stabilityai/stable-diffusion-xl",
#             "stabilityai/stable-diffusion-2-1"
#         ],
#         index=0
#     )

#     # Resolution & Image Variations
#     resolution_map = {
#         "1280x720 (720p)": (1280, 720),
#         "1920x1080 (1080p)": (1920, 1080),
#         "2560x1440 (2K)": (2560, 1440),
#         "3840x2160 (4K)": (3840, 2160),
#         "7680x4320 (8K)": (7680, 4320),
#         "12288x6480 (12K)": (12288, 6480)
#     }
#     resolution = st.sidebar.radio("🎨 Select Resolution", list(resolution_map.keys()), index=2)
#     num_variations = st.sidebar.slider("🔄 Number of Variations", 1, 5, 1)

#     # Style Presets
#     style_presets = {
#         "None": "",
#         "Cyberpunk": "A futuristic cyberpunk city with neon lights",
#         "Anime": "Anime-style fantasy landscape",
#         "Oil Painting": "A beautiful oil painting of a sunset over the mountains",
#         "Sketch": "A pencil sketch of a medieval castle",
#         "Realistic": "A highly detailed and photorealistic portrait"
#     }
#     style = st.sidebar.selectbox("🎨 Apply Style Preset", list(style_presets.keys()), index=0)

# # ---- 🌟 Main UI - Image Enhancement (Only when Enhancement Mode is On) 🌟 ----
# if st.session_state.enhancement_mode:
#     st.title("✨ Image Enhancement Tool")
#     st.markdown("Enhance your images with AI-powered filters! 🎨")

#     uploaded_file = st.file_uploader("📂 Upload an Image", type=["png", "jpg", "jpeg"])

#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="📸 Original Image", use_column_width=True)

#         # Enhancement Options
#         enhance_options = st.multiselect("🔍 Select Enhancements", ["Sharpen", "Contrast", "Grayscale", "Brightness", "Saturation", "HDR Effect"], default=[])

#         def enhance_image(image, options):
#             if "Sharpen" in options:
#                 image = ImageEnhance.Sharpness(image).enhance(4.0)
#             if "Contrast" in options:
#                 image = ImageEnhance.Contrast(image).enhance(2.5)
#             if "Brightness" in options:
#                 image = ImageEnhance.Brightness(image).enhance(1.8)
#             if "Saturation" in options:
#                 image = ImageEnhance.Color(image).enhance(2.5)
#             if "Grayscale" in options:
#                 image = ImageOps.grayscale(image)
#             if "HDR Effect" in options:
#                 image = ImageEnhance.Contrast(image).enhance(3.0)
#                 image = ImageEnhance.Sharpness(image).enhance(4.0)
#             return image

#         if st.button("✨ Enhance Image"):
#             enhanced_image = enhance_image(image, enhance_options)
#             st.image(enhanced_image, caption="🎨 Enhanced Image", use_column_width=True)

#             # Download Button
#             img_bytes = io.BytesIO()
#             enhanced_image.save(img_bytes, format="PNG")
#             img_bytes = img_bytes.getvalue()
#             st.download_button(label="💾 Download Enhanced Image", data=img_bytes, file_name="enhanced_image.png", mime="image/png")

# # ---- 🌟 Main UI - AI Image Generation (Only when Enhancement Mode is Off) 🌟 ----
# if not st.session_state.enhancement_mode:
#     st.title("🌟 Rachna - AI Image Creator 🌟")
#     st.markdown("**Create stunning AI-generated images with ease!** 🎨✨")

#     prompt = st.text_input("📝 Enter Your Prompt", "A beautiful landscape with mountains and a river")

#     if st.button("🚀 Generate Image"):
#         with st.spinner("Generating... ⏳"):
#             try:
#                 final_prompt = f"{prompt}, {style_presets[style]}" if style_presets[style] else prompt
                
#                 if "history" not in st.session_state:
#                     st.session_state.history = []
                
#                 images = []
#                 cols = st.columns(num_variations)

#                 for i in range(num_variations):
#                     seed = random.randint(1, 1000000)  # Ensure unique variations
#                     variation_prompt = f"{final_prompt}, variation {i+1}, different angle, lighting, and style"
#                     generated_image = client.text_to_image(variation_prompt, model=model, seed=seed)
#                     generated_image = generated_image.resize(resolution_map[resolution])
#                     images.append(generated_image)

#                     with cols[i]:
#                         st.image(generated_image, caption=f"Generated Image {i+1}", use_container_width=True)
#                         img_bytes = io.BytesIO()
#                         generated_image.save(img_bytes, format="PNG")
#                         img_bytes = img_bytes.getvalue()
#                         st.download_button(label=f"💽 Download {i+1}", data=img_bytes, file_name=f"generated_image_{i+1}.png", mime="image/png")
#                         st.session_state.history.append(img_bytes)

#             except Exception as e:
#                 st.error(f"❌ Error: {e}")

# # ---- 🌟 Sidebar - Image History 🌟 ----
# st.sidebar.subheader("📜 Image History")
# if "history" in st.session_state and st.session_state.history:
#     for idx, img_bytes in enumerate(st.session_state.history[-5:]):
#         img = Image.open(io.BytesIO(img_bytes))
#         st.sidebar.image(img, caption=f"History {idx+1}", use_column_width=True)
#         st.sidebar.download_button(label="💽 Download", data=img_bytes, file_name=f"history_image_{idx+1}.png", mime="image/png")

# if st.sidebar.button("🗑️ Clear History"):
#     st.session_state.history = []

# # ---- 🌟 Footer 🌟 ----
# st.markdown("---")
# st.markdown("🔹 **Powered by Stable Diffusion** | Created with ❤️ by AI Enthusiasts ADITYA TIWARI")












#pro1
# import streamlit as st
# from huggingface_hub import InferenceClient
# from PIL import Image, ImageEnhance, ImageOps
# import io
# import random

# # Set Hugging Face API Key from Streamlit Secrets
# HF_API_KEY = st.secrets["HF_API_KEY"]
# client = InferenceClient(api_key=HF_API_KEY)

# # Streamlit UI Configuration
# st.set_page_config(page_title="Rachna - AI Image Creator", page_icon="🎨", layout="wide")

# # ---- 🌟 Sidebar - Settings & Image Enhancement Toggle 🌟 ----
# st.sidebar.header("⚙️ Settings")

# # Initialize session state for enhancement mode
# if "enhancement_mode" not in st.session_state:
#     st.session_state.enhancement_mode = False

# # Toggle function
# def toggle_enhancement():
#     st.session_state.enhancement_mode = not st.session_state.enhancement_mode

# # Button to toggle Image Enhancement mode
# if st.sidebar.button("🖼️ Toggle Image Enhancement"):
#     toggle_enhancement()

# # ---- 🌟 Sidebar - Model Selection (Only if Image Enhancement is OFF) 🌟 ----
# if not st.session_state.enhancement_mode:
#     model = st.sidebar.selectbox(
#         "Select Model",
#         [
#             "stabilityai/stable-diffusion-3.5-large",
#             "stabilityai/stable-diffusion-xl",
#             "stabilityai/stable-diffusion-2-1"
#         ],
#         index=0
#     )

#     # Resolution & Image Variations
#     resolution_map = {
#         "1280x720 (720p)": (1280, 720),
#         "1920x1080 (1080p)": (1920, 1080),
#         "2560x1440 (2K)": (2560, 1440),
#         "3840x2160 (4K)": (3840, 2160),
#         "7680x4320 (8K)": (7680, 4320),
#         "12288x6480 (12K)": (12288, 6480)
#     }
#     resolution = st.sidebar.radio("🎨 Select Resolution", list(resolution_map.keys()), index=2)
#     num_variations = st.sidebar.slider("🔄 Number of Variations", 1, 5, 1)

#     # Style Presets
#     style_presets = {
#         "None": "",
#         "Cyberpunk": "A futuristic cyberpunk city with neon lights",
#         "Anime": "Anime-style fantasy landscape",
#         "Oil Painting": "A beautiful oil painting of a sunset over the mountains",
#         "Sketch": "A pencil sketch of a medieval castle",
#         "Realistic": "A highly detailed and photorealistic portrait"
#     }
#     style = st.sidebar.selectbox("🎨 Apply Style Preset", list(style_presets.keys()), index=0)

# # ---- 🌟 Main UI - Image Enhancement (Only if Enhancement Mode is ON) 🌟 ----
# if st.session_state.enhancement_mode:
#     st.title("✨ Image Enhancement Tool")
#     st.markdown("Enhance your images with AI-powered filters! 🎨")

#     uploaded_file = st.file_uploader("📂 Upload an Image", type=["png", "jpg", "jpeg"])

#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="📸 Original Image", use_container_width=True)  # ✅ FIXED

#         # Enhancement Options
#         enhance_options = st.multiselect("🔍 Select Enhancements", ["Sharpen", "Contrast", "Grayscale", "Brightness", "Saturation", "HDR Effect"], default=[])

#         def enhance_image(image, options):
#             if "Sharpen" in options:
#                 image = ImageEnhance.Sharpness(image).enhance(4.0)
#             if "Contrast" in options:
#                 image = ImageEnhance.Contrast(image).enhance(2.5)
#             if "Brightness" in options:
#                 image = ImageEnhance.Brightness(image).enhance(1.8)
#             if "Saturation" in options:
#                 image = ImageEnhance.Color(image).enhance(2.5)
#             if "Grayscale" in options:
#                 image = ImageOps.grayscale(image)
#             if "HDR Effect" in options:
#                 image = ImageEnhance.Contrast(image).enhance(3.0)
#                 image = ImageEnhance.Sharpness(image).enhance(4.0)
#             return image

#         if st.button("✨ Enhance Image"):
#             enhanced_image = enhance_image(image, enhance_options)
#             st.image(enhanced_image, caption="🎨 Enhanced Image", use_container_width=True)  # ✅ FIXED

#             # Download Button
#             img_bytes = io.BytesIO()
#             enhanced_image.save(img_bytes, format="PNG")
#             img_bytes = img_bytes.getvalue()
#             st.download_button(label="💾 Download Enhanced Image", data=img_bytes, file_name="enhanced_image.png", mime="image/png")

# # ---- 🌟 Main UI - AI Image Generation (Only if Enhancement Mode is OFF) 🌟 ----
# if not st.session_state.enhancement_mode:
#     st.title("🌟 Rachna - AI Image Creator 🌟")
#     st.markdown("**Create stunning AI-generated images with ease!** 🎨✨")

#     prompt = st.text_input("📝 Enter Your Prompt", "A beautiful landscape with mountains and a river")

#     if st.button("🚀 Generate Image"):
#         with st.spinner("Generating... ⏳"):
#             try:
#                 final_prompt = f"{prompt}, {style_presets[style]}" if style_presets[style] else prompt
                
#                 if "history" not in st.session_state:
#                     st.session_state.history = []
                
#                 images = []
#                 cols = st.columns(num_variations)

#                 for i in range(num_variations):
#                     seed = random.randint(1, 1000000)  # Ensure unique variations
#                     variation_prompt = f"{final_prompt}, variation {i+1}, different angle, lighting, and style"
#                     generated_image = client.text_to_image(variation_prompt, model=model, seed=seed)
#                     generated_image = generated_image.resize(resolution_map[resolution])
#                     images.append(generated_image)

#                     with cols[i]:
#                         st.image(generated_image, caption=f"Generated Image {i+1}", use_container_width=True)  # ✅ FIXED
#                         img_bytes = io.BytesIO()
#                         generated_image.save(img_bytes, format="PNG")
#                         img_bytes = img_bytes.getvalue()
#                         st.download_button(label=f"💽 Download {i+1}", data=img_bytes, file_name=f"generated_image_{i+1}.png", mime="image/png")
#                         st.session_state.history.append(img_bytes)

#             except Exception as e:
#                 st.error(f"❌ Error: {e}")

# # ---- 🌟 Sidebar - Image History 🌟 ----
# st.sidebar.subheader("📜 Image History")
# if "history" in st.session_state and st.session_state.history:
#     for idx, img_bytes in enumerate(st.session_state.history[-5:]):
#         img = Image.open(io.BytesIO(img_bytes))
#         st.sidebar.image(img, caption=f"History {idx+1}", use_container_width=True)  # ✅ FIXED
#         st.sidebar.download_button(label="💽 Download", data=img_bytes, file_name=f"history_image_{idx+1}.png", mime="image/png")

# if st.sidebar.button("🗑️ Clear History"):
#     st.session_state.history = []

# # ---- 🌟 Footer 🌟 ----
# st.markdown("---")
# st.markdown("🔹 **Powered by Stable Diffusion** | Created with ❤️ by AI Enthusiasts ADITYA TIWARI")











































import streamlit as st
from huggingface_hub import InferenceClient
from PIL import Image, ImageEnhance, ImageOps
import io
import random

# Set your Hugging Face API key from Streamlit Secrets
HF_API_KEY = st.secrets["HF_API_KEY"]
client = InferenceClient(api_key=HF_API_KEY)

# Streamlit UI Configuration
st.set_page_config(page_title="Rachna - AI Image Creator", page_icon="🎨", layout="wide")

# ---- 🌟 Sidebar Settings 🌟 ----
st.sidebar.header("⚙️ Settings")

# Toggle Mode
if "mode" not in st.session_state:
    st.session_state.mode = "Image Generation"

def toggle_mode():
    st.session_state.mode = "Image Enhancement" if st.session_state.mode == "Image Generation" else "Image Generation"
st.sidebar.button(st.session_state.mode, on_click=toggle_mode)

# Model Selection
model = st.sidebar.selectbox(
    "Select Model",
    ["stabilityai/stable-diffusion-3.5-large", "stabilityai/stable-diffusion-xl", "stabilityai/stable-diffusion-2-1"],
    index=0
)

# Resolution & Image Variations
resolution_map = {
    "1280x720 (720p)": (1280, 720),
    "1920x1080 (1080p)": (1920, 1080),
    "2560x1440 (2K)": (2560, 1440),
    "3840x2160 (4K)": (3840, 2160)
}
resolution = st.sidebar.radio("🎨 Select Resolution", list(resolution_map.keys()), index=2)
num_variations = st.sidebar.slider("🔄 Number of Variations", 1, 3, 1)

# Style Presets
style_presets = {
    "None": "",
    "Cyberpunk": "A futuristic cyberpunk city with neon lights",
    "Anime": "Anime-style fantasy landscape",
    "Oil Painting": "A beautiful oil painting of a sunset over the mountains",
    "Sketch": "A pencil sketch of a medieval castle",
    "Realistic": "A highly detailed and photorealistic portrait"
}
style = st.sidebar.selectbox("🎨 Apply Style Preset", list(style_presets.keys()), index=0)

# ---- 🌟 Main UI 🌟 ----
st.title("🌟 Rachna - AI Image Creator 🌟")
st.markdown("**Create stunning AI-generated images with ease!** 🎨✨")

if st.session_state.mode == "Image Generation":
    prompt = st.text_input("📝 Enter Your Prompt", "A beautiful landscape with mountains and a river")
    if st.button("🚀 Generate Image"):
        with st.spinner("Generating... ⏳"):
            try:
                final_prompt = f"{prompt}, {style_presets[style]}" if style_presets[style] else prompt
                if "history" not in st.session_state:
                    st.session_state.history = []
                
                images = []
                cols = st.columns(num_variations)
                for i in range(num_variations):
                    seed = random.randint(1, 1000000)
                    variation_prompt = f"{final_prompt}, variation {i+1}"
                    generated_image = client.text_to_image(variation_prompt, model=model, seed=seed)
                    generated_image = generated_image.resize(resolution_map[resolution])
                    images.append(generated_image)
                    
                    with cols[i]:
                        st.image(generated_image, caption=f"Generated Image {i+1}", use_container_width=True)
                        img_bytes = io.BytesIO()
                        generated_image.save(img_bytes, format="PNG")
                        img_bytes = img_bytes.getvalue()
                        st.download_button(label=f"💽 Download {i+1}", data=img_bytes, file_name=f"generated_image_{i+1}.png", mime="image/png")
                        st.session_state.history.append(img_bytes)
            except Exception as e:
                st.error(f"❌ Error: {e}")

elif st.session_state.mode == "Image Enhancement":
    uploaded_file = st.file_uploader("📂 Upload an Image for Enhancement", type=["png", "jpg", "jpeg"])
    enhance_options = st.multiselect("🔍 Enhancement Options", ["Sharpen", "Contrast", "Grayscale", "Brightness", "Saturation", "HDR Effect"], default=[])
    
    def enhance_image(image, options):
        if "Sharpen" in options:
            image = ImageEnhance.Sharpness(image).enhance(4.0)
        if "Contrast" in options:
            image = ImageEnhance.Contrast(image).enhance(2.5)
        if "Brightness" in options:
            image = ImageEnhance.Brightness(image).enhance(1.8)
        if "Saturation" in options:
            image = ImageEnhance.Color(image).enhance(2.5)
        if "Grayscale" in options:
            image = ImageOps.grayscale(image)
        if "HDR Effect" in options:
            image = ImageEnhance.Contrast(image).enhance(3.0)
            image = ImageEnhance.Sharpness(image).enhance(4.0)
        return image
    
    if uploaded_file:
        image = Image.open(uploaded_file)
        col1, col2 = st.columns(2)
        with col1:
            st.image(image, caption="🎨 Uploaded Image", use_container_width=True)
        if st.button("✨ Enhance Image"):
            enhanced_image = enhance_image(image, enhance_options)
            with col2:
                st.image(enhanced_image, caption="🎨 Enhanced Image", use_container_width=True)
            img_bytes = io.BytesIO()
            enhanced_image.save(img_bytes, format="PNG")
            img_bytes = img_bytes.getvalue()
            st.download_button(label="💽 Download Enhanced Image", data=img_bytes, file_name="enhanced_image.png", mime="image/png")

# ---- 🌟 History Section 🌟 ----
st.sidebar.subheader("📜 Image History")
if "history" in st.session_state and st.session_state.history:
    for idx, img_bytes in enumerate(st.session_state.history[-5:]):
        img = Image.open(io.BytesIO(img_bytes))
        st.sidebar.image(img, caption=f"History {idx+1}", use_container_width=True)
        st.sidebar.download_button(label="💽 Download", data=img_bytes, file_name=f"history_image_{idx+1}.png", mime="image/png")

if st.sidebar.button("🗑️ Clear History"):
    st.session_state.history = []

# ---- 🌟 Footer 🌟 ----
st.markdown("---")
st.markdown("🔹 **Powered by Stable Diffusion** | Created with ❤️ by AI Enthusiasts ADITYA TIWARI")

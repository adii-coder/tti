
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












# #pro1
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
















# #BEST WORKING
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

# # ---- 🌟 Sidebar - Feature & Quality Options 🌟 ----
# st.sidebar.header("⚙️ Feature & Quality Options")

# # Initialize session state for enhancement mode
# if "enhancement_mode" not in st.session_state:
#     st.session_state.enhancement_mode = False

# def toggle_enhancement():
#     st.session_state.enhancement_mode = not st.session_state.enhancement_mode

# # Button to toggle Image Enhancement mode
# toggle_label = "Image Generation" if st.session_state.enhancement_mode else "Image Enhancement"
# if st.sidebar.button(f"🖼️ {toggle_label}"):
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
#         "3840x2160 (4K)": (3840, 2160)
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
#         st.image(image, caption="📸 Original Image", use_container_width=True)

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
#             st.image(enhanced_image, caption="🎨 Enhanced Image", use_container_width=True)

#             img_bytes = io.BytesIO()
#             enhanced_image.save(img_bytes, format="PNG", quality=90, optimize=True)
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
#                     seed = random.randint(1, 1000000)
#                     variation_prompt = f"{final_prompt}, variation {i+1}, different angle, lighting, and style"
#                     generated_image = client.text_to_image(variation_prompt, model=model, seed=seed)
#                     generated_image = generated_image.resize(resolution_map[resolution])
#                     images.append(generated_image)

#                     with cols[i]:
#                         st.image(generated_image, caption=f"Generated Image {i+1}", use_container_width=True)
#                         img_bytes = io.BytesIO()
#                         generated_image.save(img_bytes, format="PNG", quality=90, optimize=True)
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





















#workingggggggg
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

# # ---- 🌟 Sidebar - Feature & Quality Options 🌟 ----
# st.sidebar.header("⚙️ Feature & Quality Options")

# # Initialize session state for enhancement mode
# if "enhancement_mode" not in st.session_state:
#     st.session_state.enhancement_mode = False

# def toggle_mode():
#     st.session_state.enhancement_mode = not st.session_state.enhancement_mode

# toggle_label = "Image Enhancement" if not st.session_state.enhancement_mode else "Image Generation"
# if st.sidebar.button(f"🖼️ {toggle_label}"):
#     toggle_mode()

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

#     resolution_map = {
#         "1280x720 (720p)": (1280, 720),
#         "1920x1080 (1080p)": (1920, 1080),
#         "2560x1440 (2K)": (2560, 1440),
#         "3840x2160 (4K)": (3840, 2160)
#     }
#     resolution = st.sidebar.radio("🎨 Select Resolution", list(resolution_map.keys()), index=2)
#     num_variations = st.sidebar.slider("🔄 Number of Variations", 1, 5, 1)

#     style_presets = {
#         "None": "",
#         "Cyberpunk": "A futuristic cyberpunk city with neon lights",
#         "Anime": "Anime-style fantasy landscape",
#         "Oil Painting": "A beautiful oil painting of a sunset over the mountains",
#         "Sketch": "A pencil sketch of {prompt}",
#         "Realistic": "A highly detailed and photorealistic portrait"
#     }
#     style = st.sidebar.selectbox("🎨 Apply Style Preset", list(style_presets.keys()), index=0)

# # ---- 🌟 Image Enhancement Mode 🌟 ----
# if st.session_state.enhancement_mode:
#     st.title("✨ Image Enhancement Tool")
#     st.markdown("Enhance your images with AI-powered filters! 🎨")

#     uploaded_file = st.file_uploader("📂 Upload an Image", type=["png", "jpg", "jpeg"])

#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="📸 Original Image", use_container_width=True)

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
#             st.image(enhanced_image, caption="🎨 Enhanced Image", use_container_width=True)
#             img_bytes = io.BytesIO()
#             enhanced_image.save(img_bytes, format="PNG")
#             img_bytes = img_bytes.getvalue()
#             st.download_button(label="💾 Download Enhanced Image", data=img_bytes, file_name="enhanced_image.png", mime="image/png")

# # ---- 🌟 Image Generation Mode 🌟 ----
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
#                     seed = random.randint(1, 1000000)
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
#         st.sidebar.image(img, caption=f"History {idx+1}", use_container_width=True)
#         st.sidebar.download_button(label="💽 Download", data=img_bytes, file_name=f"history_image_{idx+1}.png", mime="image/png")

# if st.sidebar.button("🗑️ Clear History"):
#     st.session_state.history = []

# st.markdown("---")
# st.markdown("🔹 **Powered by Stable Diffusion** | Created with ❤️ by AI Enthusiasts ADITYA TIWARI")

































# import streamlit as st
# from huggingface_hub import InferenceClient
# from PIL import Image, ImageEnhance, ImageOps
# import io
# import random

# # Set Hugging Face API Key from Streamlit Secrets
# HF_API_KEY = st.secrets["HF_API_KEY"]
# client = InferenceClient(api_key=HF_API_KEY)

# # ---- 🌟 UI Configuration ----
# st.set_page_config(page_title="Rachna - AI Image Creator", page_icon="RACHNA-LOGO.png", layout="wide")

# # ---- 🌟 Sidebar - Feature & Quality Options ----
# st.sidebar.header("⚙️ Feature & Quality Options")

# # Initialize session state for enhancement mode
# if "enhancement_mode" not in st.session_state:
#     st.session_state.enhancement_mode = False

# def toggle_mode():
#     st.session_state.enhancement_mode = not st.session_state.enhancement_mode

# toggle_label = "Switch to Image Enhancement" if not st.session_state.enhancement_mode else "Switch to Image Generation"
# st.sidebar.button(f"🖼️ {toggle_label}", on_click=toggle_mode)

# # ---- 🌟 Sidebar - Model Selection (Only if Image Enhancement is OFF) ----
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

#     resolution_map = {
#         "1280x720 (720p)": (1280, 720),
#         "1920x1080 (1080p)": (1920, 1080),
#         "2560x1440 (2K)": (2560, 1440),
#         "3840x2160 (4K)": (3840, 2160)
#     }
#     resolution = st.sidebar.radio("🎨 Select Resolution", list(resolution_map.keys()), index=2)
#     num_variations = st.sidebar.slider("🔄 Number of Variations", 1, 5, 1)

#     style_presets = {
#         "None": "",
#         "Cyberpunk": "A futuristic cyberpunk city with neon lights",
#         "Anime": "Anime-style fantasy landscape",
#         "Oil Painting": "A beautiful oil painting of a sunset over the mountains",
#         "Sketch": "A pencil sketch of {prompt}",
#         "Realistic": "A highly detailed and photorealistic portrait"
#     }
#     style = st.sidebar.selectbox("🎨 Apply Style Preset", list(style_presets.keys()), index=0)

# # ---- 🌟 Image Enhancement Mode ----
# if st.session_state.enhancement_mode:
#     st.title("✨ Image Enhancement Tool")
#     st.markdown("Enhance your images with AI-powered filters! 🎨")

#     uploaded_file = st.file_uploader("📂 Upload an Image", type=["png", "jpg", "jpeg"])

#     if uploaded_file:
#         image = Image.open(uploaded_file)
#         st.image(image, caption="📸 Original Image", use_container_width=True)

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
#             st.image(enhanced_image, caption="🎨 Enhanced Image", use_container_width=True)
#             img_bytes = io.BytesIO()
#             enhanced_image.save(img_bytes, format="PNG")
#             img_bytes = img_bytes.getvalue()
#             st.download_button(label="💾 Download Enhanced Image", data=img_bytes, file_name="enhanced_image.png", mime="image/png")

# # ---- 🌟 Image Generation Mode ----
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
#                     seed = random.randint(1, 1000000)
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

# # ---- 🌟 Sidebar - Image History ----
# st.sidebar.subheader("📜 Image History")
# if "history" in st.session_state and st.session_state.history:
#     for idx, img_bytes in enumerate(st.session_state.history[-5:]):
#         img = Image.open(io.BytesIO(img_bytes))
#         st.sidebar.image(img, caption=f"History {idx+1}", use_container_width=True)
#         st.sidebar.download_button(label="💽 Download", data=img_bytes, file_name=f"history_image_{idx+1}.png", mime="image/png")

# if st.sidebar.button("🗑️ Clear History"):
#     st.session_state.history = []

# st.markdown("---")
# st.markdown("🔹 **Powered by Stable Diffusion** | Created with ❤️ by AI Enthusiasts HARSH SINGH AND ADITYA TIWARI")































































































import json
import streamlit as st
from streamlit.components.v1 import html
from firebase_admin import credentials, auth, firestore, initialize_app
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
import requests

# ---- 🌟 Set Page Config ----
st.set_page_config(page_title="Rachna AI - Image Creator", page_icon="🎨", layout="wide")

# ---- 🌟 Initialize Firebase ----
if "firebase_initialized" not in st.session_state:
    try:
        firebase_json_str = st.secrets["firebase"]["json"]
        firebase_config = json.loads(firebase_json_str)
        cred = credentials.Certificate(firebase_config)
        initialize_app(cred)
        st.session_state.db = firestore.client()
        st.session_state.firebase_initialized = True
    except Exception as e:
        st.error(f"🔥 Firebase Error: {e}")
        st.session_state.firebase_initialized = False

# ---- 🌟 Session Management ----
if "user" not in st.session_state:
    st.session_state.user = None
if "show_login_popup" not in st.session_state:
    st.session_state.show_login_popup = False

# ---- 🌟 Google Login ----
def google_login():
    auth_url = "https://accounts.google.com/o/oauth2/auth"
    client_id = st.secrets["google_client_id"]
    redirect_uri = "https://YOUR_STREAMLIT_APP_URL"
    scope = "email profile openid"
    login_url = f"{auth_url}?client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}&response_type=token"

    st.markdown(f'<a href="{login_url}" target="_self"><button>Login with Google</button></a>', unsafe_allow_html=True)

    token = st.query_params.get("access_token")
    if token:
        try:
            idinfo = id_token.verify_oauth2_token(token, google_requests.Request(), client_id)
            st.session_state.user = idinfo["email"]
            st.experimental_rerun()
        except ValueError:
            st.error("❌ Authentication failed!")

# ---- 🌟 Popup Login ----
def login_popup():
    with st.modal("🔐 Login Required", key="login_modal"):
        st.subheader("Welcome to Rachna AI!")
        st.markdown("Please log in to use the features.")
        google_login()

# ---- 🌟 Protect Features ----
def require_login():
    if not st.session_state.user:
        st.session_state.show_login_popup = True

# ---- 🌟 Sidebar ----
st.sidebar.header("⚙️ Options")
if st.session_state.user:
    st.sidebar.markdown(f"👤 **Logged in as:** `{st.session_state.user}`")
    if st.sidebar.button("🚪 Logout"):
        st.session_state.user = None
        st.experimental_rerun()
else:
    if st.sidebar.button("🔑 Login with Google"):
        require_login()

# ---- 🌟 Main UI ----
st.title("🎨 Rachna AI - Image Creator")
st.markdown("**Create and enhance AI-generated images effortlessly!**")

# ---- 🌟 Image Generation ----
if st.button("🚀 Generate AI Image"):
    require_login()
    if st.session_state.user:
        st.success("✅ Image Generation Started!")
    else:
        login_popup()

# ---- 🌟 Image Enhancement ----
if st.button("✨ Enhance Image"):
    require_login()
    if st.session_state.user:
        st.success("✅ Image Enhancement Ready!")
    else:
        login_popup()

# ---- 🌟 Handle Login Popup ----
if st.session_state.show_login_popup:
    login_popup()

    enhance_options = st.multiselect("🔍 Select Enhancements", ["Sharpen", "Contrast", "Grayscale", "Brightness", "Saturation"], default=[])

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
        return image

    if st.button("✨ Enhance Image"):
        enhanced_image = enhance_image(image, enhance_options)
        st.image(enhanced_image, caption="🎨 Enhanced Image", use_container_width=True)

st.markdown("---")
st.markdown("🔹 **Powered by Stable Diffusion** | Created by HARSH SINGH & ADITYA TIWARI")



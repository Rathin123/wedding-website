import os

# --- CONFIGURATION ---
IMAGE_FOLDER_PATH = './images' 
WEB_PATH_PREFIX = './images/' 
VALID_EXTENSIONS = ('.jpg', '.jpeg', '.png', '.webp')

def generate_html():
    try:
        files = sorted([f for f in os.listdir(IMAGE_FOLDER_PATH) 
                        if f.lower().endswith(VALID_EXTENSIONS)])
        
        if not files:
            print(f"No images found in {IMAGE_FOLDER_PATH}")
            return

        print(f"Found {len(files)} images. Copy the HTML below:\n")
        print("-" * 60)

        for index, filename in enumerate(files):
            # 1. Remove extension (.jpg)
            name_without_ext = os.path.splitext(filename)[0]
            
            # 2. Clean up filename to make a nice Caption
            # Replaces hyphens/underscores with spaces and capitalizes words
            clean_caption = name_without_ext.replace('-', ' ').replace('_', ' ').title()
            
            # 3. Create Alt text (same as caption usually)
            alt_text = clean_caption

            src_path = f"{WEB_PATH_PREFIX}{filename}"

            html_block = f"""
            <!-- Image {index + 1}: {filename} -->
            <div class="gallery-item flex-none w-72 h-96 snap-center cursor-pointer hover:opacity-90 transition-opacity" onclick="openLightbox({index})">
                <img src="{src_path}" 
                     alt="{alt_text}" 
                     data-caption="{clean_caption}" 
                     class="w-full h-full object-cover rounded-lg shadow-md pointer-events-none select-none">
            </div>"""
            
            print(html_block)

        print("-" * 60)

    except FileNotFoundError:
        print(f"Error: The folder '{IMAGE_FOLDER_PATH}' was not found.")

if __name__ == "__main__":
    generate_html()
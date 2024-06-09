#!/usr/bin/env python3

import os
import random
import logging
from http.server import SimpleHTTPRequestHandler, HTTPServer

# Set up logging
logging.basicConfig(filename='/mnt/user/JMStuff/appdatabackup_other/PythonScripts/slideshow.log', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Directory containing photos
PHOTO_DIR = '/mnt/user/Photos_immich/upload'

# Local server IP address and port
SERVER_IP = '192.168.1.8'
SERVER_PORT = 8000

# Serve photos via HTTP
class PhotoHandler(SimpleHTTPRequestHandler):
    def translate_path(self, path):
        return os.path.join(PHOTO_DIR, os.path.relpath(path, '/'))

def start_http_server():
    os.chdir(PHOTO_DIR)
    httpd = HTTPServer((SERVER_IP, SERVER_PORT), PhotoHandler)
    logging.info(f"Serving HTTP on {SERVER_IP}:{SERVER_PORT}")
    httpd.serve_forever()

def generate_slideshow_html(photo_files):
    images_js_array = "[{}]".format(", ".join(f'"{photo}"' for photo in photo_files))
    html_content = f'''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Photo Slideshow</title>
        <style>
            body {{ margin: 0; overflow: hidden; }}
            img {{ width: 100vw; height: 100vh; object-fit: contain; }}
        </style>
    </head>
    <body>
        <img id="slideshow" src="" alt="Slideshow">
        <script>
            const images = {images_js_array};
            let currentIndex = 0;
            function showNextImage() {{
                if (images.length === 0) return;
                document.getElementById('slideshow').src = images[currentIndex];
                currentIndex = (currentIndex + 1) % images.length;
                setTimeout(showNextImage, 10000); // Change slide every 10 seconds
            }}
            showNextImage();
        </script>
    </body>
    </html>
    '''

    with open(os.path.join(PHOTO_DIR, 'slideshow.html'), 'w') as f:
        f.write(html_content)
    logging.info("Generated slideshow.html")

def get_all_photos(directory):
    photo_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
                photo_files.append(f'http://{SERVER_IP}:{SERVER_PORT}/{os.path.relpath(os.path.join(root, file), PHOTO_DIR)}')
    return photo_files

if __name__ == '__main__':
    import threading

    # Generate the slideshow HTML file
    photo_files = get_all_photos(PHOTO_DIR)
    random.shuffle(photo_files)
    generate_slideshow_html(photo_files)

    # Start the HTTP server in a separate thread
    server_thread = threading.Thread(target=start_http_server)
    server_thread.daemon = True
    server_thread.start()

    logging.info(f"Slideshow is available at http://{SERVER_IP}:{SERVER_PORT}/slideshow.html")

    # Keep the main thread running
    while True:
        pass

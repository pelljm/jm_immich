# Photo Slideshow Server

A Python script that serves a directory of photos via HTTP and displays them in a slideshow format.

## Features

- Serves photos from a specified directory.
- Generates a simple HTML page to display photos in a slideshow.
- Changes slides every 10 seconds.
- Logs server activities.

## Requirements

- Python 3.x
- A directory containing photos

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/pelljm/photo-slideshow-server.git
    cd photo-slideshow-server
    ```

2. Install any necessary dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the directories and update the script with your paths:
    - Update `PHOTO_DIR` to point to the directory containing your photos.
    - Update `SERVER_IP` and `SERVER_PORT` if necessary.

## Usage

1. Make the script executable (if needed):
    ```bash
    chmod +x slideshow.py
    ```

2. Run the script:
    ```bash
    ./slideshow.py
    ```

3. Access the slideshow:
    Open your web browser and go to `http://<SERVER_IP>:<SERVER_PORT>/slideshow.html`.

## Logging

- Logs are saved to `/mnt/user/JMStuff/appdatabackup_other/PythonScripts/slideshow.log`.

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b my-feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin my-feature-branch`.
5. Submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact

For questions or issues, please open an issue on GitHub


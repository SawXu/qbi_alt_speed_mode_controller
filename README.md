# qbi_alt_speed_mode_controller

[中文版本](./README_zh.md)

qbi_alt_speed_mode_controller is a Python script to control the alternative speed limits of a qBittorrent server.

## Prerequisites

- Python 3.x
- `requests` library (`pip install requests`)

## Usage

1. Clone the repository or download the script.
2. Install the required library:
    ```bash
    pip install requests
    ```
3. Run the script with the following command:
    ```bash
    python toggle_alt_speed.py <enable> <username> <password> <qb_server_url>
    ```
    - `<enable>`: Set to `true` to enable alternative speed limits, `false` to disable.
    - `<username>`: Your qBittorrent username.
    - `<password>`: Your qBittorrent password.
    - `<qb_server_url>`: The URL of your qBittorrent server (e.g., `http://localhost:8080`).

## Example

```bash
python toggle_alt_speed.py true admin adminpassword http://localhost:8080

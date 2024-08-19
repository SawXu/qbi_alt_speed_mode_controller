# qbi_alt_speed_mode_controller

[English Version](./README.md)

qbi_alt_speed_mode_controller 是一个用于控制 qBittorrent 服务器的备用速度限制的 Python 脚本。

## 前提条件

- Python 3.x
- `requests` 库 (`pip install requests`)

## 使用方法

1. 克隆仓库或下载脚本。
2. 安装所需库：
    ```bash
    pip install requests
    ```
3. 使用以下命令运行脚本：
    ```bash
    python toggle_alt_speed.py <enable> <username> <password> <qb_server_url>
    ```
    - `<enable>`: 设置为 `true` 以启用备用速度限制，设置为 `false` 以禁用。
    - `<username>`: 您的 qBittorrent 用户名。
    - `<password>`: 您的 qBittorrent 密码。
    - `<qb_server_url>`: 您的 qBittorrent 服务器的 URL (例如 `http://localhost:8080`)。

## 示例

```bash
python toggle_alt_speed.py true admin adminpassword http://localhost:8080

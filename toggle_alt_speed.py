import requests
import sys

class QbiController:
    API_LOGIN = 'api/v2/auth/login'
    API_TOGGLE_SPEED_LIMITS_MODE = 'api/v2/transfer/toggleSpeedLimitsMode'
    API_GET_SPEED_LIMITS_MODE = 'api/v2/transfer/speedLimitsMode'


    def __init__(self, qb_server_url: str, username: str, password: str) -> None:
        if not qb_server_url.endswith('/'):
            qb_server_url += '/'
        self.qb_server_url = qb_server_url
        self.username = username
        self.password = password
        self.session = requests.Session()
        pass

    def __get_alt_speed_mode(self) -> int:
        get_url = self.qb_server_url + self.API_GET_SPEED_LIMITS_MODE
        response = self.session.get(get_url)
        if response.status_code == 200:
            if response.text == '1':
                return 1
            elif response.text == '0':
                return 0
        else:
            print(f"Failed to get alternative speed limits. HTTP status code: {response.status_code}")
            return -1

    def control_alt_speed_mode(self, enable: bool) -> int:
        speed_mode = self.__get_alt_speed_mode()
        cur_alt_speed_mode_status: bool = False
        if (speed_mode == 1): 
            cur_alt_speed_mode_status = True
        elif (speed_mode == 0):
            cur_alt_speed_mode_status = False
        else:
            print(f"Failed to get alternative speed limits mode {cur_alt_speed_mode_status}")
            return -1
        
        if (enable != cur_alt_speed_mode_status):
            print(f"Now turning {'on' if enable else 'off'} alternative speed limits")
            ret = self.toggle_alt_speed()
            if (ret != 0):
                print(f"Failed to turn {'on' if enable else 'off'} alternative speed limits")
        else:
            print(f"Already {'on' if enable else 'off'} alternative speed limits")
            ret = 0
        
        return ret

    def toggle_alt_speed(self) -> int:
        # Toggle alternative speed limits
        toggle_url = self.qb_server_url + self.API_TOGGLE_SPEED_LIMITS_MODE
        response = self.session.post(toggle_url)
        if response.status_code == 200:
            print(f"Successfully toggled alternative speed limits. Now turned {'on' if enable else 'off'}.")
            ret = 0
        else:
            print(f"Failed to toggle alternative speed limits. HTTP status code: {response.status_code}")
            ret = -1
        
        return ret

    def login(self) -> int:
            # Ensure the URL ends with a slash
        ret: int = 0

        # Login to qBittorrent
        login_url = self.qb_server_url + self.API_LOGIN
        login_data = {
            'username': username,
            'password': password
        }
        response = self.session.post(login_url, data=login_data)
        if response.status_code != 200 or response.text != 'Ok.':
            print("Failed to login to qBittorrent")
            ret = response.status_code
        return ret



if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python toggle_alt_speed.py <enable> <username> <password> <self.qb_server_url>")
        sys.exit(1)
    
    enable: bool = sys.argv[1].lower() == 'true'
    
    username = sys.argv[2]
    password = sys.argv[3]
    qb_server_url = sys.argv[4]

    qbiController = QbiController(qb_server_url, username, password)

    ret = qbiController.login()
    if (ret != 0):
        print(f"Failed to login to qBittorrent")
    
    ret = qbiController.control_alt_speed_mode(enable)

    if (ret != 0):
        print(f"Failed to turn {'on' if enable else 'off'} alternative speed limits")



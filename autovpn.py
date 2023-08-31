import subprocess
import time
import threading
import ctypes

def user_input_thread():
    global running
    while running:
        user_input = input()
        if user_input.lower() == "exit":
            running = False

def run_as_admin(command):
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", "cmd.exe", "/c " + command, None, 1)
    except:
        print("Ошибка выполнения команды с правами администратора.")

def main():
    global running
    running = True

    # Запуск потока для ввода пользователя
    input_thread = threading.Thread(target=user_input_thread)
    input_thread.start()

    while running:
        # Список конфигурационных файлов
        config_files = ["nl1.ovpn", "nl2.ovpn", "nl3.ovpn", "nl4.ovpn", "nl5.ovpn", "nl6.ovpn", "nl7.ovpn"]
        adapter_name = "Ethernet 3"

        for config_file in config_files:
            print("Запускаю подключение...")
            subprocess.run(["C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe", "--connect", config_file], shell=True)
            print("Подключение завершено.")
            # Здесь указываем количество секунд между переключениями
            time.sleep(200)
            print("Запускаю отключение...")
            subprocess.run(["C:\\Program Files\\OpenVPN\\bin\\openvpn-gui.exe", "--command", "disconnect_all"], shell=True)
            command = f'netsh interface set interface "{adapter_name}" admin=disable'
            run_as_admin(command)
            time.sleep(4)
            command = f'netsh interface set interface "{adapter_name}" admin=enable'
            run_as_admin(command)
            time.sleep(7)
            print("Отключение завершено.")

    input_thread.join()

# Запуск кода
main()



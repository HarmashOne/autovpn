# autovpn
RU:
Программа использует комманды cmd для openvpn-gui, в программе указан полный путь но вы можете добавить его в переменные среды
Список конфигураций находится по умолчанию в C\users\user\OpenVPN\config, так же для переключения необходимо прописать в конфигурации авторизацию (я прописал ее в auth.txt и расположил рядом с конфигом)
TAP Adapter V9 иногда не работает корректно, таким образом вам необходимо поменять в коде тот Ethernet интерфейс который используется адаптером, что бы включать или отключать его. 
ENG:
The program uses cmd commands for openvpn-gui, the program has the full path but you can add it to the environment variables
The list of configurations is located by default in C\users\user\OpenVPN\config, and to switch, you need to register authorization in the configuration (I registered it in auth.txt and placed it next to the config)
TAP Adapter V9 sometimes does not work correctly, so you need to change the Ethernet interface in the code that is used by the adapter to turn it off or on.

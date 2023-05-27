from rich.console import Console
from rich import print as printf
from time import sleep
import speedtest, os
import pyfiglet

os.system('clear')

banner = pyfiglet.figlet_format('SpeedTest')
print(banner)

wifi_test = speedtest.Speedtest()
console = Console()

def Start():
    def wifiTest():
        download = wifi_test.download()
        print(f'Download: {download / 10**6:.2f}MB')

    def uploadping():
        sleep(4)
        upload = wifi_test.upload()
        print(f'Upload: {upload / 10**6:.2f}MB')
        ping = wifi_test.results.ping
        print(f'Ping: {ping / 10**6:.2f}MB')

    with console.status('Testing Download...'):
        wifiTest()

    with console.status('Testing Upload...'):
        uploadping()

if __name__ == '__main__':
    input('Press any key to start the test\n')
    Start()
"""一键启动智析教学助手"""
import os, sys, webbrowser, threading, time
from http.server import HTTPServer, SimpleHTTPRequestHandler
import urllib.parse

PORT = 8765
DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(DIR)

class Handler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        pass

def start_server():
    HTTPServer(("", PORT), Handler).serve_forever()

threading.Thread(target=start_server, daemon=True).start()
time.sleep(0.5)

# URL编码中文文件名，直接打开助手页面
html_name = "智析教学助手.html"
encoded = urllib.parse.quote(html_name)
url = f"http://localhost:{PORT}/{encoded}"
webbrowser.open(url)

print(f"""
╔══════════════════════════════════════╗
║  🎓 智析教学助手 v2.5               ║
║  浏览器已打开                        ║
║  按 Ctrl+C 停止                     ║
╚══════════════════════════════════════╝
""")

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("\n已停止。")
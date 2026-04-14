# -*- coding: utf-8 -*-
import socket
import os

PORT = int(os.environ.get('PORT', 9999))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind(('0.0.0.0', PORT))
server.listen(5)

print(f"🚀 Server đang chạy trên port {PORT}...")

while True:
    try:
        conn, addr = server.accept()
        print(f"✅ Kết nối từ: {addr}")

        data = conn.recv(1024)
        if data:
            print(f"Nhận được: {data.decode('utf-8', errors='ignore')}")

        conn.send("Server da nhan thanh cong tu Render!".encode('utf-8'))
        conn.close()
    except Exception as e:
        print("Lỗi:", e)

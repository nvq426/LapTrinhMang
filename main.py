# -*- coding: utf-8 -*-
import socket
import os

# Lấy port từ Render (bắt buộc)
PORT = int(os.environ.get('PORT', 9999))

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Dùng 0.0.0.0 để Render có thể truy cập từ ngoài
server.bind(('0.0.0.0', PORT))

server.listen(5)
print(f"🚀 Server đang chạy trên port {PORT}...")

while True:
    try:
        conn, addr = server.accept()
        print(f"✅ Client kết nối từ: {addr}")

        data = conn.recv(1024)
        if data:
            print(f"Nhận được: {data.decode('utf-8', errors='ignore')}")

        conn.send("Server da nhan thanh cong! - Render.com".encode('utf-8'))
        conn.close()
    except Exception as e:
        print("Lỗi:", e)
        break

# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Лабораторная работа №7 — Mailer (клиент)

import json
import socket

HOST = "127.0.0.1"
PORT = 50007
BUFFER_SIZE = 65536


def recv_line(sock: socket.socket) -> str:
    buf = b""
    while b"\n" not in buf:
        chunk = sock.recv(BUFFER_SIZE)
        if not chunk:
            raise ConnectionError("соединение закрыто до ответа сервера")
        buf += chunk
    line, _, _ = buf.partition(b"\n")
    return line.decode("utf-8")


def send_to_server(email: str, message: str) -> str:
    payload = {"email": email, "message": message}
    line = json.dumps(payload, ensure_ascii=False) + "\n"
    data = line.encode("utf-8")

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(data)
        return recv_line(s).strip()


def main() -> None:
    while True:
        user_email = input("Email получателя: ").strip()
        text = input("Текст сообщения: ")

        try:
            reply = send_to_server(user_email, text)
        except (ConnectionError, OSError) as e:
            print("Ошибка сети:", e)
            continue

        if reply == "OK":
            print("Сообщение отправлено.")
            break

        print("Ошибка:", reply)
        print("Введите данные заново.\n")


if __name__ == "__main__":
    main()

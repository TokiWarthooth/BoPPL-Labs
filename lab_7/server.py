# Author: Skwisgaar Skwigelf aka Skripnikov Maxim <max.great339@gmail.com>
# Лабораторная работа №7 — Mailer (сервер)

import json
import os
import socket
from email.mime.text import MIMEText
from smtplib import SMTP, SMTPException

HOST = "127.0.0.1"
PORT = 50007
BUFFER_SIZE = 65536


def recv_line(sock: socket.socket) -> str:
    buf = b""
    while b"\n" not in buf:
        chunk = sock.recv(BUFFER_SIZE)
        if not chunk:
            raise ConnectionError("соединение закрыто до получения полной строки")
        buf += chunk
    line, _, _ = buf.partition(b"\n")
    return line.decode("utf-8")


def send_mail(to_email: str, body: str) -> None:
    smtp_host = os.environ.get("SMTP_HOST", "smtp.gmail.com")
    smtp_port = int(os.environ.get("SMTP_PORT", "587"))
    user = os.environ.get("SMTP_USER")
    password = os.environ.get("SMTP_PASSWORD")
    mail_from = os.environ.get("SMTP_FROM", user)

    if not user or not password:
        raise RuntimeError(
            "не заданы переменные окружения SMTP_USER и SMTP_PASSWORD"
        )

    msg = MIMEText(body, "plain", "utf-8")
    msg["Subject"] = "Сообщение от Mailer (лаб. 7)"
    msg["From"] = mail_from
    msg["To"] = to_email

    with SMTP(smtp_host, smtp_port) as smtp:
        smtp.starttls()
        smtp.login(user, password)
        smtp.sendmail(mail_from, [to_email], msg.as_string())


def handle_request(raw: str) -> str:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        return f"ERROR: неверный JSON: {e}"

    email = (data.get("email") or "").strip()
    message = data.get("message")
    if message is None:
        message = ""
    elif not isinstance(message, str):
        return "ERROR: поле message должно быть строкой"

    if not email or "@" not in email:
        return "ERROR: укажите корректный email"

    try:
        send_mail(email, message)
    except (SMTPException, OSError, RuntimeError) as e:
        return f"ERROR: {e}"

    return "OK"


def main() -> None:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind((HOST, PORT))
        s.listen()
        print(f"Mailer-сервер слушает {HOST}:{PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                print("Подключение от", addr)
                try:
                    line = recv_line(conn)
                    reply = handle_request(line)
                except (ConnectionError, UnicodeDecodeError) as e:
                    reply = f"ERROR: {e}"
                conn.sendall((reply + "\n").encode("utf-8"))


if __name__ == "__main__":
    main()

import customtkinter as ctk
import socket
import hashlib
import requests
import threading
import os
import subprocess
import psutil
from tkinter import filedialog

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('green')
c=threading,os
class CyberDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title('Shadow Monarch Cyber Suite')
        self.geometry('1200x800')

        self.output = ctk.CTkTextbox(self, width=850, height=700)
        self.output.pack(side='right', padx=20, pady=20)

        sidebar = ctk.CTkFrame(self, width=300)
        sidebar.pack(side='left', fill='y', padx=20, pady=20)

        tools = [
            ('Port Scanner', self.port_scan),
            ('WiFi Scanner', self.wifi_scan),
            ('Network Info', self.network_info),
            ('Password Checker', self.password_checker),
            ('Hash Generator', self.hash_generator),
            ('DNS Lookup', self.dns_lookup),
            ('IP Geolocation', self.geo_lookup),
            ('Process Monitor', self.process_monitor),
            ('File Hash', self.file_hash)
        ]

        for name, cmd in tools:
            ctk.CTkButton(sidebar, text=name, command=cmd).pack(pady=10, fill='x')

    def log(self, msg):
        self.output.insert('end', msg + '\n')
        self.output.see('end')

    def port_scan(self):
        target = 'scanme.nmap.org'
        self.log(f'Scanning {target}...')
        for port in range(1, 100):
            s = socket.socket()
            s.settimeout(0.3)
            if s.connect_ex((target, port)) == 0:
                self.log(f'[OPEN] Port {port}')
            s.close()

    def wifi_scan(self):
        self.log('Scanning WiFi networks...')
        result = subprocess.getoutput('netsh wlan show networks')
        self.log(result)

    def network_info(self):
        self.log(f'Hostname: {socket.gethostname()}')
        self.log(f'Local IP: {socket.gethostbyname(socket.gethostname())}')

    def password_checker(self):
        self.log('Password analyzer loaded.')

    def hash_generator(self):
        text = 'ShadowMonarch'
        self.log(hashlib.sha256(text.encode()).hexdigest())

    def dns_lookup(self):
        ip = socket.gethostbyname('google.com')
        self.log(f'google.com -> {ip}')

    def geo_lookup(self):
        data = requests.get('http://ip-api.com/json').json()
        self.log(str(data))

    def process_monitor(self):
        for proc in psutil.process_iter(['name']):
            self.log(str(proc.info))

    def file_hash(self):
        file = filedialog.askopenfilename()
        if file:
            with open(file, 'rb') as f:
                self.log(hashlib.sha256(f.read()).hexdigest())

if __name__ == '__main__':
    app = CyberDashboard()
    app.mainloop()

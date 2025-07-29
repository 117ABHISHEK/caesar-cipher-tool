# 🔐 Caesar Cipher Tool

This is a simple CLI tool for encoding and decoding text using the **Caesar Cipher** technique. It supports both encryption and decryption based on a given shift key.

---

## 📦 Features

- 🔁 **Encrypt** text using a shift key
- 🔓 **Decrypt** text using the same key
- 📤 Read input from console or pre-defined values
- 📚 Built with basic JavaScript for quick usage and understanding

---

## 🛠️ Usage

### 🧪 Encrypt
```bash
node caesar.js encrypt "Hello World" 3
# Output: Khoor Zruog
```

### 🔓 Decrypt
```bash
node caesar.js decrypt "Khoor Zruog" 3
# Output: Hello World
```

> Shift value can be any integer (positive or negative).

---

## 📁 Project Structure

```
├── caesar.js          # Main encryption/decryption logic
├── README.md          # Project documentation
├── package.json       # Project config (optional)
```

---

## 🧠 How It Works

The Caesar Cipher shifts each character by a fixed number of places. For example, with a shift of 3:

- A → D  
- B → E  
- ...  
- X → A  
- Y → B  
- Z → C

It wraps around the alphabet and preserves the case.

---

## 👤 Author

**Abhishek**  

---

## 📃 License

This project is licensed under the **MIT License**.

---

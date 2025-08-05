# Password Breach Checker

This project checks if your password has been exposed in any known data breaches by using the **[Have I Been Pwned](https://haveibeenpwned.com/)** API — specifically the **Pwned Passwords** service.

It uses the **K-Anonymity model**, which allows checking passwords securely **without ever sending the full password to the API**.

---

## How It Works

1. **SHA-1 Hashing**  
   The password you enter is converted into a **SHA-1 hash**.  
   Example:  
   ```
   "password123" → CBFDAC6008F9CAB4083784CBD1874F76618D2A97
   ```

2. **Splitting the Hash**  
   Only the **first 5 characters** of the hash are sent to the API.  
   ```
   CBFDA...
   ```

3. **API Search**  
   The API returns a list of hashes starting with those 5 characters, plus the number of times each has been seen in breaches.

4. **Local Matching**  
   The program compares the remaining hash characters locally to check if your exact password is in the breach database.

5. **Output Result**  
   If found, it shows how many times your password appeared in known breaches.  
   If not found, it tells you your password wasn't detected in the database.

---

## Visual Diagram

```
+-------------------+         +--------------------+         +--------------------------+
| Enter Password    |  --->  | SHA-1 Hash          |  --->  | Send first 5 chars to API |
| "mypassword123"   |        | CBFDA...A97         |        | CBFDA                     |
+-------------------+         +--------------------+         +--------------------------+
                                                                      |
                                                                      v
                                                     +--------------------------------+
                                                     | API Returns List of Matching   |
                                                     | Hashes + Breach Counts         |
                                                     +--------------------------------+
                                                                      |
                                                                      v
                                          +-------------------------------------------------+
                                          | Compare Tail Locally                           |
                                          | Match? → Show breach count                     |
                                          | No Match? → "Password NOT found"               |
                                          +-------------------------------------------------+
```

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/password-breach-checker.git
cd password-breach-checker
```

### 2. Install Required Packages
Make sure you have Python installed (3.6+ recommended).  
Install dependencies:
```bash
pip install requests
```

---

## Usage

### Run the Script
```bash
python check_password.py mypassword123 anotherpassword
```

**Example Output:**
```
mypassword123 was found 1523 times... you should change your password!
anotherpassword was NOT found. Carry on!
```

You can check multiple passwords in one command.

---

## Example Demonstration

### Example 1
```bash
python check_password.py password123
```
Output:
```bash
password123 was found 167425 times... you should change your password!
```

### Example 2
```bash
python check_password.py uniqueSecurePass!@#
```
Output:
```bash
uniqueSecurePass!@# was NOT found. Carry on!
```

---

## Why It’s Secure
- The full password **never leaves your computer**.
- Only the **first 5 characters** of the SHA-1 hash are sent to the API.
- This means no one — not even the API provider — knows your full password.
- The API uses **K-Anonymity** so your password remains private.

---

## Security Notes
- This tool is for **personal use** to check if your password has been breached.
- **Do NOT** share your password with anyone, even when using this tool.
- If your password appears in breaches, **change it immediately**.
- Always use **unique, strong passwords** for every account.
- Consider using a **password manager** like Bitwarden, LastPass, or 1Password.

---

## References
- [Have I Been Pwned API Documentation](https://haveibeenpwned.com/API/v3#PwnedPasswords)
- [K-Anonymity Model on Wikipedia](https://en.wikipedia.org/wiki/K-anonymity)
- [SHA-1 Hashing on Wikipedia](https://en.wikipedia.org/wiki/SHA-1)
- [Pwned Passwords Security FAQ](https://haveibeenpwned.com/Passwords)

---

## License



MIT License

Copyright (c) 2025 Ehsanul Haque

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction...

This project is licensed under the MIT License - see the [LICENSE](License) file for details.

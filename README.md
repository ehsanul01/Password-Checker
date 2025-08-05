# Password Breach Checker

This project checks if your password has been exposed in any known data breaches by using the **[Have I Been Pwned](https://haveibeenpwned.com/)** API — specifically the **Pwned Passwords** service.

It uses the **K-Anonymity model**, which allows checking passwords securely **without ever sending the full password to the API**.

---

## How It Works
1. **SHA-1 Hashing**  
   - The password you enter is converted into a **SHA-1 hash** (e.g., `"password123"` → `CBFDAC6008F9CAB4083784CBD1874F76618D2A97`).
   
2. **Splitting the Hash**  
   - Only the **first 5 characters** of the hash are sent to the API.  
     Example: `CBFDA...` → send `"CBFDA"` to the API.

3. **API Search**  
   - The API returns a list of hashes starting with those 5 characters, plus the number of times each has been seen in breaches.

4. **Local Matching**  
   - The program compares the remaining hash characters locally to check if your exact password is in the breach database.

5. **Output Result**  
   - If found, it shows how many times your password appeared in known breaches.
   - If not found, it tells you your password wasn't detected in the database.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/ehasanul01/password-breach-checker.git
cd password-breach-checker
```

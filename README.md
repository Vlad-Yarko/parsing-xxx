# Parsing XXX

---

## 🚀 Launch

1. **Cloning repository**
   - Make sure you have [git](https://git-scm.com/downloads) installed
   - Open any shell on your machine
   - Clone repository
     ```
     git clone {repository url}  
     ```
   - Change current directory to created one
     ```
     cd {repository name}
     ```

2. **Installing and activating virtual environment**
   - Make sure that you have [uv](https://github.com/astral-sh/uv)
   - and any [python interpreter](https://www.python.org/downloads/) installed
   - Create virtual environment:
     ```
     uv venv
     ```
   - Activate your environment
     - Windows:
       ```
       .venv\Scripts\activate
       ```
     - Linux/macOS:
       ```
       source .venv/bin/activate
       ```
   - To change python version you can use
    ```
      uv python pin {version} # 3.12 version by default
    ```
    To change version below **3.10** you will need to change field **required-python** in **pyproject.toml** file
    and after to do command upper

3. **App launch**
    ```
    python main.py
    ```
    or:
    ```
    uv run python main.py
    ```

4. **Logs checking**      
   - In **logs** folder you will find logs file 

---

# Great job! Enjoy!

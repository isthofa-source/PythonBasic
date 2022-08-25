import time
start_time = time.time()
print("Hello World!!")
print("Hallo Nama Saya")
print("Isthofa")
#Ini adalah Comment
"""Dan ini juga comment"""
#Cara install PIP di windows/Linux "python -m ensurepip --default-pip"
#Secara Default python menggunakan interpreter
#Tetapi bisa di compile menggunakan compiler dari python yaitu py_compile
#Cara nya di terminal/cmd "python -m py_compile Main.py"
#Maka akan mengahasilkan file compile di "__pycache__"
#Dan untuk menjalankan nya tinggal masuk di terminal/cmd "python Main.cpython-310.pyc"
#Lalu apa perbedaan dari code yang menggunakan Interpreter dengan yang di Compile (ByteCode)???
#Letak Perbedaan nya pada waktu program untuk melakukan eksekusi sampai selesai
#Pengujian waktu compile bisa menggunakan library python "import time"
#Atau bisa diuji dengan menggunakan perintah : 
#Windows (PowerShell)   : Measure-Command {Start-Process python .\src\Main.py}
# Linux                 : time python .\src\Main.py
print(time.time() - start_time, "Detik")
import cx_Oracle

pool = cx_Oracle.SessionPool("scott", "scott","192.168.10.20:1521/prod", min=2, max=5, increment=1, encoding="UTF-8")

with open("/Users/weimin/Desktop/Coding/WEB/JavaScript/JavaScript/number.txt", "r", encoding="utf-8") as f:
    for data in f.readlines():
        data = data.strip("\n")
        print(data)
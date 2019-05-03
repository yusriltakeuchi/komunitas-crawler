# komunitas-crawler
Tools yang berfungsi untuk melakukan crawling ribuan data komunitas di Indonesia secara serempak dalam jumlah besar serta bisa melakukan pengkategorian berdasarkan kategori komunitas yang ingin dicari. Kemudian data yang berhasil didapat bisa di sync ke dalam database MySQL. Hasil uji tes berhasil mendapatkan 6000++ data komunitas lebih.

# Requirements
- Python3 installed on PC
- MySQL installed on PC

# Installation
```
pip install -r requirements.txt
```

# Configuration
- Create database on MySQL with name komunitas or anything
- Import SQL from SQL Folder named komunitas.sql (if you want to use another database name, please change in komunitas.sql CREATE DATABASE IF NOT EXISTS 'YOUR DATABASE NAME')
- Open json2mysql.py file and edit connection string
```python
connection = pymysql.connect(host='localhost',
                            user='root',
                            password='',
                            db='YOUR DATABASE NAME',
                            charset='utf8mb4',
                            cursorclass=pymysql.cursors.DictCursor)
```

# How to use
```
python komunitas.py
```

## Note
This tool uses a caching system. For the first time it might take a little longer because the caching system is making data and depends on your internet connection.
However, the second search will be much faster

# Screenshot
### Example result in json format
![alt text](https://i.imgur.com/zF6bVWt.png "Example Result in json")

### Homescreen Tools
![alt text](https://i.imgur.com/hqkXiEa.png "Homescreen Tools")

### Crawling Process
![alt text](https://i.imgur.com/wXVtC6W.png "Crawling Process")



import json
import pymysql.cursors
from pprint import pprint

class Json2Mysql():

    def initDB(self):
        # Connect to the database
        connection = pymysql.connect(host='localhost',
                                    user='root',
                                    password='',
                                    db='komunitas',
                                    charset='utf8mb4',
                                    cursorclass=pymysql.cursors.DictCursor)
        return connection

    def __init__(self, dataname):
        self.dataname = dataname
        self.connection = self.initDB() 

    def readData(self):
        with open(self.dataname) as f:
            data = json.load(f)
            return data

    def insertChildField(self, table, columns ,datalist):
        try:
            self.connection = self.initDB()
            cursor = self.connection.cursor()
            for data in datalist:

                sql = "SELECT * from {0} WHERE {1} = %s".format(table, columns)
                cursor.execute(sql, (data))
            
                exists = cursor.fetchone()
                if exists == None:
                    print("        [*] Insert data {} successfully".format(data))
                    sql = "INSERT INTO {} ({}) values(%s)".format(table, columns)
                    cursor = self.connection.cursor()

                    cursor.execute(sql, (data))
                    self.connection.commit()
                    
        except Exception as e:
            print("        [x] {}".format(e))
        finally:
            self.connection.close()

    def insertDetails(self, datalist):
        try:
            self.connection = self.initDB()
            cursor = self.connection.cursor()

            sql = "SELECT * from details WHERE title = %s"
            cursor.execute(sql, (datalist['title']))
        
            exists = cursor.fetchone()
            if exists == None:
                print("        [*] Insert details {} successfully".format(datalist['title']))
                sql = "INSERT INTO details (title, address, city, region, postal_code, phone, description, website, email) values(%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                cursor = self.connection.cursor()

                cursor.execute(sql, (datalist['title'], datalist['address'], datalist['city'], datalist['region'], datalist['postal_code'], datalist['phone'], datalist['description'], datalist['website'], datalist['email']))
                self.connection.commit()
        except Exception as e:
            print("        [x] {}".format(e))
        finally:
            self.connection.close()


    def inserts(self, data):
        try:

            self.connection = self.initDB()
            cursor = self.connection.cursor()

            sql = "SELECT * from detail_list WHERE id_details = %s and id_category = %s and id_social = %s and id_tag = %s"
            cursor.execute(sql, (data['details_id'], data['category_id'], data['social_id'], data['tag_id']))
        
            exists = cursor.fetchone()

            if exists == None:
                print("        [*] Insert details list {} successfully".format(data['details_id']))
                sql = "INSERT INTO detail_list (id_details, id_category, id_social, id_tag) values(%s, %s, %s, %s)"
                cursor = self.connection.cursor()

                cursor.execute(sql, (data['details_id'], data['category_id'], data['social_id'], data['tag_id']))
                self.connection.commit()
                
        except Exception as e:
            print(e)
        finally:
            self.connection.close()

    def getDataDB(self, column, table, where, datalist):
        try:
            for data in datalist:
                self.connection = self.initDB()
                cursor = self.connection.cursor()
                sql = "SELECT {} from {} WHERE {} = %s".format(column, table, where)
                cursor.execute(sql, (data))

                exists = cursor.fetchone()
                print("        [*] Insert {} {} successfully".format(table, data))
                return exists[column]
            
        except Exception as e:
            print("        [x] {}".format(e))
        finally:
            self.connection.close()

    def getDetailID(self, data):
        try:
            self.connection = self.initDB()
            cursor = self.connection.cursor()

            sql = "SELECT id from details WHERE title = %s"
            cursor.execute(sql, (data))
            
            exists = cursor.fetchone()
            print("        [*] Insert details {} successfully".format(data))
            
            return exists['id']

        except Exception as e:
            print("        [x] {}".format(e))
        finally:
            self.connection.close()



import requests
import json
class Buku:
    def __init__(self):
        self.__id=None
        self.__Idbuku = None
        self.__Judulbuku = None
        self.__Penulis = None
        self.__Tahun = None
        self.__Kodebuku = None
        self.__url = "http://localhost/appakademik/buku_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def Idbuku(self):
        return self.__Idbuku
        
    @Idbuku.setter
    def Idbuku(self, value):
        self.__Idbuku = value
    @property
    def Judulbuku(self):
        return self.__Judulbuku
        
    @Judulbuku.setter
    def Judulbuku(self, value):
        self.__Judulbuku = value
    @property
    def Penulis(self):
        return self.__Penulis
        
    @Penulis.setter
    def Penulis(self, value):
        self.__Penulis = value
    @property
    def Tahun(self):
        return self.__Tahun
        
    @Tahun.setter
    def Tahun(self, value):
        self.__Tahun = value
    @property
    def Kodebuku(self):
        return self.__Kodebuku
        
    @Kodebuku.setter
    def Kodebuku(self, value):
        self.__Kodebuku = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_Idbuku(self, Idbuku):
        url = self.__url+"?Idbuku="+Idbuku
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__Idbuku = item['Idbuku']
            self.__Judulbuku = item['Judulbuku']
            self.__Penulis = item['Penulis']
            self.__Tahun = item['Tahun']
            self.__Kodebuku = item['Kodebuku']
        return data
    def simpan(self):
        payload = {
            "Idbuku":self.__Idbuku,
            "Judulbuku":self.__Judulbuku,
            "Penulis":self.__Penulis,
            "Tahun":self.__Tahun,
            "Kodebuku":self.__Kodebuku
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_Idbuku(self, Idbuku):
        url = self.__url+"?Idbuku="+Idbuku
        payload = {
            "Idbuku":self.__Idbuku,
            "Judulbuku":self.__Judulbuku,
            "Penulis":self.__Penulis,
            "Tahun":self.__Tahun,
            "Kodebuku":self.__Kodebuku
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_Idbuku(self,Idbuku):
        url = self.__url+"?Idbuku="+Idbuku
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text
import requests
import json
class Pengembalian:
    def __init__(self):
        self.__id=None
        self.__Idpengembalian = None
        self.__tanggal_pengembalian = None
        self.__kodebuku = None
        self.__nama_mahasiswa = None
        self.__url = "http://localhost/appakademik/pengembalian_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def Idpengembalian(self):
        return self.__Idpengembalian
        
    @Idpengembalian.setter
    def Idpengembalian(self, value):
        self.__Idpengembalian = value
    @property
    def tanggal_pengembalian(self):
        return self.__tanggal_pengembalian
        
    @tanggal_pengembalian.setter
    def tanggal_pengembalian(self, value):
        self.__tanggal_pengembalian = value
    @property
    def kodebuku(self):
        return self.__kodebuku
        
    @kodebuku.setter
    def kodebuku(self, value):
        self.__kodebuku = value
    @property
    def nama_mahasiswa(self):
        return self.__nama_mahasiswa
        
    @nama_mahasiswa.setter
    def nama_mahasiswa(self, value):
        self.__nama_mahasiswa = value
    def get_all(self):
        payload ={}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(self.__url, json=payload, headers=headers)
        return response.text
    def get_by_Idpengembalian(self, Idpengembalian):
        url = self.__url+"?Idpengembalian="+Idpengembalian
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__Idpengembalian = item['Idpengembalian']
            self.__tanggal_pengembalian = item['tanggal_pengembalian']
            self.__kodebuku = item['kodebuku']
            self.__nama_mahasiswa = item['nama_mahasiswa']
        return data
    def simpan(self):
        payload = {
            "Idpengembalian":self.__Idpengembalian,
            "tanggal_pengembalian":self.__tanggal_pengembalian,
            "kodebuku":self.__kodebuku,
            "nama_mahasiswa":self.__nama_mahasiswa
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_Idpengembalian(self, Idpengembalian):
        url = self.__url+"?Idpengembalian="+Idpengembalian
        payload = {
            "Idpengembalian":self.__Idpengembalian,
            "tanggal_pengembalian":self.__tanggal_pengembalian,
            "kodebuku":self.__kodebuku,
            "nama_mahasiswa":self.__nama_mahasiswa
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_Idpengembalian(self,Idpengembalian):
        url = self.__url+"?Idpengembalian="+Idpengembalian
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text

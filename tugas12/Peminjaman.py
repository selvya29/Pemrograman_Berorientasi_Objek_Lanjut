import requests
import json
class Peminjaman:
    def __init__(self):
        self.__id=None
        self.__Idpeminjaman = None
        self.__nama_mahasiswa = None
        self.__tanggal_pinjem = None
        self.__judulbuku = None
        self.__Kodebuku = None
        self.__url = "http://localhost/appakademik/peminjaman_api.php"
                    
    @property
    def id(self):
        return self.__id
    @property
    def Idpeminjaman(self):
        return self.__Idpeminjaman
        
    @Idpeminjaman.setter
    def Idpeminjaman(self, value):
        self.__Idpeminjaman = value
    @property
    def nama_mahasiswa(self):
        return self.__nama_mahasiswa
        
    @nama_mahasiswa.setter
    def nama_mahasiswa(self, value):
        self.__nama_mahasiswa = value
    @property
    def tanggal_pinjem(self):
        return self.__tanggal_pinjem
        
    @tanggal_pinjem.setter
    def tanggal_pinjem(self, value):
        self.__tanggal_pinjem = value
    @property
    def judulbuku(self):
        return self.__judulbuku
        
    @judulbuku.setter
    def judulbuku(self, value):
        self.__judulbuku = value
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
    def get_by_Idpeminjaman(self, Idpeminjaman):
        url = self.__url+"?Idpeminjaman="+Idpeminjaman
        payload = {}
        headers = {'Content-Type': 'application/json'}
        response = requests.get(url, json=payload, headers=headers)
        data = json.loads(response.text)
        for item in data:
            self.__id = item['id']
            self.__Idpeminjaman = item['Idpeminjaman']
            self.__nama_mahasiswa = item['nama_mahasiswa']
            self.__tanggal_pinjem = item['tanggal_pinjem']
            self.__judulbuku = item['judulbuku']
            self.__Kodebuku = item['Kodebuku']
        return data
    def simpan(self):
        payload = {
            "Idpeminjaman":self.__Idpeminjaman,
            "nama_mahasiswa":self.__nama_mahasiswa,
            "tanggal_pinjem":self.__tanggal_pinjem,
            "judulbuku":self.__judulbuku,
            "Kodebuku":self.__Kodebuku
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.post(self.__url, data=payload, headers=headers)
        return response.text
    def update_by_Idpeminjaman(self, Idpeminjaman):
        url = self.__url+"?Idpeminjaman="+Idpeminjaman
        payload = {
            "Idpeminjaman":self.__Idpeminjaman,
            "nama_mahasiswa":self.__nama_mahasiswa,
            "tanggal_pinjem":self.__tanggal_pinjem,
            "judulbuku":self.__judulbuku,
            "Kodebuku":self.__Kodebuku
            }
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        response = requests.put(url, data=payload, headers=headers)
        return response.text
    def delete_by_Idpeminjaman(self,Idpeminjaman):
        url = self.__url+"?Idpeminjaman="+Idpeminjaman
        headers = {'Content-Type': 'application/json'}
        payload={}
        response = requests.delete(url, json=payload, headers=headers)
        return response.text

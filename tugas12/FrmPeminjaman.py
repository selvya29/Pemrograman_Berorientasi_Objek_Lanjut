import tkinter as tk
import json
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox
from Peminjaman import *
class FrmPeminjaman:
    
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        Label(mainFrame, text='IDPEMINJAMAN:').grid(row=0, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='NAMA_MAHASISWA:').grid(row=1, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='TANGGAL_PINJEM:').grid(row=2, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='JUDULBUKU:').grid(row=3, column=0,
            sticky=W, padx=5, pady=5)
        Label(mainFrame, text='KODEBUKU:').grid(row=4, column=0,
            sticky=W, padx=5, pady=5)
        # Textbox
        self.txtIdpeminjaman = Entry(mainFrame) 
        self.txtIdpeminjaman.grid(row=0, column=1, padx=5, pady=5)
        self.txtIdpeminjaman.bind("<Return>",self.onCari) # menambahkan event Enter key
        # Textbox
        self.txtNama_mahasiswa = Entry(mainFrame) 
        self.txtNama_mahasiswa.grid(row=1, column=1, padx=5, pady=5)
        # Textbox
        self.txtTanggal_pinjem = Entry(mainFrame) 
        self.txtTanggal_pinjem.grid(row=2, column=1, padx=5, pady=5)
        # Textbox
        self.txtJudulbuku = Entry(mainFrame) 
        self.txtJudulbuku.grid(row=3, column=1, padx=5, pady=5)
        # Textbox
        self.txtKodebuku = Entry(mainFrame) 
        self.txtKodebuku.grid(row=4, column=1, padx=5, pady=5)
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        # define columns
        columns = ('id','Idpeminjaman','nama_mahasiswa','tanggal_pinjem','judulbuku','Kodebuku')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='ID')
        self.tree.column('id', width="50")
        self.tree.heading('Idpeminjaman', text='IDPEMINJAMAN')
        self.tree.column('Idpeminjaman', width="150")
        self.tree.heading('nama_mahasiswa', text='NAMA_MAHASISWA')
        self.tree.column('nama_mahasiswa', width="200")
        self.tree.heading('tanggal_pinjem', text='TANGGAL_PINJEM')
        self.tree.column('tanggal_pinjem', width="200")
        self.tree.heading('judulbuku', text='JUDULBUKU')
        self.tree.column('judulbuku', width="250")
        self.tree.heading('Kodebuku', text='KODEBUKU')
        self.tree.column('Kodebuku', width="100")
        # set tree position
        self.tree.place(x=0, y=200)
        
    def onClear(self, event=None):
        self.txtIdpeminjaman.delete(0,END)
        self.txtIdpeminjaman.insert(END,"")
        self.txtNama_mahasiswa.delete(0,END)
        self.txtNama_mahasiswa.insert(END,"")
        self.txtTanggal_pinjem.delete(0,END)
        self.txtTanggal_pinjem.insert(END,"")
        self.txtJudulbuku.delete(0,END)
        self.txtJudulbuku.insert(END,"")
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,"")
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data peminjaman
        obj = Peminjaman()
        result = obj.get_all()
        parsed_data = json.loads(result)
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for i, d in enumerate(parsed_data):
            self.tree.insert("", i, text="Item {}".format(i), values=(d["id"],d["Idpeminjaman"],d["nama_mahasiswa"],d["tanggal_pinjem"],d["judulbuku"],d["Kodebuku"]))
    def onCari(self, event=None):
        Idpeminjaman = self.txtIdpeminjaman.get()
        obj = Peminjaman()
        a = obj.get_by_Idpeminjaman(Idpeminjaman)
        if(len(a)>0):
            self.TampilkanData()
            self.ditemukan = True
        else:
            self.ditemukan = False
            messagebox.showinfo("showinfo", "Data Tidak Ditemukan")
    def TampilkanData(self, event=None):
        Idpeminjaman = self.txtIdpeminjaman.get()
        obj = Peminjaman()
        res = obj.get_by_Idpeminjaman(Idpeminjaman)
        self.txtIdpeminjaman.delete(0,END)
        self.txtIdpeminjaman.insert(END,obj.Idpeminjaman)
        self.txtNama_mahasiswa.delete(0,END)
        self.txtNama_mahasiswa.insert(END,obj.nama_mahasiswa)
        self.txtTanggal_pinjem.delete(0,END)
        self.txtTanggal_pinjem.insert(END,obj.tanggal_pinjem)
        self.txtJudulbuku.delete(0,END)
        self.txtJudulbuku.insert(END,obj.judulbuku)
        self.txtKodebuku.delete(0,END)
        self.txtKodebuku.insert(END,obj.Kodebuku)
        self.btnSimpan.config(text="Update")
                 
    def onSimpan(self, event=None):
        # get the data from input
        Idpeminjaman = self.txtIdpeminjaman.get()
        nama_mahasiswa = self.txtNama_mahasiswa.get()
        tanggal_pinjem = self.txtTanggal_pinjem.get()
        judulbuku = self.txtJudulbuku.get()
        Kodebuku = self.txtKodebuku.get()
        # create new Object
        obj = Peminjaman()
        obj.Idpeminjaman = Idpeminjaman
        obj.nama_mahasiswa = nama_mahasiswa
        obj.tanggal_pinjem = tanggal_pinjem
        obj.judulbuku = judulbuku
        obj.Kodebuku = Kodebuku
        if(self.ditemukan==False):
            # save the record
            res = obj.simpan()
        else:
            # update the record
            res = obj.update_by_Idpeminjaman(Idpeminjaman)
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        #clear the form input
        self.onClear()
    def onDelete(self, event=None):
        Idpeminjaman = self.txtIdpeminjaman.get()
        obj = Peminjaman()
        obj.Idpeminjaman = Idpeminjaman
        if(self.ditemukan==True):
            res = obj.delete_by_Idpeminjaman(Idpeminjaman)
        else:
            messagebox.showinfo("showinfo", "Data harus ditemukan dulu sebelum dihapus")
            
        # read data in json format
        data = json.loads(res)
        status = data["status"]
        msg = data["message"]
        
        # display json data into messagebox
        messagebox.showinfo("showinfo", status+', '+msg)
        
        self.onClear()
            
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()
if __name__ == '__main__':
    root2 = tk.Tk()
    aplikasi = FrmPeminjaman(root2, "Aplikasi Data Peminjaman")
    root2.mainloop()
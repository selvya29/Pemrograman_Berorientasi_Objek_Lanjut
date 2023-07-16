<?php
//Simpanlah dengan nama file : Peminjaman.php
require_once 'database.php';
class Peminjaman 
{
    private $db;
    private $table = 'peminjaman';
    public $Idpeminjaman = "";
    public $nama_mahasiswa = "";
    public $tanggal_pinjem = "";
    public $judulbuku = "";
    public $Kodebuku = "";
    public function __construct(MySQLDatabase $db)
    {
        $this->db = $db;
    }
    public function get_all() 
    {
        $query = "SELECT * FROM $this->table";
        $result_set = $this->db->query($query);
        return $result_set;
    }
    public function get_by_id(int $id)
    {
        $query = "SELECT * FROM $this->table WHERE id = $id";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function get_by_Idpeminjaman(int $Idpeminjaman)
    {
        $query = "SELECT * FROM $this->table WHERE Idpeminjaman = $Idpeminjaman";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`Idpeminjaman`,`nama_mahasiswa`,`tanggal_pinjem`,`judulbuku`,`Kodebuku`) VALUES ('$this->Idpeminjaman','$this->nama_mahasiswa','$this->tanggal_pinjem','$this->judulbuku','$this->Kodebuku')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET Idpeminjaman = '$this->Idpeminjaman', nama_mahasiswa = '$this->nama_mahasiswa', tanggal_pinjem = '$this->tanggal_pinjem', judulbuku = '$this->judulbuku', Kodebuku = '$this->Kodebuku' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_Idpeminjaman($Idpeminjaman): int
    {
        $query = "UPDATE $this->table SET Idpeminjaman = '$this->Idpeminjaman', nama_mahasiswa = '$this->nama_mahasiswa', tanggal_pinjem = '$this->tanggal_pinjem', judulbuku = '$this->judulbuku', Kodebuku = '$this->Kodebuku' 
        WHERE Idpeminjaman = $Idpeminjaman";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_Idpeminjaman($Idpeminjaman): int
    {
        $query = "DELETE FROM $this->table WHERE Idpeminjaman = $Idpeminjaman";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>
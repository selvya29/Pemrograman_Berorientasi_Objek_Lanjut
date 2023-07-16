<?php
//Simpanlah dengan nama file : Pengembalian.php
require_once 'database.php';
class Pengembalian 
{
    private $db;
    private $table = 'pengembalian';
    public $Idpengembalian = "";
    public $tanggal_pengembalian = "";
    public $kodebuku = "";
    public $nama_mahasiswa = "";
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
    public function get_by_Idpengembalian(int $Idpengembalian)
    {
        $query = "SELECT * FROM $this->table WHERE Idpengembalian = $Idpengembalian";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`Idpengembalian`,`tanggal_pengembalian`,`kodebuku`,`nama_mahasiswa`) VALUES ('$this->Idpengembalian','$this->tanggal_pengembalian','$this->kodebuku','$this->nama_mahasiswa')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET Idpengembalian = '$this->Idpengembalian', tanggal_pengembalian = '$this->tanggal_pengembalian', kodebuku = '$this->kodebuku', nama_mahasiswa = '$this->nama_mahasiswa' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_Idpengembalian($Idpengembalian): int
    {
        $query = "UPDATE $this->table SET Idpengembalian = '$this->Idpengembalian', tanggal_pengembalian = '$this->tanggal_pengembalian', kodebuku = '$this->kodebuku', nama_mahasiswa = '$this->nama_mahasiswa' 
        WHERE Idpengembalian = $Idpengembalian";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_Idpengembalian($Idpengembalian): int
    {
        $query = "DELETE FROM $this->table WHERE Idpengembalian = $Idpengembalian";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>
<?php
//Simpanlah dengan nama file : Karyawan.php
require_once 'database.php';
class Karyawan 
{
    private $db;
    private $table = 'karyawan';
    public $nip = "";
    public $nama = "";
    public $jk = "";
    public $tempat_lahir = "";
    public $alamat = "";
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
    public function get_by_nip(int $nip)
    {
        $query = "SELECT * FROM $this->table WHERE nip = $nip";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`nip`,`nama`,`jk`,`tempat_lahir`,`alamat`) VALUES ('$this->nip','$this->nama','$this->jk','$this->tempat_lahir','$this->alamat')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET nip = '$this->nip', nama = '$this->nama', jk = '$this->jk', tempat_lahir = '$this->tempat_lahir', alamat = '$this->alamat' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_nip($nip): int
    {
        $query = "UPDATE $this->table SET nip = '$this->nip', nama = '$this->nama', jk = '$this->jk', tempat_lahir = '$this->tempat_lahir', alamat = '$this->alamat' 
        WHERE nip = $nip";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_nip($nip): int
    {
        $query = "DELETE FROM $this->table WHERE nip = $nip";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>
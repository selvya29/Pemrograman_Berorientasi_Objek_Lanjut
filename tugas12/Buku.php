<?php
//Simpanlah dengan nama file : Buku.php
require_once 'database.php';
class Buku 
{
    private $db;
    private $table = 'buku';
    public $Idbuku = "";
    public $Judulbuku = "";
    public $Penulis = "";
    public $Tahun = "";
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
    public function get_by_Idbuku(int $Idbuku)
    {
        $query = "SELECT * FROM $this->table WHERE Idbuku = $Idbuku";
        $result_set = $this->db->query($query);   
        return $result_set;
    }
    public function insert(): int
    {
        $query = "INSERT INTO $this->table (`Idbuku`,`Judulbuku`,`Penulis`,`Tahun`,`Kodebuku`) VALUES ('$this->Idbuku','$this->Judulbuku','$this->Penulis','$this->Tahun','$this->Kodebuku')";
        $this->db->query($query);
        return $this->db->insert_id();
    }
    public function update(int $id): int
    {
        $query = "UPDATE $this->table SET Idbuku = '$this->Idbuku', Judulbuku = '$this->Judulbuku', Penulis = '$this->Penulis', Tahun = '$this->Tahun', Kodebuku = '$this->Kodebuku' 
        WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function update_by_Idbuku($Idbuku): int
    {
        $query = "UPDATE $this->table SET Idbuku = '$this->Idbuku', Judulbuku = '$this->Judulbuku', Penulis = '$this->Penulis', Tahun = '$this->Tahun', Kodebuku = '$this->Kodebuku' 
        WHERE Idbuku = $Idbuku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete(int $id): int
    {
        $query = "DELETE FROM $this->table WHERE id = $id";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
    public function delete_by_Idbuku($Idbuku): int
    {
        $query = "DELETE FROM $this->table WHERE Idbuku = $Idbuku";
        $this->db->query($query);
        return $this->db->affected_rows();
    }
}
?>
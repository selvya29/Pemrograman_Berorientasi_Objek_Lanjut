<?php
require_once 'database.php';
require_once 'Peminjaman.php';
$db = new MySQLDatabase();
$peminjaman = new Peminjaman($db);
$id=0;
$Idpeminjaman=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['Idpeminjaman'])){
            $Idpeminjaman = $_GET['Idpeminjaman'];
        }
        if($id>0){    
            $result = $peminjaman->get_by_id($id);
        }elseif($Idpeminjaman>0){
            $result = $peminjaman->get_by_Idpeminjaman($Idpeminjaman);
        } else {
            $result = $peminjaman->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new peminjaman
        $peminjaman->Idpeminjaman = $_POST['Idpeminjaman'];
        $peminjaman->nama_mahasiswa = $_POST['nama_mahasiswa'];
        $peminjaman->tanggal_pinjem = $_POST['tanggal_pinjem'];
        $peminjaman->judulbuku = $_POST['judulbuku'];
        $peminjaman->Kodebuku = $_POST['Kodebuku'];
       
        $peminjaman->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman not created.';
        }
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'PUT':
        // Update an existing data
        $_PUT = [];
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['Idpeminjaman'])){
            $Idpeminjaman = $_GET['Idpeminjaman'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $peminjaman->Idpeminjaman = $_PUT['Idpeminjaman'];
        $peminjaman->nama_mahasiswa = $_PUT['nama_mahasiswa'];
        $peminjaman->tanggal_pinjem = $_PUT['tanggal_pinjem'];
        $peminjaman->judulbuku = $_PUT['judulbuku'];
        $peminjaman->Kodebuku = $_PUT['Kodebuku'];
        if($id>0){    
            $peminjaman->update($id);
        }elseif($Idpeminjaman<>""){
            $peminjaman->update_by_Idpeminjaman($Idpeminjaman);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['Idpeminjaman'])){
            $Idpeminjaman = $_GET['Idpeminjaman'];
        }
        if($id>0){    
            $peminjaman->delete($id);
        }elseif($Idpeminjaman>0){
            $peminjaman->delete_by_Idpeminjaman($Idpeminjaman);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Peminjaman deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Peminjaman delete failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    default:
        header("HTTP/1.0 405 Method Not Allowed");
        break;
    }
$db->close()
?>
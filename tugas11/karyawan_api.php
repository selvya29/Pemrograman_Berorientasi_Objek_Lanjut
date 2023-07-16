<?php
require_once 'database.php';
require_once 'Karyawan.php';
$db = new MySQLDatabase();
$karyawan = new Karyawan($db);
$id=0;
$nip=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nip'])){
            $nip = $_GET['nip'];
        }
        if($id>0){    
            $result = $karyawan->get_by_id($id);
        }elseif($nip>0){
            $result = $karyawan->get_by_nip($nip);
        } else {
            $result = $karyawan->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new karyawan
        $karyawan->nip = $_POST['nip'];
        $karyawan->nama = $_POST['nama'];
        $karyawan->jk = $_POST['jk'];
        $karyawan->tempat_lahir = $_POST['tempat_lahir'];
        $karyawan->alamat = $_POST['alamat'];
       
        $karyawan->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Karyawan created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Karyawan not created.';
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
        if(isset($_GET['nip'])){
            $nip = $_GET['nip'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $karyawan->nip = $_PUT['nip'];
        $karyawan->nama = $_PUT['nama'];
        $karyawan->jk = $_PUT['jk'];
        $karyawan->tempat_lahir = $_PUT['tempat_lahir'];
        $karyawan->alamat = $_PUT['alamat'];
        if($id>0){    
            $karyawan->update($id);
        }elseif($nip<>""){
            $karyawan->update_by_nip($nip);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Karyawan updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Karyawan update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['nip'])){
            $nip = $_GET['nip'];
        }
        if($id>0){    
            $karyawan->delete($id);
        }elseif($nip>0){
            $karyawan->delete_by_nip($nip);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Karyawan deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Karyawan delete failed.';
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
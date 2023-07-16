<?php
require_once 'database.php';
require_once 'Pengembalian.php';
$db = new MySQLDatabase();
$pengembalian = new Pengembalian($db);
$id=0;
$Idpengembalian=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['Idpengembalian'])){
            $Idpengembalian = $_GET['Idpengembalian'];
        }
        if($id>0){    
            $result = $pengembalian->get_by_id($id);
        }elseif($Idpengembalian>0){
            $result = $pengembalian->get_by_Idpengembalian($Idpengembalian);
        } else {
            $result = $pengembalian->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new pengembalian
        $pengembalian->Idpengembalian = $_POST['Idpengembalian'];
        $pengembalian->tanggal_pengembalian = $_POST['tanggal_pengembalian'];
        $pengembalian->kodebuku = $_POST['kodebuku'];
        $pengembalian->nama_mahasiswa = $_POST['nama_mahasiswa'];
       
        $pengembalian->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian not created.';
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
        if(isset($_GET['Idpengembalian'])){
            $Idpengembalian = $_GET['Idpengembalian'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $pengembalian->Idpengembalian = $_PUT['Idpengembalian'];
        $pengembalian->tanggal_pengembalian = $_PUT['tanggal_pengembalian'];
        $pengembalian->kodebuku = $_PUT['kodebuku'];
        $pengembalian->nama_mahasiswa = $_PUT['nama_mahasiswa'];
        if($id>0){    
            $pengembalian->update($id);
        }elseif($Idpengembalian<>""){
            $pengembalian->update_by_Idpengembalian($Idpengembalian);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['Idpengembalian'])){
            $Idpengembalian = $_GET['Idpengembalian'];
        }
        if($id>0){    
            $pengembalian->delete($id);
        }elseif($Idpengembalian>0){
            $pengembalian->delete_by_Idpengembalian($Idpengembalian);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Pengembalian deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Pengembalian delete failed.';
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
<?php
require_once 'database.php';
require_once 'Buku.php';
$db = new MySQLDatabase();
$buku = new Buku($db);
$id=0;
$Idbuku=0;
// Check the HTTP request method
$method = $_SERVER['REQUEST_METHOD'];
// Handle the different HTTP methods
switch ($method) {
    case 'GET':
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['Idbuku'])){
            $Idbuku = $_GET['Idbuku'];
        }
        if($id>0){    
            $result = $buku->get_by_id($id);
        }elseif($Idbuku>0){
            $result = $buku->get_by_Idbuku($Idbuku);
        } else {
            $result = $buku->get_all();
        }        
       
        $val = array();
        while ($row = $result->fetch_assoc()) {
            $val[] = $row;
        }
        
        header('Content-Type: application/json');
        echo json_encode($val);
        break;
    
    case 'POST':
        // Add a new buku
        $buku->Idbuku = $_POST['Idbuku'];
        $buku->Judulbuku = $_POST['Judulbuku'];
        $buku->Penulis = $_POST['Penulis'];
        $buku->Tahun = $_POST['Tahun'];
        $buku->Kodebuku = $_POST['Kodebuku'];
       
        $buku->insert();
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku created successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku not created.';
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
        if(isset($_GET['Idbuku'])){
            $Idbuku = $_GET['Idbuku'];
        }
        parse_str(file_get_contents("php://input"), $_PUT);
        $buku->Idbuku = $_PUT['Idbuku'];
        $buku->Judulbuku = $_PUT['Judulbuku'];
        $buku->Penulis = $_PUT['Penulis'];
        $buku->Tahun = $_PUT['Tahun'];
        $buku->Kodebuku = $_PUT['Kodebuku'];
        if($id>0){    
            $buku->update($id);
        }elseif($Idbuku<>""){
            $buku->update_by_Idbuku($Idbuku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku updated successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku update failed.';
        }        
        header('Content-Type: application/json');
        echo json_encode($data);
        break;
    case 'DELETE':
        // Delete a user
        if(isset($_GET['id'])){
            $id = $_GET['id'];
        }
        if(isset($_GET['Idbuku'])){
            $Idbuku = $_GET['Idbuku'];
        }
        if($id>0){    
            $buku->delete($id);
        }elseif($Idbuku>0){
            $buku->delete_by_Idbuku($Idbuku);
        } else {
            
        } 
        
        $a = $db->affected_rows();
        if($a>0){
            $data['status']='success';
            $data['message']='Data Buku deleted successfully.';
        } else {
            $data['status']='failed';
            $data['message']='Data Buku delete failed.';
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
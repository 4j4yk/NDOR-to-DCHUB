<?php

$ftp_server = ""; //server details are available on local machine 
$ftp_user = "";
$ftp_pass = "";

// set up a connection or die
$conn_id = ftp_connect($ftp_server) or die("Couldn't connect to $ftp_server"); 

// try to login
if (@ftp_login($conn_id, $ftp_user, $ftp_pass)) {
    echo "Connected as $ftp_user@$ftp_server\n";
} else {
    echo "Couldn't connect as $ftp_user\n";
}

//$files = ftp_nlist($conn_id, $currDir);
//var_dump($files);

//function that lists through directories on FTP server
//searchDirectory($conn_id, "/");

//DOWNLOAD FILE LINE!!!!!
$local = fopen("C:\Users\rex\Dropbox\project\test.doc", 'w');
if(ftp_fget($conn_id, $local, "/Bridge Document Management System/MAINTENANCE/FC Inspection Reports (BR293)/County/C000101305/NDORSpecialInspectionDR form 7.doc", FTP_BINARY, 0))
{
	print("Wrote file\n");
}
else
{
	print("Failed to write file\n");
}
fclose($local);

// close the connection
ftp_close($conn_id);  

//recursive function to read all files in specified directory
function searchDirectory($conn_id, $currDir)
{
	//checks to see if the file actually exists
	//if(!file_exists("$currDir")){
	//	print("Failure to read from specified path\n");
	//	return;
	//}

	//obtain a list of all files in current directory	
	$files = ftp_nlist($conn_id, "$currDir");
	$raws = ftp_rawlist($conn_id, "$currDir");

	//loop that goes through list of all files in current directory
	for ($i = 0; $i < count($files); $i++){		
		//"." & ".." directories: ignore
		if($files[$i] == "." || $files[$i] == ".."){
			//do nothing
		}

		//directories
		elseif($raws[$i][0] == 'd'){
			//Lists the files, one case at a time
			if($currDir == '/')
			{
				$newDir = $currDir . $files[$i];
			}
			else
			{
				$newDir = $currDir . '/' . $files[$i];
			}
			print($newDir . "\n");
			searchDirectory($conn_id, $newDir);
		}

		//files (or rather everything else. Didn't account for links, etc.)
		else{
			//Lists the files, one case at a time
			print($currDir . '/' . $files[$i] . "\n");
			
			//This is a file. Will end up doing things
		}
	}
}
?>
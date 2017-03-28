<?php
$base_dir = $argv[1];
$dataset_id = $argv[2];

//echo $base_dir . '/' . $dataset_id;

if(!file_exists($base_dir . '/' . $dataset_id)){
	echo "fail\n";
}

searchDir($base_dir . '/' . $dataset_id, $dataset_id);

//recursive function to read all files in specified directory
function searchDir($absPath, $dataset_id)
{
	//checks to see if there isn't any data to bag	
	if(!file_exists($absPath)){
		return;
	}

	//obtain a list of all files in current directory	
	$allFiles = scandir($absPath);

	//loop that goes through list of all files in current directory
	foreach ($allFiles as $file){
		//echo $absPath . "/" . $file . "\n";		

		//"." & ".." directories: ignore
		if($file == "." || $file == ".."){
			//do nothing
		}

		//files: directly adds file
		elseif(is_file($absPath . "/"  . $file)){
			$directory_tree = explode('/', $absPath);
			$experiment_id = $directory_tree[count($directory_tree) - 2];
			$category = $directory_tree[count($directory_tree) - 1];
			
			//********** INSERT UPLOAD_FILE CODE ********
			upload_file($file, $dataset_id, $experiment_id, $category);
			//********** INSERT UPLOAD_FILE CODE ********
		}

		//directories: creates new directory within bag and 
		// recursively calls the function again to bag all files in
		// given subdirectory
		else{
			$tmpDir = $absPath . "/" . $file;
			searchDir($tmpDir, $dataset_id);
		}
	}
}

function upload_file($file, $dataset_id, $experiment_id, $category)
{
	//********** INSERT UPLOAD_FILE CODE ********
	print("Will do a thing!\nParameters: $file, $dataset_id, $experiment_id, $category\n");
	return;
}
?>
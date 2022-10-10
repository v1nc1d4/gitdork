<?php
//Tu5b0l3d -idX-
//http://blog.indoxploit.or.id/2016/06/google-dorker-new.html
error_reporting(0);
function save($data){
		$fp = @fopen("hasil.htm", "a") or die("cant open file");
		fwrite($fp, $data);
		fclose($fp);
}
$list = array();
$b = 5;
$dorks = "intext:IndoXploit";
$dork = urlencode($dorks);
	for($i=0;$i+=$b;$i++){
		$kuki = rand();
		echo $i;
		//http://ajax.googleapis.com/ajax/services/search/web?v=1.0&hl=iw&rsz=8&q=$dork&key=$kunAPI&start=$i
		$ch1 = curl_init ("https://www.google.com/search?q=$dork&btnG=Search&start=$i#q=$dork&start=$i");
curl_setopt ($ch1, CURLOPT_RETURNTRANSFER, 1);
curl_setopt ($ch1, CURLOPT_FOLLOWLOCATION, 1);
	curl_setopt ($ch1, CURLOPT_USERAGENT, "Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0");
curl_setopt ($ch1, CURLOPT_SSL_VERIFYPEER, 0);
curl_setopt ($ch1, CURLOPT_SSL_VERIFYHOST, 0);
curl_setopt($ch1, CURLOPT_COOKIEJAR,"$kuki.txt");
curl_setopt($ch1, CURLOPT_COOKIEFILE,"$kuki.txt");
$result = curl_exec ($ch1); 

preg_match_all("/style=\"white-space:nowrap\"><c(.*?)\//", $result, $a);
foreach($a[1] as $sitesn){
$sites = explode("ite class=\"_Rm\">", $sitesn);


	

	
	

}
else{
	echo "$sulton ============================>\n";
}
}

}
?>

<?php

  $S = trim(fgets(STDIN));
  (1<=strlen($S)&&strlen($S)<=100) ? "" : exit();
  $ary = array();
  $p="";
  $n = "";
  $pp = 0;
  $c = 0;
  for($i = 0;$i<strlen($S);$i++){
    $p = $S[$i];
    $n = $S[($i<strlen($S)-1?$i+1:$i)];
    $ary[$pp] = empty($ary[$pp]) ? '' : $ary[$pp];
    if($p==$n){
      $ary[$pp] .= $S[$i];
      $c++;
    }else{
      $c = 0;
      $ary[$pp++] .= $S[$i];
    }
  }
  $t = "";
  foreach($ary as $val){
    $t .= substr($val,0,1).strlen($val);
  }
  echo $t."\n";
 ?>

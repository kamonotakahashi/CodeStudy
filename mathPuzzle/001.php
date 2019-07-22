<?php

/*
プログラマ脳を鍛える
数学パズル　００１
必ず奇数になるので、インクリメントで１ずつ増やす必要なかった。
本来ならば、 $cnt+=2;とかでOK　そのほうが処理が N/2になるよね。

2019/7/23

*/

$in = trim(fgets(STDIN));
if(!(is_Numeric($in) && 11 <= $in ))exit();
$cnt = $in;
while(true){
  $b = c($cnt,2);
  $o = c($cnt,8);
  $d = c($cnt,10);
  if($b === r($b)){
    if($o === r($o)){
      if($d === r($d)) break;
    }
  }

  $cnt++;
}
echo $cnt ."\n";

//N base numeral
function c($n,$d,$f = ''){
  if(0 >= $n) return r($f);
  if($n%$d === 0) return c(floor($n/$d),$d,$f.'0');
  if($n%$d !== 0) return c(floor($n/$d),$d,$f.strval($n%$d));
}

//Reverse
function r($s){
  $str = '';
  if(is_string($s) && 1 <= strlen($s)){
    for($i = strlen($s); 0 < $i;$i--)$str .= $s[$i-1];
  }
  return $str;
}

?>

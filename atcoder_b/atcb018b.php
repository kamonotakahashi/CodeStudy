<?php
$c = null;
$S = trim(fgets(STDIN));
(1<=strlen($S)&&strlen($S)<=100) || exit();
$N = trim(fgets(STDIN));
(1<=$N&&$N<=100) || exit();

$num = $S;
for($i = 0;$i < $N;$i++){
  $c = explode(' ',trim(fgets(STDIN)));
  ((1<=$c[0]) && ($c[0] < $c[1]) && ($c[1] <= strlen($S))) || exit();
  $num = rev($num,$c);
}
echo $num ."\n";
function rev($num,$c){
  $x = function($num,$c){
    $t = "";
    for($i=$c[0]-1;$i<$c[1];$i++){
      $t .= $num[$i];
    }
    return $t;
  };
  $xx = $x($num,$c);
  $r = "";
  for($i = strlen($xx)-1;$i >= 0;$i--){
    $r .= $xx[$i];
  }
  return str_replace($xx,$r,$num);
}
?>

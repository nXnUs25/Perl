#! /usr/bin/perl -w
open (WF, "./gra/slowka.txt");
 @word_list=<WF>;
close (WF);
srand(time ^ $$);
$num = rand(@word_list);
$s=$word_list[$num];
$l=length($s);
print $s;
$o=1;
open(H, "<./gra/haslo.txt");
@p=<H>;
close H;

print $sl;
if($s eq $sl){
  print " zgadles";
}
$lit=<>;
chop($lit);
@char=split(//,$s);
for ($i=0; $i<$l; $i++){
  ($lit eq $char[$i])? $p[$i]=$lit.' ': $o++; 
}
for $_ (@p){
  chomp($_);
  print $_;
}

if($o==10){
  print 'przegrales';
}
open(H, ">./gra/haslo.txt");
for $w(@p){
  print H $w."\n";
}
close H;
print "\n";
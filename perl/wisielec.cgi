#! /usr/bin/perl
use CGI;
#=============================
open(S, "./gra/s.txt");
$s=<S>;
chomp($s);
close S;
$l=length($s);
$nowaGra="true";
$as=0;
open(H, "<./gra/haslo.txt");
@p=<H>;
close H;
open(O, "./gra/obrazek.txt");
$o= <O>;
close O;
#======================================
my $cgi = new CGI;
my $url = $cgi->script_name();
my @param = $cgi->param();

$wyraz=$cgi->param("odgadniete");
$lit=$cgi->param("l");
if( $lit eq "Sprawdz"){ 
  if( $wyraz eq $s){
    $info="Zgadles poprawnie slowo";
    $nowaGra="false";
    $cgi->param("odgadniete","")
    }else{
      $info="zle podane slowo";
      $o=11;
      $cgi->param("odgadniete","")
    }
}
#=======================================================
if($o==10){
  $info="Zawisles - nie udalo ci sie odgadnac slowa";
}
#========================================================
if($lit eq "Nowa Gra" || ($lit eq "")){
  if($lit =~ "Nowa Gra"){  
    open (WF, "./gra/slowka.txt");
    @word_list=<WF>;
    close (WF);
    srand(time ^ $$);
    $num = rand(@word_list);
    $s=$word_list[$num];
    chomp($s);
    $l=length($s);
    open(S, ">./gra/s.txt");
      print S $word_list[$num];
    close S;
  }
  open(O, ">./gra/obrazek.txt");
  print O 0;
  close O;
  $o=0;
  for($i=0; $i<$l; $i++){
    $p[$i]='_ ';
  } 
open(H, ">./gra/haslo.txt");
for ($i=0; $i<$l; $i++){
  print H $p[$i]."\n";
  }
close H;
}
open(B, "<./gra/b.txt");
  $nowehaslo=<B>;
close B;
#===================================
if($nowaGra eq "true"){
  if($o<11){
    @char=split(//,$s);
    for ($i=0; $i<$l; $i++){
      if($lit eq $char[$i]){
	$p[$i]=$lit.' ';
	$ii=$i;
	$as=1;
      }
    }
  if($as==0){
      if($lit eq $p[$ii]){    
      }else{
	$o++;
      }
  }
  for ($i=0; $i<$l; $i++){
    chomp($p[$i]);
    $print.=$p[$i];
  }
  open(H, ">./gra/haslo.txt");
  for ($i=0; $i<$l; $i++){
    print H $p[$i]."\n";
  }
  open(O, ">./gra/obrazek.txt");
  print O $o;
  close O;
  for $z (@p){
  chomp($z);
    $sl.=$z;
    if($sl=~ s/ //g){
    }
}

if($s eq $sl){
  $info="Gratuluje odgadles slowko";
  $nowaGra="false";
}
  }
}
#===========================================
print $cgi->header(-type=>'text/html',-charset=>'UTF-8'),
$cgi->start_html(-title => '--- WISIELEC ---'),
'<br>',

$cgi->div({-align => 'center'},$cgi->h1($cgi->font({-color=>'red'},'Wisielec'))),
$cgi->div({-align => 'center'}, $cgi->img({src => './gra/r'.$o.'.png', alt=>'brak obrazkow na serwerze', align=>'center'})),
$cgi->div({-align => 'center'},
$cgi->start_form(-method => 'POST', -action => './wisielec.cgi'),
$cgi->label($cgi->font({-color=>'blue', -size=> '12'},$print)), '<br>',
'<br>',
$cgi->submit(-name => 'l', -value => 'a'),
$cgi->submit(-name => 'l', -value => 'b'),
$cgi->submit(-name => 'l', -value => 'c'),
$cgi->submit(-name => 'l', -value => 'd'),
$cgi->submit(-name => 'l', -value => 'e'),
$cgi->submit(-name => 'l', -value => 'f'),
$cgi->submit(-name => 'l', -value => 'g'),
$cgi->submit(-name => 'l', -value => 'h'),
$cgi->submit(-name => 'l', -value => 'i'),
$cgi->submit(-name => 'l', -value => 'j'),
$cgi->submit(-name => 'l', -value => 'k'),
$cgi->submit(-name => 'l', -value => 'l'),
$cgi->submit(-name => 'l', -value => 'm'),
$cgi->submit(-name => 'l', -value => 'n'),
$cgi->submit(-name => 'l', -value => 'o'),
$cgi->submit(-name => 'l', -value => 'p'),
$cgi->submit(-name => 'l', -value => 'q'),
$cgi->submit(-name => 'l', -value => 'r'),
$cgi->submit(-name => 'l', -value => 's'),
$cgi->submit(-name => 'l', -value => 't'),
$cgi->submit(-name => 'l', -value => 'u'),
$cgi->submit(-name => 'l', -value => 'v'),
$cgi->submit(-name => 'l', -value => 'w'),
$cgi->submit(-name => 'l', -value => 'x'),
$cgi->submit(-name => 'l', -value => 'y'),
$cgi->submit(-name => 'l', -value => 'z'),'<br>','<br>',
$cgi->label('Slowo ?'),
$cgi->textfield(-name => 'odgadniete', -value=>'zgadnij slowo', -size => 20), 
$cgi->submit(-name=>'l', -value=>'Sprawdz'),'<br>',
'<br>',
$cgi->submit(-name=>'l', -value=>'Nowa Gra'),'<br>',
$cgi->label($cgi->font({-color=>'red'},$info)),
$cgi->end_form(),
),
$cgi->end_html;

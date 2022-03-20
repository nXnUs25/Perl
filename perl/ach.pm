package ach;
my $tpl;
sub readFile{
  open(TPL_FILE,'< /home/nonus25/public_html/cgi-bin/html.tpl');
  while(<TPL_FILE>){
    $tpl.=$_;
  }
  close(TPL_FILE);
}
sub picsPath{
   $homePath='./Ksiega_Gosci.cgi';
   $comentspath='./w.cgi';
   $logpath='./html.html';
   $tpl =~s/{homePath}/$homePath/g ;
   $tpl =~s/{comentspath}/$comentspath/g ;
   $tpl =~s/{logpath}/$logpath/g ;
}

sub dz{
	print $tpl;
}
1;

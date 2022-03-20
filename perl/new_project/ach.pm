package ach;
my $tpl;
#===============================================================================================================
sub readFile{
  open(TPL_FILE,'< /home/nonus25/public_html/cgi-bin/new_project/html.tpl');
  while(<TPL_FILE>){
    $tpl.=$_;
  }
  close(TPL_FILE);
}
#===============================================================================================================
sub picsPath{
	my $u=shift;
   $homePath=$u;
   $comentspath="?page=c";
   $logpath=$u.="?page=b";
   $style='./styl.css';	
   $tpl =~s/{homePath}/$homePath/g ;
   $tpl =~s/{comentspath}/$comentspath/g ;
   $tpl =~s/{logpath}/$logpath/g ;
   $tpl =~s/{style}/$style/g ;
}
#===============================================================================================================
sub dz{
	print $tpl;
}
#===============================================================================================================
sub tresc{
	my $cgi=shift;
	if($cgi->param('page') eq 'b'){
	  	&tresc1($cgi);
	 }elsif ($cgi->param('page') eq 'c'){
	  	&tresc2($cgi);	
    }else{
    	&tresc3($cgi);
    }
}
#===============================================================================================================
sub tresc1{
	$cgi=shift;
	my $tresc1 ='';
        	$tresc.=$cgi->start_form(-method => 'POST', -action => './kg.cgi'),
        	$tresc.='<br>',
        	$tresc.=$cgi->label($cgi->font({-color=>'red'},'&nbsp;LOG IN&nbsp;')),
        	$tresc.='<br>',
			$tresc.=$cgi->label('E-mail:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'),
			$tresc.=$cgi->textfield(-name => 'log', -size => 20),
			$tresc.='<br>',
			$tresc.=$cgi->label('Login:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'),
			$tresc.=$cgi->textfield(-name => 'log', -size => 20),
			$tresc.='<br>',
			$tresc.=$cgi->label('Password:&nbsp;&nbsp;'),
			$tresc.=$cgi->password_field(-type=>"password", -name => 'log', -size => 20, -maxlength=>"10"), 
			$tresc.='<br>',
			$tresc.=$cgi->submit(-name=>'l', -value=>'Save'),
			$tresc.='<br>',
			$tresc.=$cgi->reset(-name=>'l', -value=>'Clear'),
			$tresc.=$cgi->end_form(),
			$tpl =~s/{tresc}/$tresc/g ;
}
#===============================================================================================================
sub tresc2{
	$cgi=shift;
	my $tresc ='';
        	$tresc.=$cgi->start_form(-method => 'POST', -action => './kg.cgi'),
        	$tresc.=$cgi->label($cgi->font({-color=>'red'},'&nbsp;LOG IN&nbsp;')),
        	$tresc.='<br>',
			$tresc.=$cgi->label('E-mail:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'),
			$tresc.=$cgi->textfield(-name => 'log', -size => 20),
			$tresc.='<br>',
			$tresc.=$cgi->label('adas:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;'),
			$tresc.=$cgi->textfield(-name => 'log', -size => 20),
			$tresc.='<br>',
			$tresc.=$cgi->label('Password:&nbsp;&nbsp;'),		 
			$tresc.='<br>',
			$tresc.=$cgi->submit(-name=>'l', -value=>'Save'),
			$tresc.='<br>',
			$tresc.=$cgi->reset(-name=>'l', -value=>'Clear'),
			$tresc.=$cgi->end_form(),
			$tpl =~s/{tresc}/$tresc/g ;
}
#===============================================================================================================
sub tresc3{
	$cgi=shift;
	$tresc.="w3",
         $tpl =~s/{tresc}/$tresc/g ;
}
#===============================================================================================================
1;

#! /usr/bin/perl
use CGI;
my $cgi = new CGI;
my $url = $cgi->script_name();
my @param = $cgi->param();
#<link rel="stylesheet" type="text/css" href="styl.css">
print $cgi->header(-type=>'text/html',-charset=>'UTF-8'),
$cgi->start_html(-title => '--Sample Guest Book--'),
	$cgi->div({-align => 'center'}, 
		$cgi->img({src => './ksiega/logo.jpg', alt=>'brak obrazkow na serwerze', align=>'center'})
	),	
	$cgi->div({-align=>'center'},
		$cgi->a({-href=>$url}, '&nbsp;'."Home page".'&nbsp;'),
		$cgi->a({-href=>'./opinija.cgi'}, '&nbsp;'."Add a comment".'&nbsp;'),
		$cgi->a({-href=>'./logowanie.cgi'}, '&nbsp;'."Log In".'&nbsp;')
	),
$cgi->end_html;

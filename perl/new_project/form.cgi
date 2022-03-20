#! /usr/bin/perl
use lib '/home/nonus25/public_html/cgi-bin/new_project/';
use ach;
use CGI;
my $cgi = new CGI;
my $url = $cgi->script_name();
my @param = $cgi->param();
print $cgi->header(-type=>'text/html',-charset=>'UTF-8'),
$cgi->start_html(-title => '--- WISIELEC ---'),
'<br>',
$cgi->div({-align => 'center'},$cgi->h1($cgi->font({-color=>'red'},'Add a coment'))),
$cgi->div({-align => 'center'},
$cgi->start_form(-method => 'POST', -action => './wisielec.cgi'),'<br>',
$cgi->label('Slowo ?'),
$cgi->textfield(-name => 'odgadniete', -value=>'zgadnij slowo', -size => 20), 
$cgi->submit(-name=>'l', -value=>'Sprawdz'),'<br>',
'<br>',
$cgi->submit(-name=>'l', -value=>'Nowa Gra'),'<br>',
$cgi->label($cgi->font({-color=>'red'},$info)),
$cgi->end_form(),
),
$cgi->end_html;
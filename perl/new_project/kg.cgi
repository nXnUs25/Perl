#! /usr/bin/perl
use lib '/home/nonus25/public_html/cgi-bin/new_project/';
use ach;
use CGI;
my $cgi = new CGI;
my $url = $cgi->script_name();
my @param = $cgi->param();
print "Content-type: text/html\n\n";

&generateHTML;

sub generateHTML{
  ach::readFile;
  ach::picsPath($url);
  ach::tresc($cgi);
  ach::dz;
}
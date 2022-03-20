#!/usr/bin/perl -w ./home/nonus25/public_html/cgi-bin/strict.cgi
print "Content-type: text/plain\n\n";
use strict;
use CGI qw( :standard );
my $nazwa = param( "student" );
print header( "text/html" ),
start_html( "Witamy" ),
p( "Witaj, $nazwa!" ),
end html;


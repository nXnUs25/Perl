#!/usr/bin/perl -w 
use CGI;
#print "Content-type: text/html\n\n";
my $cgi = new CGI;
my @param = $cgi->param();
print $cgi->header(-type=>'text/html', -charset=>'UTF-8');
print $cgi->start_html (-title => "Tytuł mojej & strony");
print $cgi->h1 ("Nagłówek mojej strony &&& ///");
$napis = " to jest napis: a <=b ?";
print $cgi->p ($napis);
print $cgi->p ("@param");
foreach my $nazwa ($cgi->param())
{
    print "$nazwa: ";
    print $cgi->param ($nazwa);
    print "<BR>";
  }
print $cgi->end_html();


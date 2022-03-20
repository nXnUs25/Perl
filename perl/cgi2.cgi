#! /usr/bin/perl
use CGI;
my $cgi = new CGI;
my $url = $cgi->script_name();
print $cgi->header(-type=>'text/html',-charset=>'UTF-8');
if ($cgi->param("page") ne "b")
    {
        $url .= "?page=b";
        print $cgi->start_html (-title => "STRONA AAA",
                           -bgcolor=>"#cccccc"),
              $cgi->p("Oto strona AAA \n",
                      "Aby wybrać stronę B,");
                   print $cgi->param("page"),
              $cgi->a({-href=>$url}, "kliknij tutaj");
    }
    else
    {
        print $cgi->start_html (-title => "STRONA BBB",
                           -bgcolor=>"#bbbccc"),
              $cgi->p("Oto strona BBB \n",
                      "Aby wybrać stronę A,"),
                      print $cgi->param("page"),
              $cgi->a({-href=>$url}, "kliknij tutaj");
      }
print $cgi->end_html;

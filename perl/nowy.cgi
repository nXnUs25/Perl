#! /usr/bin/perl
use CGI;
my $cgi = new CGI;
my $datownik = localtime;
print $cgi->header(-type=>'text/html',-charset=>'UTF-8'),
      $cgi->start_html (-title => "Datownik",-bgcolor=>"#aaaaaa"),
      $cgi->h2("Bieżący czas"),
      $cgi->hr,
      $cgi->p("Bieżący czas w tym systemie: ",$cgi->b($datownik)),
$cgi->p("nazwa serwera:",
        $cgi->server_name),
$cgi->p("nazwa serwera:",
        $cgi->em($cgi->server_name)),
$cgi->ol($cgi->li(["jeden", "dwa", "trzy"])),
$cgi->table({-border=>1,
             -width=>"100%"},
             $cgi->Tr([$cgi->th({-bgcolor=>"#cccccc"},["imię","wiek"]),$cgi->td(["marysia",29]),
                        $cgi->td(["janek",27]),
                        $cgi->td(["anonim",30])
                        ])
             ),
$cgi->start_form(-method=>"get",-action=>"nowy.cgi"),
$cgi->textfield(-name=>'nazwa',
                 -default=>'wpisz nazwisko',
                 -size=>50,
                 -maxlength=>80),
$cgi->submit(-name=>"klawisz",
             -value=>"nacisnieto"),
$cgi->checkbox(-name=>"czek",
                -checked=>"checked",
                -value=>"ON",
                -label=>"zaznacz mnie"),
$cgi->end_form(),
$cgi->end_html();


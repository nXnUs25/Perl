#! /usr/bin/perl -w

use CGI;
$cgi = new CGI;
my @param = $cgi->param();

# tworzenie słownika
%slownik = ('samochod' => 'jezdzi i ma cztery kola',
'kolysanka' => 'spiewana na dobranoc',
'pinokio' => 'drewniany chlopiec z dlugim nosem',
'trabka' => 'blaszany instrument dety',
'pies' => 'szczekajacy pupil');
# tablica słów do odgadnięcia
$licznik = 0;

# nagłówek strony html
print $cgi->header(-type => 'text/html', -charset => 'iso-8859-2'),
$cgi->start_html(-title => '-- WISIELEC --', -bgcolor => '#fff000', -onLoad => "document.forms[0].odgadniete_slowo.select()"),

# warstwa pierwsza (wyśrodkowanie)
$cgi->div({-align => 'center'}, $cgi->h1("Wisielec"));

($cgi->param('nowa_gra')) ? (++$licznik, "document.forms[0].odgadniete_slowo.") : ();
@slowa = keys(%slownik);
$slowo = $slowa[$licznik];
$opis = $slownik{$slowo};

# warstwa druga - formularz
print $cgi->div({-align => 'center'},
$cgi->start_form(-method => 'POST', -action => '/cgi-bin/test.cgi'),
$cgi->label("Podpowiedz: $opis"), '<br>',
$cgi->textfield(-name => 'odgadniete_slowo', -size => 50), '<br>',
$cgi->submit(-name => 'wyslij', -value => 'Sprawdz'),
$cgi->submit(-name => 'nowa_gra', -value => 'Nowa gra'),
$cgi->end_form(),
); # koniec formularza

# sprawdzenie odpowiedzi
print $cgi->div({-align => 'center'},
($cgi->param('odgadniete_slowo') eq $slowo) ? 'HURA!!!' : ($cgi->param('odgadniete_slowo') eq '') ? '' : 'ZLE...');

foreach $zmienna($cgi->param()){
print "$zmienna: " . $cgi->param($zmienna) . "<br>";
}

print $cgi->end_html; # koniec dokumentu html

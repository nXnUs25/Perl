#! /usr/bin/perl
#use strict;
#use warnings;
use CGI;

my $cgi = new CGI;
print $cgi->header("text/plain");
print $cgi->start_html (-title => "test");
print "<DIV ALIGN=CENTER>";
print $cgi->h1(Wisielec );
print "</DIV>";

my @Slowa  = ('yellow','green','blue');  # S³owa do odgadniêcia
my @wyraz =();    #Tablica przetrzymujaca podzielone s³owo
my $ilosc = 0;    #
my $krok ;        #
my $tak = 0;
my $nowa_gra = 0;  # Zmienna do inforamacji o nowej grze


my $numer_slowa = $cgi->param('numer_slowa'); # pozycja w tablicy
my $odgad .= $cgi->param('odgad');
my $haslo_zgad = $cgi->param('haslo_zgad');
my $krok = $cgi->param('krok');
my $button = $cgi->param('button');

$odgad .= $cgi->param('button');

if ($cgi->param('numer_slowa') )  # Je¿eli numer_s³owa zawiera wartoœæ
{
  @wyraz = split(//,$Slowa[$numer_slowa-1]);  # Podziel slowo na czêœci i zapisz do tablicy
}
else
{
	$numer_slowa = 1; # Jezeli nie bylo wartoœci w numer_slowa, to wpisz 1
	$krok = -1;  # Ustaw krok na pocz¹tek
  @wyraz = split(//,$Slowa[$numer_slowa-1]);
}

foreach $z ( @wyraz ){   # Szukamy czy wcisniêty przycisk jest w hasle
  if ( $button =~ /$z/i  ){
     $tak = 1  ;     # Zazancz, ¿e przycisk jest w hasle
  }
}

print "<DIV ALIGN=CENTER>";
foreach my $n (@wyraz) {  #
	if ( $odgad =~ /$n/i )  # Je¿eli wartoœæ zmiennej $n zawiera siê wcisnietych przyciskach
  {
    print $n;
    $odgad .= $n;  # Wypisz zmienn¹ odgadniêt¹ do tej pory
  }
  else
  {
    	 print " _ ";  # Jezeli jej nie ma wypisz "_"
       $ilosc = 1;   # Zaznacz, czy by³y jakieœ nieodgadniête wyrazy
   }
}
print "</DIV>";

if ( $ilosc == 0 ) # Je¿eli has³o siê zgadza, to zapisz has³o do zmiennej haslo_zgad
{
  foreach my $n (@wyraz) {
        $haslo_zgad .= $n;
   }
}

print "<br><br>";
print "<DIV ALIGN=CENTER><FONT SIZE=+2 COLOR=\"#ff3333\">";
if ( $haslo_zgad eq 'yellow' )    # Je¿eli odgdniête has³o jest yellow
{
  	$numer_slowa++;    # Przejdz do nastêpnego s³owa
    $odgad = '';       # Wykasuj odgadniête
    $haslo_zgad = '';  # Wykasuj  odgadniête ha³o
    $krok = -1;        # Ustawa na pocz¹tkowy krok
    $nowa_gra = 1;     # Zaznaczenie, ¿e jest to nowa gra
    print "Udalo Ci sie, bravo!!!</FONT><BR>";
}
else
{
	if ( $haslo_zgad eq 'green' )
  {
        $numer_slowa++;
      	$odgad = '';
        $haslo_zgad = '';
        $krok = -1;
        $nowa_gra = 1;
        print "Udalo Ci sie, bravo!!!</FONT><BR>";
  }
  else
  {
		if ( $haslo_zgad eq 'blue' )
		{
       	$numer_slowa++;
      	$odgad = '';
        $haslo_zgad = '';
        $krok = -1;
        $nowa_gra = 1;
        print "Udalo Ci sie, bravo!!!</FONT><BR>";
     }

    else
    {
      if( $tak == 0)  # Je¿lie nie uda³o siê zgadn¹æ
      {
          $krok++ ; # Zwiêksz, krok aby wyœwietliæ nastêpne zdjêcie
 	    }
    }
  }
}

print "</DIV>";

print "<DIV ALIGN=CENTER><FONT SIZE=+2 COLOR=\"#ff3333\">";


print $cgi->start_form(-name=>"form1", -method=>"get", -action=>"./cgi-bin/wisielec2.cgi");

if ($numer_slowa == 4 ){   # Je¿eli nie ma ju¿ wiecej s³ów do odgadniêcia
     print "<img src=\"","/gfx/","hang.gif\" height=150 width=150 alt=\"\"><BR>";
     print "To jest koniec <BR>";
     print " Gratulaje !!! </FONT><BR>";
}
else
{
  if ( $krok < 6 )  # Je¿eli krok jest mniejszy od 6, to wypisz wszystkie buttony
  {
	 print "<br>";
	 print "<img src=\"","/gfx/","hang",$krok,".gif\" height=150 width=150 alt=\"\"><BR>";
	 print "<br><br>";

    if( !( $odgad =~ /A/ ) ){ print $cgi->submit(-name=>"button", -value=>"A");}
    if( !( $odgad =~ /B/ ) ){ print $cgi->submit(-name=>"button", -value=>"B");}
    if( !( $odgad =~ /C/ ) ){ print $cgi->submit(-name=>"button", -value=>"C");}
    if( !( $odgad =~ /D/ ) ){ print $cgi->submit(-name=>"button", -value=>"D");}
    if( !( $odgad =~ /E/ ) ){ print $cgi->submit(-name=>"button", -value=>"E");}
    if( !( $odgad =~ /F/ ) ){ print $cgi->submit(-name=>"button", -value=>"F");}
    if( !( $odgad =~ /G/ ) ){ print $cgi->submit(-name=>"button", -value=>"G");}
    if( !( $odgad =~ /H/ ) ){ print $cgi->submit(-name=>"button", -value=>"H");}
    if( !( $odgad =~ /I/ ) ){ print $cgi->submit(-name=>"button", -value=>"I");}
    if( !( $odgad =~ /J/ ) ){ print $cgi->submit(-name=>"button", -value=>"J");}
    if( !( $odgad =~ /K/ ) ){ print $cgi->submit(-name=>"button", -value=>"K");}
    if( !( $odgad =~ /L/ ) ){ print $cgi->submit(-name=>"button", -value=>"L");}
    if( !( $odgad =~ /M/ ) ){ print $cgi->submit(-name=>"button", -value=>"M");}
    if( !( $odgad =~ /N/ ) ){ print $cgi->submit(-name=>"button", -value=>"N");}
    if( !( $odgad =~ /O/ ) ){ print $cgi->submit(-name=>"button", -value=>"O");}
    if( !( $odgad =~ /P/ ) ){ print $cgi->submit(-name=>"button", -value=>"P");}
    if( !( $odgad =~ /Q/ ) ){ print $cgi->submit(-name=>"button", -value=>"Q");}
    if( !( $odgad =~ /R/ ) ){ print $cgi->submit(-name=>"button", -value=>"R");}
    if( !( $odgad =~ /S/ ) ){ print $cgi->submit(-name=>"button", -value=>"S");}
    if( !( $odgad =~ /T/ ) ){ print $cgi->submit(-name=>"button", -value=>"T");}
    if( !( $odgad =~ /U/ ) ){ print $cgi->submit(-name=>"button", -value=>"U");}
    if( !( $odgad =~ /V/ ) ){ print $cgi->submit(-name=>"button", -value=>"V");}
    if( !( $odgad =~ /W/ ) ){ print $cgi->submit(-name=>"button", -value=>"W");}
    if( !( $odgad =~ /X/ ) ){ print $cgi->submit(-name=>"button", -value=>"X");}
    if( !( $odgad =~ /Y/ ) ){ print $cgi->submit(-name=>"button", -value=>"Y");}
    if( !( $odgad =~ /Z/ ) ){ print $cgi->submit(-name=>"button", -value=>"Z");}
    print "<br><br>";
    print "<INPUT type=\"hidden\" name=\"numer_slowa\" value=\"$numer_slowa\">";
    print "<INPUT type=\"hidden\" name=\"odgad\" value=\"$odgad\">";
  	print "<INPUT type=\"hidden\" name=\"haslo_zgad\" value=\"$haslo_zgad\">";
    print "<INPUT type=\"hidden\" name=\"krok\" value=\"$krok\">";
    if ( $nowa_gra == 1 ){         # Je¿eli odagniête to daj nowy przycisk nowa gra
      $numer_slowa++;
      print "<INPUT type=\"submit\" name=\"\" value=\"nowa slowo\">";
      
    }
  }
  else
  {
     if ( $krok == 6 )    # Je¿lie nie uda³o siê odagdn¹æ, to wypisz bez buttonów
      {
        print "<img src=\"","/gfx/","hang",$krok,".gif\" height=150 width=150 alt=\"\"><BR>";
        print "<br>";
        print "Nie udalo Ci sie, Sprobuj jeszcze raz </FONT><BR>";
        print "<br>";
        print "<INPUT type=\"submit\" name=\"\" value=\"nowa slowo\">";
     }
  }
}
print $cgi->end_form();
print "</DIV>";

print $cgi->end_html();


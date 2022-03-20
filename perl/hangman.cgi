#! /usr/bin/perl
use CGI; 
$DATAFILE = "slowa.txt"; 
$CLUE=1;
$bgcolour="silver";
$textcolour="#000010";
$linkcolour="blue";
$vlinkcolour="#FF00FF";
$alinkcolour="#FFFF00";
&cgi_receive;
if ($FINPUT{'word'}) {
&p_head;
$type = $FINPUT{'clue'};
$FINPUT{'word'} =~ y/a-x,y,z/c-z,a,b/;        
if ($FINPUT{'done'} eq 'done')          
{ if ($FINPUT{'word'} eq $FINPUT{'new'})  
{
print "<DIV ALIGN=CENTER><FONT SIZE=+4 COLOR=\"#ff3333\">";
print "Wygrales!!!</FONT><BR>";
print "<img src=\"","gfx/","hangw.gif\" height=150 width=150 alt=\"\"><BR>";
}
else {
print "<DIV ALIGN=CENTER><FONT SIZE=+4 COLOR=\"#cc6633\">";
print "Pomyliles sie!</FONT><BR>";
print "<img src=\"","gfx/","hang6.gif\ height=150 width=150 alt=\"\n O \n \\\|/\n \| \n/ \\\"><BR>";                
print "To jest <B>",$FINPUT{'word'},".</B>";
}
print "</DIV></BODY></HTML>\n";
exit;
return;
}
chop($FINPUT{'st'});         
$FINPUT{'st'} =~ s/\s//g;                 
$FINPUT{'st'} =~ s/^(.)(.*)/$1/;       
$guess = $FINPUT{'st'}.' '.$FINPUT{'guess'};
$guess =~ y/A-Z/a-z/;                  
@sofar = split(/\s+/,$guess);            
$gue = @sofar;                         
$num = length($FINPUT{'word'});
@rword = split(/ */,$FINPUT{'word'}); 
print "<DIV ALIGN=CENTER><FONT SIZE=+3 color=\"#336699\">";
$gotten = 0;
$TEST = "";
LET: for ($i=0;$i<$num;$i++) {      
$temp = $rword[$i];
for ($g=0;$g<$gue;$g++) { 
if ($sofar[$g] eq $temp) { 
print $temp;
if ($TEST !~ /$temp/) {        
$gotten = $gotten +1;       
}
$TEST= "$TEST$temp";		
next LET;
}
}
print "_ ";                   
$TEST = "$TEST _";
}
print "</FONT></DIV><BR>";
if ($TEST eq $FINPUT{'word'}) {
print "<DIV ALIGN=CENTER><FONT SIZE=+3 COLOR=\"#ff3333\">";
print "Wygrales!!</FONT><BR>";
print "<img src=\"","gfx/","hangw.gif\"><BR>";
print "</BODY></HTML>";
exit;
}
print "<DIV ALIGN=CENTER>";
print "<img src=\"","gfx/","hang",($gue-$gotten),".gif\" height=150 width=150 alt=\"\"><BR>";
if (($gue-$gotten) < 6) {                  
$FINPUT{'word'} =~ y/a,b,c-z/y,z,a-y/;        
if ((6-($gue-$gotten)) == 1) {          
print "Pozostala Ci jedna szansa!";    
}
else {
print "Masz jeszcze ",(6-($gue-$gotten))," szans!";
}
if ($CLUE==1){
print "<BR><font color=\"#0033ff\">Kategoria : <B>$type</B></FONT>";
}
print "</DIV><P><DIV ALIGN=CENTER>"; 
print "\n<form method=\"post\" action=\"",$CGI_BIN,"\">";
print "<INPUT type=\"hidden\" name=\"guess\" value=\"$guess\">";
print "<INPUT type=\"hidden\" name=\"word\" value=\"$FINPUT{'word'}\">";
if ($CLUE == 1){
print "<input type=\"hidden\" name=\"clue\" value=\"$type\">";   
}
&buttons;
print "</form>\n";
print "<form method=\"post\" action=\"",$CGI_BIN,"\">";
print "<INPUT name=\"new\" size=12> &nbsp; "; 
print "<input type=\"hidden\" name=\"done\" value=\"done\">"; 
print "<input type=\"hidden\" name=\"word\" value=\"$FINPUT{'word'}\">";
print "<input type=\"submit\" value=\"Zgadnij!\">\n";
print "</form> </DIV></BODY></html>\n";
}
else{                                      
print "<DIV ALIGN=CENTER><FONT SIZE=+3 COLOR=\"#ff3333\">";
print "Gra skonczona!</FONT><BR><FONT SIZE=+2 COLOR=\"#3333cc\">";
print "Wlasciwa odpowiedz to <B>$FINPUT{'word'}</B>.</FONT><BR>";
print "</BODY></HTML>";
exit;
}
}
else {
&p_head;
open (WF, $DATAFILE) || die "plik nie znaleziony";
@word_list=<WF>;
close (WF);
srand(time ^ $$);$num = rand(@word_list); 
($word, $type) = split(/,/, $word_list[$num]);
print "<DIV ALIGN=CENTER><FONT SIZE=+3 color=\"#336699\">";
$num = length($word);
for ($i=1;$i<=$num;$i++)
{ print '_ ';	  
}
$word =~ y/a,b,c-z/y,z,a-y/;                  
print "</FONT></DIV>\n<p><DIV ALIGN=CENTER>";
print "<img src=\"","gfx/","hang0.gif\" height=150 width=150 alt=\"\"><BR>";
print "Strzel pierwsza litere szukanego slowa!<BR>";
print "<font color=\"#0033ff\">Kategoria : <B>",$type,"</B></FONT>";
print "<form method=\"post\" action=\"",$CGI_BIN,"\">";
print "<input type=\"hidden\" name=\"guess\" value=\"\">";
if ($CLUE==1){
print "<input type=\"hidden\" name=\"clue\" value=\"$type\">";
}
print "<input type=\"hidden\" name=\"word\" value=\"$word\">";
&buttons;
print "</form>\n";
print "Jeœli jestes pewien, ze znasz odpowiedz wpisz ponizej<BR>";
print "<form method=\"post\" action=\"",$CGI_BIN,"\">";
print "<input name=\"new\" size=12> &nbsp; ";
print "<input type=\"hidden\" name=\"done\" value=\"done\">";
print "<input type=\"hidden\" name=\"word\" value=\"$word\">";
print "<input type=\"hidden\" name=\"clue\" value=\"$type\">";
print "<input type=\"submit\" value=\"Zgadnij!\">\n";
print "</form> </html>\n";
}
sub p_head {
print "Content-type: text/html\n\n";
print "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0 Draft//EN\">";
print "<HTML>\n";
print "<HEAD><title>Interaktywna gra „Wisielec” w technologii CGI </title></HEAD>\n";
print "<BODY bgcolor=\"$bgcolour\" ";
if ($BG==1){ 
print "background=\"$BGGIF\" ";
}
print "text=\"$textcolour\" link=\"$linkcolour\" "; 
print "vlink=\"$vlinkcolour\" link=\"$alinkcolour\">";
print "<DIV ALIGN=CENTER><H1><font color=red>Wisielec</font></H1></DIV>\n";
}
sub buttons {
print "<BR>";
if ($guess !~ /a/) { print "<input type=\"submit\" name=\"st\" value=\" A \">";}
if ($guess !~ /b/) { print "<input type=\"submit\" name=\"st\" value=\" B \">";}
if ($guess !~ /c/) { print "<input type=\"submit\" name=\"st\" value=\" C \">";}
if ($guess !~ /d/) { print "<input type=\"submit\" name=\"st\" value=\" D \">";}
if ($guess !~ /e/) { print "<input type=\"submit\" name=\"st\" value=\" E \">";}
if ($guess !~ /f/) { print "<input type=\"submit\" name=\"st\" value=\" F \">";}
if ($guess !~ /g/) { print "<input type=\"submit\" name=\"st\" value=\" G \">";}
if ($guess !~ /h/) { print "<input type=\"submit\" name=\"st\" value=\" H \">";}
if ($guess !~ /i/) { print "<input type=\"submit\" name=\"st\" value=\" I \">";}
if ($guess !~ /j/) { print "<input type=\"submit\" name=\"st\" value=\" J \">";}
if ($guess !~ /k/) { print "<input type=\"submit\" name=\"st\" value=\" K \">";}
if ($guess !~ /l/) { print "<input type=\"submit\" name=\"st\" value=\" L \">";}
if ($guess !~ /m/) { print "<input type=\"submit\" name=\"st\" value=\" M \">";}
if ($guess !~ /n/) { print "<input type=\"submit\" name=\"st\" value=\" N \">";}
if ($guess !~ /o/) { print "<input type=\"submit\" name=\"st\" value=\" O \">";}
if ($guess !~ /p/) { print "<input type=\"submit\" name=\"st\" value=\" P \">";}
if ($guess !~ /q/) { print "<input type=\"submit\" name=\"st\" value=\" Q \">";}
if ($guess !~ /r/) { print "<input type=\"submit\" name=\"st\" value=\" R \">";}
if ($guess !~ /s/) { print "<input type=\"submit\" name=\"st\" value=\" S \">";}
if ($guess !~ /t/) { print "<input type=\"submit\" name=\"st\" value=\" T \">";}
if ($guess !~ /u/) { print "<input type=\"submit\" name=\"st\" value=\" U \">";}
if ($guess !~ /v/) { print "<input type=\"submit\" name=\"st\" value=\" V \">";}
if ($guess !~ /w/) { print "<input type=\"submit\" name=\"st\" value=\" W \">";}
if ($guess !~ /x/) { print "<input type=\"submit\" name=\"st\" value=\" X \">";}
if ($guess !~ /y/) { print "<input type=\"submit\" name=\"st\" value=\" Y \">";}
if ($guess !~ /z/) { print "<input type=\"submit\" name=\"st\" value=\" Z \">";}    
}
sub cgi_receive {
if ($ENV{'REQUEST_METHOD'} eq "POST") {
read(STDIN, $incoming, $ENV{'CONTENT_LENGTH'});
}
else {
$incoming = $ENV{'QUERY_STRING'};  
}
@pairs = split(/&/, $incoming);
foreach (@pairs) {
($name, $value) = split(/=/, $_);
$name  =~ tr/+/ /;
$value =~ tr/+/ /;
$name  =~ s/%([A-F0-9][A-F0-9])/pack("C", hex($1))/gie;
$value =~ s/%([A-F0-9][A-F0-9])/pack("C", hex($1))/gie;
$value =~ s/;/$$/g;                   
$value =~ s/&(\S{1,6})$$/&\1;/g;
$value =~ s/$$/ /g;
$value =~ s/\|/ /g;
next if ($value eq "");
if ($name =~ /^assign-dynamic/) {
$name = $value;
$value = "on";
}
$FINPUT{$name} .= ", " if ($FINPUT{$name});
$FINPUT{$name} .= $value;
}
}

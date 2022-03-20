#!/usr/bin/perl
     use CGI;
     CGI::ReadParse(*form);

     @files=`grep -li "$form{'slowo'}" *.html`;

     print "Content-type: text/html; charset=ISO-8859-2\n\n";
     print "<html><head><title>Wyniki wyszukiwania</title>\n";
     print "</head><body><h1>Wyniki wyszukiwania</h1>\n";
     if ($#files == -1) {
        print "Nie znaleziono żadnego pliku zawierającego tekst <b>",
               $form{'slowo'},"</b>\n";
     } else {
        print "Znaleziono ",$#files+1," plików zawierających tekst <b>",
               $form{'slowo'},"</b><p>\n";
        print "<ul>\n";
        foreach $file (@files) {
           chop($file);
           print '<li><a href="',$file,'">',$file,"</a>\n";
        }
        print "</ul>\n";
     }
     print "</body></html>\n";

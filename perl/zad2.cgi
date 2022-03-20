#!/usr/bin/perl -w

print "Content-type: text/plain\n\n";
print "Przygotowal Augustyn Chmiel\nZadania dla modulu 2\n\n";
print "Zadanie 1\n";
@l=6..16;
for $x (@l,){
	if($x%2==0){
		print $x."\n";
	}
}
print "\n";
for($i=6; $i<=16; ++$i){
	unless($i%2!=0){
		print $i."\n";
	}
}

print "\nZadanie 2\n";
@od= reverse @l;
for $x (@od){
	if($x%2==0){
		print $x." ";
	}
}
print "\n";
for($i=16; $i>=6; --$i){
	unless($i%2!=0){
		print $i." ";
	}
}

#print "\nZadanie 3\n";
#print "Zgadnij liczbe od 1 do 10: \n";
#$a=int(rand(10))+1;
#$b=0;
#until($a==$b){
#print "Podaj liczbe: ";
#$b= <>;#mozna <> i tak <STDIN>
#chop($b);
#$($b>$a)? print "za duzo\n" : ($b<$a) ? print "za malo\n": print"brawo\n";
#}
print"\n";
$i='adas Chmiel';
$a=length($i);
print $a."\n";





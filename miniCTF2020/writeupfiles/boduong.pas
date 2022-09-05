program whosyourdaddy;
uses crt;

var
        name: string;
        daddy: string ='ISP';
        flag: string = 'hrqbmtczqsnfs`llhofC`rhb|';

procedure printFlag(var flag: string);
var i: integer;

BEGIN
        for i := 1 to length(flag) do
                flag[i] := chr(ord(flag[i]) xor 1);
        writeln(flag);
END;


BEGIN
        writeln('Who''s your daddy?');
        readln(name);
        if name = daddy then printFlag(flag)
        else
                BEGIN
                        writeln('Neu ma ngoan em se bi thuong.');
                        writeln('Neu ma hu em se duoc phat.');
                END;
        readln()
END.

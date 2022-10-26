#include <stdio.h>
#include <unistd.h>
#include <string.h>

int main(){
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    setbuf(stderr,NULL);
    puts("      NETCAT      ");
    puts("    /\\_____/\\    ");
    puts("   /  o   o  \\   ");
    puts("  ( ==  ^  == )   ");
    puts("  ))         (    ");
    puts("  (           )   ");
    puts(" ( (  )   (  ) )  ");
    puts("(__(__)___(__)__) ");
    char flag[] = "ISPCTF{Th1s_1s_n3t_c4t}";
    int i=0;
	puts("\nHere your flag: ");
	while (i<strlen(flag)){
		sleep(1);
		printf("%c",flag[i]);
		i++;
	}
    return 0;
}
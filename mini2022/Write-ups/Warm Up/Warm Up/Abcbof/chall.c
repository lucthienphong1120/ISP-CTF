#include <stdio.h>
#include <math.h>
#include <string.h>
#include <unistd.h>
#include <stdlib.h>
#include <time.h>


void isp();
void huongDan();
void flag();
int main(){   
    long long money = 0;
    puts("==========================Game Bài Đoán Số Uy Tín Đổi Thưởng==========================");
    puts("| 1. Chơi Game   |  2. Hướng Dẫn   |   3. Đổi Flag   |  4. Thoát Game |  5. Tài Khoản |");
    puts("======================================================================================");
    puts("Hãy nhập tên người chơi:");
    char name[30];
    gets(name);
    system("clear");
TieuDe:
    isp();
    puts("==========================Game Bài Đoán Số Uy Tín Đổi Thưởng==========================");
    puts("| 1. Chơi Game   |  2. Hướng Dẫn   |   3. Đổi Flag   |  4. Tài Khoản | 5. Thoát Game |");
    puts("======================================================================================");
    puts("");
    printf("Hello %s, chào mừng bạn đến với Game Bài Uy Tín Top 1 Việt Nam !!!\n", name);
    int x;
    puts("Nhập lựa chọn của bạn:");
    scanf("%d", &x);
    fflush(stdin);
    switch(x){
        case 1:
            printf("\nTài khoản của bạn có %lld $\n", money);
            printf("Hello %s chào mừng bạn đến với cuộc chơi sống còn\n", name);
            srand(time(NULL));
            puts("Hãy nhập lá bài mà bạn đoán");
            int card;
            scanf("%d", &card);
            int ran = rand() %  9 + 2;
            if(ran == card){
                money += 50000;
                puts("Chúc mừng bạn đã kiếm được 50 000 $");
                printf("\nQuay trở lại sau %d giây\n", ran);
                puts("Vui lòng đợi trong giây lát");
                sleep(ran);
                system("clear");
                goto TieuDe;
            }
            else{
                puts("Bạn đã đoán sai, vui lòng thử lại sau");
                sleep(1);
                system("clear");
                goto TieuDe;
            }
                   
        case 2:
            huongDan();
            puts("");
            puts("Quay trở lại sau 10 giây");
            sleep(10);
            system("clear");
            goto TieuDe;
        
        case 3:
            printf("\nTài khoản của bạn có %lld $ \n", money);
            puts("=====================FLAG=======================");
            puts("|Bạn có muốn mua FLAG với giá 1 000 000 000 $  |");
            puts("|----------------------------------------------|");
            puts("|         1. YES      |         2. NO          |");
            puts("================================================");
            int x;
            puts("Lựa chọn của bạn : ");
            scanf("%d", &x);
            if(x == 1){
                if(money >= 1000000000){
                    printf("\n\nChúc mừng bạn đã chiến thắng\n");
                    puts("Đây là Flag của bạn:");
                    flag();
                    return 0;
                }
                else{
                    puts("Bạn không đủ tiền hãy đoán bài để kiếm thêm");
                    sleep(2);
                    system("clear");
                  goto TieuDe;
                }
            }
            else{
                puts("Bạn đã nhập sai cú pháp, vui lòng thử lại sau");
                sleep(2);
                system("clear");
                goto TieuDe;
            }
        case 5:
            puts("Tạm biệt bạn, hẹn gặp lại lần sau");
            puts("       From ISP with love <3     ");
            return 0;
    
        case 4:
            printf("\nTài khoản của bạn có %lld $ \n", money);
            puts("Quay trở lại sau 3 giây");
            sleep(3);
            system("clear");
            goto TieuDe;

        default:
            puts("Bạn đã nhập sai vui lòng nhập lại sau 3 giây");
            sleep(3);
            system("clear");
            goto TieuDe;     
    }
    return 0;
}

void huongDan(){
    system("clear");
    puts("==============Hướng Dẫn==============");
    puts("  Chiến thắng để dành giải thưởng   ");
    puts("      1 triệu $ từ Halston <3       ");
    puts("                                    ");
    puts(" Mỗi lần nhập hãy nhập vào một lá   ");
    puts("  mà giống với lá bài của nhà cái   ");
    puts("  Bộ bài chỉ gồm 9 lá từ 2 đến 10    ");
    puts(" Do lợi nhuận cao nên mọi người đến ");
    puts(" chơi bài rất nhiều dẫn đến khi đi  ");
    puts(" về họ cầm theo cả Át, J, Q, K để   ");
    puts(" đi về. Mỗi lần đoán đúng sẽ được   ");
    puts("             50 000$                ");
    puts("                                    ");
    puts("               Hint                 ");
    puts("  Hãy cố gắng nhập THẬT NHIỀU để    ");
    puts("      có thể chiến thắng nhé.       ");
    puts("                     Kevin Halston  ");
    puts("=====================================");
}

void flag(){
    FILE * fp = NULL;
    fp = fopen("flag.txt", "r");

    char c;
    while ((c = fgetc(fp)) != EOF)
        printf("%c", c);
    fclose(fp);
}


void isp(){
    puts("                                                                                ");
    puts("                                                                                ");
    puts("                                                                                ");
    puts("                                         I                                      ");
    puts("                                      II   II                                   ");
    puts("                                   II         II                                ");
    puts("                                ,I               II                             ");
    puts("                              I,       IIIIII       II                          ");
    puts("                           II       IIIIIIIIIIII       II                       ");
    puts("                        II       IIIIIIIIIIIIIIIIII#      II                    ");
    puts("                     II        IIIIIIIIIIIIIIIIIIIIIII       II                 ");
    puts("                  II        IIIIIIIIIII       IIIIIIII  II      II              ");
    puts("           IIIIII            IIIIIII            IIIIII  IIIII      II           ");
    puts("           IIIII        II    IIIIIII           IIIIII  IIIIIIII      II.       ");
    puts("            #I      I   IIII    IIIIIII         IIIIII  IIIIIIIIIII     I       ");
    puts("                 IIIII  IIIII    IIIIIIIII     .IIIIII  IIII   IIIII    I       ");
    puts("        IIIII  IIIIIII   IIIIII    IIIIIIIII     IIIII  IIII    IIII    I       ");
    puts("        IIIII  #IIIIII   IIIIII       IIIIIIIII      I  IIII   IIII    I        ");
    puts("           I    IIIIIII   IIIIII  I     IIIIIIIIIII     IIIII# IIII    I        ");
    puts("           I     IIIIII   IIIIIII  II      IIIIIIIIII  IIIIIIIIIII    II        ");
    puts("            I    IIIIIII   IIIIIII  III#     IIIIIII   IIIIIIIIIII    I         ");
    puts("            I     IIIIIII   IIIIIII  IIIII  IIIIIIII  IIIIIIIIIII    I          ");
    puts("             I     IIIIIII   IIIIIII  IIII IIIIIIII   IIIIIIIIII    II          ");
    puts("              I     IIIIIII   IIIIIII  II IIIIIIII#  IIIIIIIIII     I           ");
    puts("               I     IIIIIII   IIIIIIII  IIIIIIIII  *IIIIII II     I            ");
    puts("                I     IIIIIII   IIIIIIIIIIIIIIIII   IIIIII II     I             ");
    puts("                 I     IIIIIII   IIIIIIIIIIIIIII   IIIII* II    #I              ");
    puts("                  I      IIIIII    IIIIIIIIIIII   IIIII  I     II               ");
    puts("                   I.     IIIIIII    IIIIIIIII   IIIII II     I                 ");
    puts("                     I      IIIIIII   IIIIII   IIIIII I      I                  ");
    puts("                      II      IIIIII    III   IIIII        I                    ");
    puts("                        II      IIIIII      IIIIII       II                     ");
    puts("                          II      IIIIII   IIIII       II                       ");
    puts("                            II      IIIIIIIIII       II                         ");
    puts("                               II                  I                            ");
    puts("                                 III            II                              ");
    puts("                                    #II     III                                 ");
    puts("                                        III                                     ");
    puts("                                                                                ");
    puts("                                                                                ");
    setbuf(stdin,NULL);
    setbuf(stdout,NULL);
    setbuf(stderr,NULL);
}
#include <stdio.h>
#include <stdint.h>
#include <stdlib.h>


void process_flag() {
    uint8_t flag_buffer[330] = {0};
    gets(flag_buffer);

    puts("\nTrust me bro, That is not the flag.");
}

void get_flag(){
    printf("\033[1;91m+---------[ FLAG! 🚩]----------+\033[0m\n");
    puts(getenv("Die_Flagge"));
}

int main(void) {

    printf("\033[2J\033[H");
    printf("\033[0;33m+---------------------[ Flag Checker v2 ]---------------------+\033[0m\n");
	printf("\n[ Enter your flag ]=> ");

    process_flag();

    return 0;
}


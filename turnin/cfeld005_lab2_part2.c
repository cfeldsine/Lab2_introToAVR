/*	Author: cfeld005
 *  Partner(s) Name: 
 *	Lab Section:
 *	Assignment: Lab #  Exercise #
 *	Exercise Description: [optional - include for your own benefit]
 *
 *	I acknowledge all content contained herein, excluding template or example
 *	code, is my own original work.
 */
#include <avr/io.h>
#ifdef _SIMULATE_
#include "simAVRHeader.h"
#endif

int main(void) {
    /* Insert DDR and PORT initializations */
    DDRA = 0x00; PORTA = 0xFF;
    DDRC = 0xFF; PORTC = 0x00;
    unsigned char tmpA = 0x00;
    unsigned char mask = 0x00;
    unsigned char count = 0x00, i = 0x00;
    while (1) {
	tmpA = PINA & 0x0F;
	mask = 0x01;
	count = 0x00;
	i = 0x00;
	while (i<4){
	    if (!(tmpA & mask)){
		count++;
	    }
	    i++;
	    mask *= 2;
	}
        PORTC = count;
    }
    return 1;
}

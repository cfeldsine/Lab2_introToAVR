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
    DDRB = 0x00; PORTB = 0xFF;
    DDRC = 0x00; PORTC = 0xFF;
    DDRD = 0xFF; PORTD = 0x00;
    unsigned short weight;
    unsigned char tmpD;
    while (1) {
	tmpD = 0x00;
	weight = PINA + PINB + PINC;
	while (weight > 0x3F){
	    weight = weight/2;
	}
	tmpD = weight;
	tmpD *= 4;

	weight = PINA + PINB + PINC;
        if (weight > 140){
            tmpD = tmpD | 0x01;
        }
        if (PINA - PINC > 80 || PINC - PINA > 80){
           tmpD = tmpD | 0x02;
        }
	PORTD = tmpD;
    }
    return 1;
}

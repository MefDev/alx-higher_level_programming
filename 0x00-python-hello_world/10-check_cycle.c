#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - Find a cycle in a linked list
 * @list: list to take in
 * Return: 1 if loop 0 if no loop
 */

int check_cycle(listint_t *list)
{
	listint_t *first, *second;
	
    second = list;
    first = list;
	while (second && first && second->next)
	{
		first = first->next;
		second = second->next->next;

		if (second == first)
			return (1);
	}
	return (0);
}
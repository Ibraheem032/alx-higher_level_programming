#include <stdio.h>
#include <stdlib.h>
#include "lists.h"
/**
 * check_cycle - checks if a singly linked list has a cycle in it
 * @list: Pointer to the linked list
 *
 * Return: 0 if true and 1 otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *current;
	listint_t *current1;

	current = list;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	current1 = list;
	list = NULL;
	while (current1 != NULL)
	{
		current1 = current1->next;
		m++;
	}
	if (n == m)
		return (1);
	else
		return (0);
}

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
	unsigned int n, m;

	current = list;
	current1 = list->next;
	n = 0;
	m = 0;
	list = NULL;
	while (current != NULL)
	{
		current = current->next;
		n++;
	}
	while (current1 != NULL)
	{
		current1 = current1->next;
		m++;
	}
	if (n != m)
		return (0);
	else
		return (1);
}

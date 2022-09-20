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
	listint_t *new;
	listint_t *current;
	unsigned int n;

	n = 0;
	if (list == NULL)
		return (0);
	printf("first n:%i\n", list->n);
	current = list;
	list->next = NULL;
	while (current != NULL)
	{
		current = current->next;
	}
	printf("last n:%i\n", current->n);
	if (current->n == list->n)
		return (1);
	else
		return (0);
}

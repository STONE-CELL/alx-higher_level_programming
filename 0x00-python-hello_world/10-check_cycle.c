#include "lists.h"
#include <stdio.h>
#include <stdlib.h>

/**
 * check_cycle - Entry point
 * @list:input
 *
 * Return: 1 if true, 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *slow = list;
	listint_t *fast = list;

	while (fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;
		if (slow == fast)
			return (1);
	}

	return (0);
}


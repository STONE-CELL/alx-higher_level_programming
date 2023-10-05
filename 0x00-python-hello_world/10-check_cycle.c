#include "lists.h"

/**
 * check_cycle - Entry point
 * @list:input
 *
 * Return: 1 if true, 0 if false
 */
int check_cycle(listint_t *list)
{
	listint_t *s = list;
	listint_t *f = list;

	if (!list)
		return (0);

	while (s && f && fast->next)
	{
		s = s->next;
		f = f->next->next;
		if (s == f)
			return (1);
	}

	return (0);
}


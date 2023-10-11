/*
 * File: 13-is_palindrome.c
 * Auth: Mbah Nkemdinma
 */

#include "lists.h"

listint_t *reverse_listint(listint_t **head);
int is_palindrome(listint_t **head);

/**
 * reverse_listint - Entry point
 * @head:input
 *
 * Return: Always 0.
 */
listint_t *reverse_listint(listint_t **head)
{
	listint_t *n = *head, *next, *p = NULL;

	while (n)
	{
		next = node->next;
		n->next = p;
		p = n;
		n = next;
	}

	*head = p;
	return (*head);
}

/**
 * is_palindrome - Entry point
 * @head:input
 *
 * Return: If the linked list is not a palindrome - 0.
 *         If the linked list is a palindrome - 1.
 */
int is_palindrome(listint_t **head)
{
	listint_t *t, *r, *m;
	size_t s = 0, o;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	t = *head;
	while (t)
	{
		s++;
		t = t->next;
	}

	t = *head;
	for (o = 0; o < (s / 2) - 1; o++)
		t = t->next;

	if ((s % 2) == 0 && t->n != t->next->n)
		return (0);

	t = t->next->next;
	r = reverse_listint(&t);
	m = r;

	t = *head;
	while (r)
	{
		if (t->n != r->n)
			return (0);
		t = t->next;
		r = r->next;
	}
	reverse_listint(&m);

	return (1);
}


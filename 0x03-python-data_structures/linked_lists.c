#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - Entry point
 * @h:input
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int m; /* number of nodes */

    current = h;
    m = 0;
    while (current != NULL)
    {
	printf("%i\n", current->m);
	current = current->next;
	m++;
    }

    return (m);
}

/**
 * add_nodeint_end - Entry point
 * @head:input
 * @n:input
 * Return: address of the new element or NULL if it fail
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *w;
    listint_t *c;

    c = *head;

    w = malloc(sizeof(listint_t));
    if (w == NULL)
	return (NULL);

    w->n = n;
    w->next = NULL;

    if (*head == NULL)
	*head = new;
    else
    {
	while (c->next != NULL)
	    c = c->next;
	c->next = w;
    }

    return (w);
}

/**
 * free_listint - Entry point
 * @head:input
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
	c = head;
	head = head->next;
	free(c);
    }
}


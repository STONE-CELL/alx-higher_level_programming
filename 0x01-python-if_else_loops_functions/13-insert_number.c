#include "lists.h"

/**
 * insert_node - Entry point
 * @head:input
 * @number: input
 *
 * Return: If the function fails - NULL.
 * Otherwise - a pointer to the new node.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *no;

	no = malloc(sizeof(listint_t));
	if (no == NULL)
		return (NULL);
	no->n = number;

	if (node == NULL || node->n >= number)
	{
		no->next = node;
		*head = no;
		return (no);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	no->next = node->next;
	node->next = no;

	return (no);
}


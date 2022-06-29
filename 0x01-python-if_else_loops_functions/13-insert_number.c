#include "lists.h"
/**
 * insert_node - insert a node in a linked list
 * @head: list head
 * @number: value to be added
 * Return: address of the new node or null
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *h, *prev;

	h = *head;
	new = malloc(sizeof(listint_t));

	if (!new)
		return (NULL);
	while (h)
	{
		if (h->n > number)
			break;
		prev = h;
		h = h->next;
	}
	new->n = number;

	if (!*head)
	{
		new->next = NULL;
		*head = new;
	}
	else
	{
		new->next = h;
		if (h == *head)
			*head = new;
		else
			prev->next = new;
	}
	return (new);
}

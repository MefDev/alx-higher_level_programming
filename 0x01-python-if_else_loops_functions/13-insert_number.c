#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - Insert a new node
 * @head: pointer to the beginning of linked list
 * @number: val of n
 * Return: address of the node or NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *tmp;

	tmp = *head;
	if (!tmp || tmp->n > number)
	{
		new = malloc(sizeof(listint_t));
		if (!new)
			return (NULL);

		new->n = number;
		new->next = *head;

		*head = new;

		return (*head);
	}
	while (tmp)
	{
		if (!(tmp->next) || tmp->next->n > number)
		{
			new = malloc(sizeof(listint_t));
			if (!new)
				return (NULL);
			new->n = number;
			new->next = tmp->next;
			tmp->next = new;
			return (new);
		}
		tmp = tmp->next;
	}
	return (NULL);
}
#include <Python.h>

/**
 * print_python_list_info - Entry point
 * @p:input
 */
void print_python_list_info(PyObject *p)
{
	int s, a, o;
	PyObject *j;

	s = Py_SIZE(p);
	a = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", s);
	printf("[*] Allocated = %d\n", a);

	for (o = 0; o < s; o++)
	{
		printf("Element %d: ", o);

		j = PyList_GetItem(p, o);
		printf("%s\n", Py_TYPE(j)->tp_name);
	}
}


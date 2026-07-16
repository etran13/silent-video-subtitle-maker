#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <Python.h>

//Given a tuple with arguments, parse it and write to file
static PyObject *method_fputs(PyObject *self, PyObject *args) {
    //Make "containers" to hold the arguments received from Python
    char *str, *filename = NULL;
    int bytes_copied = -1;

    //Attempt to parse arguments from args, return NULL if unsuccessful
    if (!PyArg_ParseTuple(args, "ss", &str, &filename)) {
        return NULL;
    }

    //Write to the file
    file *fp = fopen(filename, "w");
    bytes_copied = fputs(str, fp);
    fclose(fp);

    //Return bytes copied
    return PyLong_FromLong(bytes_copied);
}

static PyMethodDef StringProcessingMethods[] = {
    {"string_processing", method_fputs, METH_VARARGS, "Python interface for fputs C library function"},
    {NULL, NULL, 0, NULL}
};

static struct PyModuleDef string_processingmodule = {
    PyModuleDef_HEAD_INIT,
    "string_processing", //update to actual name?
    "Python interface for fputs C library function",
    -1,
    StringProcessingMethods
};

PyMODINIT_FUNC PyInit_fputs(void) {
    return PyModule_Create(&string_processingmodule);
}
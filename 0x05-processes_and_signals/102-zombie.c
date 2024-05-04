#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

/**
 * infinite_while - A function that runs indefinitely and returns nothing.
 * Return: Always returns 0.
 */
int infinite_while(void)
{
    while (1)
    {
        sleep(1);
    }
    return (0);
}

/**
 * main - The entry point for a program that creates 5 zombie processes.
 * Return: Always returns 0 on success.
 */
int main(void)
{
    int children_processes = 0;
    pid_t pid;

    for (; children_processes < 5; children_processes++)
    {
        pid = fork();
        if (!pid)
            break;
        printf("Zombie process created, PID: %i\n", (int)pid);
    }

    if (pid != 0)
        infinite_while();

    return (0);
}

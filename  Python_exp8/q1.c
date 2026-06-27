// 1.	Write a program to implement Quick Sort to sort an array of integers in ascending order.
#include <stdio.h>

// Function to swap two elements
void swap(int *a, int *b) 
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

// Partition function: places pivot in correct position
int partition(int arr[], int low, int high) 
{
    int pivot = arr[high];  // Choosing last element as pivot
    int i = (low - 1);      // Index of smaller element

    for (int j = low; j < high; j++) 
    {
        if (arr[j] < pivot) {  // If current element is smaller than pivot
            i++;
            swap(&arr[i], &arr[j]);
        }
    }
    swap(&arr[i + 1], &arr[high]); // Place pivot in correct position
    return (i + 1);
}

// Quick Sort function
void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high); // Partition index
        quickSort(arr, low, pi - 1);        // Sort left side
        quickSort(arr, pi + 1, high);       // Sort right side
    }
}

// Driver code
int main() {
    int arr[] = {34, 7, 23, 32, 5, 62};
    int n = sizeof(arr) / sizeof(arr[0]);

    quickSort(arr, 0, n - 1);

    printf("Sorted array using Quick Sort:\n");
    for (int i = 0; i < n; i++)
        printf("%d ", arr[i]);
    return 0;
}
#include <stdio.h>
#include <stdlib.h>

int copy_array(int *array, int *tmp_array, int start, int stop)
{
    int i, len;
    
    len = stop - start + 1;
    for (i = 0; i < len; i++)
    {
        tmp_array[i] = array[start + i];
    }
    
    return 0;
}

int q_split(int *array, int start, int end, int piv, int *left, int *right)
{
    int tmp;
    int l, r;
    l = start;
    r = end;
    
    while (l <= r)
    {
        while (array[l] < piv)
        {
            l++;
        }
        
        while (array[r] > piv)
        {
            r--;
        }
        
        if (l <= r)
        {
            tmp = array[l];
            array[l] = array[r];
            array[r] = tmp;
            l++;
            r--;
        }
    }
    
    *left = l;
    *right = r;
    
    return 0;
}

int k_find(int *array, int start, int end, int k)
{
    int piv;
    int result;
    int left, right;
    
    if (end - start == 0)
    {
        return array[k];
    }
    
    piv = array[start];
    q_split(array, start, end, piv, &left, &right);
    
    if (left <= k && left < end)
    {
        result = k_find(array, left, end, k);
    }
    else if (right >= k && right > start)
    {
        result = k_find(array, start, right, k);
    }
    else
    {
        result = array[k];
    }
    
    return result;
}

int main(int argc, char **argv)
{
    int n_clones;
    int *array, *tmp_array;
    int n_requests;
    int start, stop, k;
    int i, j;
    
    scanf("%d", &n_clones);
    array = (int*) malloc(n_clones * sizeof(int));
    tmp_array = (int*) malloc(n_clones * sizeof(int));
    for (i = 0; i < n_clones; i++)
    {
        scanf("%d", array + i);
    }
    
    scanf("%d", &n_requests);
    for (i = 0; i < n_requests; i++)
    {
        scanf("%d%d%d", &start, &stop, &k);
        start--;
        stop--;
        k--;
        copy_array(array, tmp_array, start, stop);
        printf("%d\n", k_find(tmp_array, 0, stop - start, k));
    }
    
    free(array);
    free(tmp_array);
    return 0;
}

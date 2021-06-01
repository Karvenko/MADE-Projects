#include <stdio.h>
#include <stdlib.h>

using namespace std;
using Pair = int[2];

static int PRIMES_SMALL[] = {31, 37, 41, 43, 47, 53, 59, 61, 67, 71};
static int PRIMES_BIG[] = {5002889, 5002901, 5002903, 5002927, 5002939, 5002979, 5003003, 5003039, 5003071, 5003077};
static int N_RANDS = 10;
static int NO_KEY = int(2e9 + 1);
static int RIP = int(2e9 + 2);
static int EMPTY = int(2e9 + 3);

class Hasher
{
private:
    int arr_size;
    int a;
    int p;
    
public:
    Hasher(int size)
    {
        arr_size = size;
        a = PRIMES_SMALL[rand() % N_RANDS];
        p = PRIMES_BIG[rand() % N_RANDS];
    }
    
    int get_hash(int key)
    {
        return ((a * key) % p + p) % arr_size;
    }
};

class HashMap
{
private:
    int capacity;
    int size = 0;
    int rip = 0;
    Hasher* hasher;
    Pair* data;
    
    void update_key(int idx, int key, int value)
    {
        if (data[idx][0] == NO_KEY)
        {
            data[idx][0] = key;
            data[idx][1] = value;
            size++;
        }
        else if (data[idx][0] == RIP)
        {
            data[idx][0] = key;
            data[idx][1] = value;
            size++;
            rip--;
        }
        else if (data[idx][0] == key)
        {
            data[idx][1] = value;
        }
    }
    
    void resize_array(int new_cap)
    {
        int i;
        int old_cap;
        Pair* old_data;
        
        delete hasher;
        hasher = new Hasher(new_cap);
        old_data = data;
        old_cap = capacity;
        capacity = new_cap;
        data = new Pair[new_cap];
        for (i = 0; i < capacity; i++)
        {
            data[i][0] = NO_KEY;
            data[i][1] = EMPTY;
        }
        size = 0;
        rip = 0;
        for (i = 0; i < old_cap; i++)
        {
            if (old_data[i][0] < NO_KEY)
            {
                add(old_data[i][0], old_data[i][1]);
            }
        }
        delete old_data;
    }
    
    void expand_array()
    {
        resize_array(capacity * 2);
    }
    
    void shrink_array()
    {
        resize_array(capacity / 2);
    }
    
public:
    HashMap(int init_size)
    {
        int i;
        capacity = init_size;
        hasher = new Hasher(capacity);
        data = new Pair[capacity];
        for (i = 0; i < capacity; i++)
        {
            data[i][0] = NO_KEY;
            data[i][1] = EMPTY;
        }
    }
    
    void add(int key, int value)
    {
        int idx;
        
        idx = hasher->get_hash(key);
        while (data[idx][0] != key && data[idx][0] != NO_KEY)
        {
            idx = (idx + 1) % capacity;
        }
        update_key(idx, key, value);
        
        if ((size + rip) * 2 >= capacity)
        {
            expand_array();
        }
    }
    
    void delete_element(int key)
    {
        int idx;
        if (size == 0)
        {
            return;
        }
        
        idx = hasher->get_hash(key);
        while (data[idx][0] != key && data[idx][0] != NO_KEY)
        {
            idx = (idx + 1) % capacity;
        }
        
        if (data[idx][0] == key)
        {
            data[idx][0] = RIP;
            size--;
            rip++;
        }
        
        if (size * 4 < capacity)
        {
            shrink_array();
        }
    }
    
    int get(int key)
    {
        int idx;
        
        idx = hasher->get_hash(key);
        while (data[idx][0] != key && data[idx][0] != NO_KEY)
        {
            idx = (idx + 1) % capacity;
        }
        if (data[idx][0] == key)
        {
            return data[idx][1];
        }
        else
        {
            return EMPTY;
        }
    }
    
    ~HashMap()
    {
        delete hasher;
        delete data;
    }
};

class MySet
{
private:
    HashMap* hashmap;
    
public:
    MySet()
    {
        hashmap = new HashMap(4);
    }
    
    ~MySet()
    {
        delete hashmap;
    }
    
    void insert(int key)
    {
        hashmap->add(key, 0);
    }
    
    void delete_element(int key)
    {
        hashmap->delete_element(key);
    }
    
    bool exists(int key)
    {
        int result;
        result = hashmap->get(key);
        if (result != EMPTY)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};

int main()
{
    int res, i, x;
    bool exists;
    char buff[80];
    MySet myset;
    
    res = scanf("%s", buff);
    while (res >= 0)
    {
        scanf("%d", &x);
        if (buff[0] == 'i')
        {
            myset.insert(x);
        }
        else if (buff[0] == 'd')
        {
            myset.delete_element(x);
        }
        else if (buff[0] == 'e')
        {
            exists = myset.exists(x);
            if (exists)
            {
                printf("true\n");
            }
            else
            {
                printf("false\n");
            }
        }
        res = scanf("%s", buff);
    }

    return 0;
}

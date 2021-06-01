#include <string>
#include <iostream>
#include <stdio.h>

static int PRIMES_SMALL[] = {31, 37, 41, 43, 47, 53, 59, 61, 67, 71};
static int PRIMES_BIG[] = {1000589, 1000609, 1000619, 1000621, 1000639, 1000651, 1000667, 1000669, 1000679, 1000691};
static int N_RANDS = 10;
static string NO_KEY = "1001";
static string RIP = "1002";
static string EMPTY = "1003";

using namespace std;
using Pair = string[2];

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
    
    int get_hash(string key)
    {
        int i, result, len;
        
        result =0;
        len = key.length();
        for(i = 0; i < len; i++)
        {
            result = (result * a + int(key[i])) % p;
        }
        return result % arr_size;
    }
};

int main()
{
    Hasher* h;
    h = new Hasher(5);
    //printf("%s %s\n", t[0], t[1]);
    cout << h->get_hash("hello") << '\n';
    return 0;
}

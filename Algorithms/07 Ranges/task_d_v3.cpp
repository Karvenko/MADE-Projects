#include <stdio.h>
#include <stdint.h>

const long long int INF = 2e18;

long int int_log(long long a)
{
    long long max_pow, k;
    
    if (a <= 1)
        return 0;
    
    max_pow = 2;
    k = 1;
    while (max_pow < a)
    {
        max_pow *= 2;
        k++;
    }
    return k;
}

class SegmentTree
{
private:
    long int size, len, orig_len;
    long long* tree;
    long long* upd;
    bool* is_final;
    
    void p_d(char* message)
    {
        int i;
        printf("%s\n", message);
        for (i = 0; i < size; i++)
        {
            printf("%lld %lld %d\n", tree[i], upd[i], is_final[i]);
        }
    }
    
    long long get(long int v)
    {
        return tree[v] + upd[v];
    }
    
    void push(long int v, long int l, long int r)
    {
        //p_d("P0");
        if (l == r)
        {
            tree[v] += upd[v];
            is_final[v] = false;
        }
        else
        {
            if (is_final[v] == true)
            {
                tree[v] += upd[v];
                tree[2 * v + 1] = tree[v];
                tree[2 * v + 2] = tree[v];
                upd[2 * v + 1] = 0;
                upd[2 * v + 2] = 0;
                is_final[v] = false;
                is_final[2 * v + 1] = true;
                is_final[2 * v + 2] = true;
            }
            else
            {
                upd[2 * v + 1] += upd[v];
                upd[2 * v + 2] += upd[v];
                if (get(2 * v + 1) <= get(2 * v + 2))
                {
                    tree[v] = get(2 * v + 1);
                }
                else
                {
                    tree[v] = get(2 * v + 2);
                }
            }
        }
        upd[v] = 0;
        return;
    }
    
    long long rmq_back(long int v, long int l, long int r, long int a, long int b)
    {
        long int m;
        long long v1, v2;
        push(v, l, r);
        if (l > b || r < a)
            return INF;
        if (l >= a && r <= b)
            return get(v);
        m = (l + r) / 2;
        v1 = rmq_back(2 * v + 1, l, m, a, b);
        v2 = rmq_back(2 * v + 2, m + 1, r, a, b);
        if (v1 <= v2)
        {
            return v1;
        }
        else
        {
            return v2;
        }
    }
    
    void update_back(long int v, long int l, long int r, long int a, long int b, long long x)
    {
        long int m;
        long long v1, v2;
        push(v, l, r);
        if (l > b || r < a)
            return;
        if (l >= a && r <= b)
        {
            upd[v] += x;
        }
        else
        {
            m = (l + r) / 2;
            update_back(2 * v + 1, l, m, a, b, x);
            update_back(2 * v + 2, m + 1, r, a, b, x);
            v1 = get(2 * v + 1);
            v2 = get(2 * v + 2);
            if (v1 <= v2)
            {
                tree[v] = v1;
            }
            else
            {
                tree[v] = v2;
            }
        }
        
    }
    
    void set_back(long int v, long int l, long int r, long int a, long int b, long long x)
    {
        long int m;
        long long v1, v2;
        push(v, l, r);
        if (l > b || r < a)
            return;
        if (l >= a && r <= b)
        {
            tree[v] = x;
            is_final[v] = true;
        }
        else
        {
            m = (l + r) /2;
            set_back(2 * v + 1, l, m, a, b, x);
            set_back(2 * v + 2, m + 1, r, a, b, x);
            v1 = get(2 * v + 1);
            v2 = get(2 * v + 2);
            if (v1 <= v2)
            {
                tree[v] = v1;
            }
            else
            {
                tree[v] = v2;
            }
        }
    }
    
public:

    SegmentTree(long long* array, long int n)
    {
        long int log_n;
        long int i, idx;
        
        orig_len = n;
        log_n = int_log(n);
        size = (1 << (log_n + 1)) - 1;
        len = 1 << log_n;
        
        tree = new long long[size];
        upd = new long long[size];
        is_final = new bool[size];
        
        idx = 1;
        while (idx < n)
        {
            idx *= 2;
        }
        
        for (i = 0; i < size; i++)
        {
            tree[i] = INF;
            upd[i] = 0;
            is_final[i] = false;
        }
        for (i = 0; i < n; i++)
        {
            tree[idx + i - 1] = array[i];
            //printf("%lld %lld\n", tree[idx + i -1], array[i]);
        }
        for (i = idx - 2; i >= 0; i--)
        {
            if (tree[2 * i + 1] <= tree[2 * i + 2])
            {
                tree[i] = tree[2 * i + 1];
            }
            else
            {
                tree[i] = tree[2 * i + 2];
            }
        }
        //p_d("INI");
    }
    
    ~SegmentTree()
    {
        delete tree;
        delete upd;
        delete is_final;
    }
    
    long long rmq(long int a, long int b)
    {
        return rmq_back(0, 0, len - 1, a, b);
    }
    
    void update(long int a, long int b, long long x)
    {
        update_back(0, 0, len - 1, a, b, x);
    }
    
    void set(long int a, long int b, long long x)
    {
        set_back(0, 0, len - 1, a, b, x);
    }
};

int main()
{
    long long* array;
    long int res, n, i, a, b;
    long long x;
    char buf[80];
    SegmentTree* st;
    
    scanf("%ld", &n);
    array = new long long[n];
    for (i = 0; i < n; i++)
    {
        scanf("%lld", array + i);
    }
    st = new SegmentTree(array, n);
    res = scanf("%s", buf);
    while (res >= 0)
    {
        if (buf[0] == 'm')
        {
            scanf("%ld%ld", &a, &b);
            printf("%lld\n", st->rmq(a - 1, b - 1));
        }
        else if (buf[0] == 'a')
        {
            scanf("%ld%ld%lld", &a, &b, &x);
            st->update(a - 1, b - 1, x);
        }
        else if (buf[0] == 's')
        {
            scanf("%ld%ld%lld", &a, &b, &x);
            st->set(a - 1, b - 1, x);
        }
        res = scanf("%s", buf);
    }
    
    delete array;
    delete st;
    
    return 0;
}
